import { promises as fs } from 'fs';
import axios from 'axios';
import path from 'path';
import puppeteer from 'puppeteer';
import { spawn } from 'child_process';

/**
 * Converts a string to kebab-case format
 * @param {string} str - The input string to convert
 * @returns {Promise<string>} The kebab-cased string with only lowercase letters, numbers, and hyphens
 */
async function toKebabCase(str: string): Promise<string> {
    return str.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

/**
 * Executes a shell command
 * @param {string} command - The command to execute
 * @param {string[]} args - Arguments for the command
 * @param {string} cwd - Current working directory
 * @param {boolean} silent - Whether to suppress output
 * @returns {Promise<void>}
 */
const executeCommand = async (
    command: string,
    args: string[],
    cwd: string,
    silent = false
): Promise<void> => {
    return new Promise((resolve, reject) => {
        const process = spawn(command, args, {
            stdio: silent ? 'pipe' : 'inherit', // Capture output if silent
            cwd,
        });

        let output = '';
        let errorOutput = '';

        process.stdout?.on('data', (data) => {
            output += data.toString();
        });

        process.stderr?.on('data', (data) => {
            errorOutput += data.toString();
        });

        process.on('close', (code) => {
            if (code === 0) {
                resolve();
            } else {
                console.error(`Command failed: ${command} ${args.join(' ')}`);
                console.error(`Exit code: ${code}`);
                console.error(`Output: ${output}`);
                console.error(`Error output: ${errorOutput}`);
                reject(new Error(`Command "${command} ${args.join(' ')}" failed with code ${code}`));
            }
        });

        process.on('error', (err) => {
            console.error('Process error:', err);
            reject(err);
        });
    });
};
interface CodeSnippet {
    lang: string;
    langSlug: string;
    code: string;
}

interface ProblemDetails {
    content: string;
    codeSnippets: CodeSnippet[];
    difficulty: string;
    questionId: string;
    title: string;
}

/**
 * Formats the problem content into a file with comments
 * @param {string} language - The programming language
 * @param {string} problemContent - The problem description in HTML
 * @param {string} code - The code snippet
 * @returns {string} The formatted file content
 */
function formatProblemFile(language: string, problemContent: string, code: string): string {
    const htmlToComment = (html: string) => {
        const text = html
            .replace(/<[^>]+>/g, '')
            .replace(/&nbsp;/g, ' ')
            .replace(/&lt;/g, '<')
            .replace(/&gt;/g, '>')
            .replace(/&quot;/g, '"')
            .replace(/&#39;/g, "'")
            .replace(/&amp;/g, '&');

        const commentMap: { [key: string]: [string, string] } = {
            python: ['"""', '"""'],
            typescript: ['/*', '*/'],
            javascript: ['/*', '*/'],
            java: ['/*', '*/'],
            cpp: ['/*', '*/'],
            c: ['/*', '*/'],
            csharp: ['/*', '*/'],
            dart: ['/*', '*/'],
            php: ['/*', '*/'],
            go: ['/*', '*/'],
            rust: ['/*', '*/'],
            ruby: ['=begin', '=end'],
            swift: ['/*', '*/'],
            kotlin: ['/*', '*/'],
        };

        const [start, end] = commentMap[language] || ['/*', '*/'];
        return `${start}\n${text.trim()}\n${end}\n\n`;
    };

    return `${htmlToComment(problemContent)}${code}`;
}

/**
 * Fetches the CSRF token from LeetCode's homepage
 * @returns {Promise<string>} The CSRF token
 */
async function fetchCsrfToken(): Promise<string> {
    const response = await axios.get('https://leetcode.com/', {
        headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        },
    });

    // Extract the CSRF token from the response
    const csrfTokenMatch = response.data.match(/var csrfToken = '([^']+)'/);
    if (!csrfTokenMatch) {
        throw new Error('CSRF token not found');
    }

    return csrfTokenMatch[1];
}

/**
 * Fetches the daily LeetCode challenge using Puppeteer
 * @returns {Promise<any>} The daily challenge details
 */
async function getDailyLeetcodeChallengeWithPuppeteer(): Promise<any> {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    try {
        console.log('Navigating to LeetCode...');
        await page.goto('https://leetcode.com/problemset/all/', { waitUntil: 'networkidle2' });

        // Wait for the calendar to load
        await page.waitForSelector('[href^="/problems/"][class*="h-8 w-8"]', { timeout: 5000 });

        console.log('Extracting daily challenge...');
        const dailyChallenge = await page.evaluate(() => {
            // Find the element with the green background (current day)
            const dailyChallengeElement = document.querySelector('[href^="/problems/"] span[class*="bg-green-s"]')?.closest('a');
            if (!dailyChallengeElement) return null;

            // Extract the problem slug from the href
            const href = dailyChallengeElement.getAttribute('href');
            const match = href?.match(/\/problems\/([^/]+)/);
            return match ? match[1] : null;
        });

        if (!dailyChallenge) {
            throw new Error('Failed to extract daily challenge');
        }

        return {
            data: {
                activeDailyCodingChallengeQuestion: {
                    question: {
                        titleSlug: dailyChallenge,
                    },
                },
            },
        };
    } finally {
        await browser.close();
    }
}

/**
 * Checks if a file has non-comment content
 * @param {string} filePath - The path to the file
 * @returns {Promise<boolean>} Whether the file has non-comment content
 */
async function hasContent(filePath: string): Promise<boolean> {
    try {
        const content = await fs.readFile(filePath, 'utf-8');
        const nonCommentContent = content
            .split('\n')
            .filter(
                (line) =>
                    !line.trim().startsWith('/*') &&
                    !line.trim().startsWith('*/') &&
                    !line.trim().startsWith('//') &&
                    line.trim().length > 0
            )
            .join('')
            .trim();
        return nonCommentContent.length > 0;
    } catch {
        return false;
    }
}

/**
 * Fetches the daily LeetCode challenge and creates solution files in multiple languages
 * @throws {Error} If the API request fails or file operations fail
 */
async function getDailyLeetcodeChallenge(): Promise<void> {
    console.log('Fetching daily LeetCode challenge...');
    const url = 'https://leetcode.com/graphql';

    try {
        // Fetch the CSRF token
        const csrfToken = await fetchCsrfToken();

        const headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://leetcode.com/',
            'Origin': 'https://leetcode.com',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrfToken,
        };

        const dailyQuery = await axios.post(
            url,
            {
                query: `
                    query questionOfToday {
                        activeDailyCodingChallengeQuestion {
                            question {
                                questionId
                                title
                                titleSlug
                                difficulty
                            }
                        }
                    }
                `,
            },
            { headers }
        );

        const question = dailyQuery.data.data.activeDailyCodingChallengeQuestion.question;
        console.log('Daily Challenge (API):', question);

        const titleSlug = question.titleSlug;

        const [contentResponse, snippetsResponse] = await Promise.all([
            axios.post(
                url,
                {
                    query: `
                        query questionContent($titleSlug: String!) {
                            question(titleSlug: $titleSlug) {
                                content
                                mysqlSchemas
                            }
                        }
                    `,
                    variables: { titleSlug },
                },
                { headers }
            ),
            axios.post(
                url,
                {
                    query: `
                        query questionEditorData($titleSlug: String!) {
                            question(titleSlug: $titleSlug) {
                                codeSnippets {
                                    lang
                                    langSlug
                                    code
                                }
                            }
                        }
                    `,
                    variables: { titleSlug },
                },
                { headers }
            ),
        ]);

        const details: ProblemDetails = {
            content: contentResponse.data.data.question.content,
            codeSnippets: snippetsResponse.data.data.question.codeSnippets,
            difficulty: question.difficulty,
            questionId: question.questionId,
            title: question.title,
        };

        console.log('Challenge details:');
        console.log(`Question ID: ${details.questionId}`);
        console.log(`Title: ${details.title}`);
        console.log(`Difficulty: ${details.difficulty}`);

        const kebabTitle = await toKebabCase(details.title);
        const filePrefix = `${details.questionId}-${kebabTitle}`;

        const extensions: { [key: string]: string } = {
            python: 'py',
            typescript: 'ts',
            javascript: 'js',
            java: 'java',
            cpp: 'cpp',
            c: 'c',
            csharp: 'cs',
            dart: 'dart',
            php: 'php',
            go: 'go',
            rust: 'rs',
            ruby: 'rb',
            swift: 'swift',
            kotlin: 'kt',
        };

        const existingFiles: string[] = [];
        const createdFiles: string[] = [];
        const skippedFiles: string[] = [];

        for (const [language, extension] of Object.entries(extensions)) {
            const dirPath = path.join(language, details.difficulty.toLowerCase());
            const fileName =
                language === 'dart'
                    ? `${details.questionId}_${kebabTitle.replace(/-/g, '_')}.${extension}`
                    : `${filePrefix}.${extension}`;
            const filePath = path.join(dirPath, fileName);

            try {
                await fs.access(filePath);
                const hasExistingContent = await hasContent(filePath);

                if (hasExistingContent) {
                    console.log(`File exists with content, skipping: ${filePath}`);
                    skippedFiles.push(filePath);
                    continue;
                }

                existingFiles.push(filePath);
                console.log(`File exists but empty, replacing: ${filePath}`);
            } catch {
                await fs.mkdir(dirPath, { recursive: true });
            }

            const snippet = details.codeSnippets.find((s) => s.langSlug === language);
            const content = formatProblemFile(language, details.content, snippet?.code || '');

            await fs.writeFile(filePath, content);
            if (!existingFiles.includes(filePath)) {
                createdFiles.push(filePath);
            }
            console.log(`${existingFiles.includes(filePath) ? 'Updated' : 'Created'} file: ${filePath}`);
        }

        if (skippedFiles.length > 0) {
            console.log('\nSkipped Files (already have content):');
            skippedFiles.forEach((file) => console.log(file));
        }

        if (existingFiles.length > 0) {
            console.log('\nUpdated Empty Files:');
            existingFiles.forEach((file) => console.log(file));
        }

        if (createdFiles.length > 0) {
            console.log('\nNewly Created Files:');
            createdFiles.forEach((file) => console.log(file));
        }


        await executeCommand('bun', ['run', 'problems', question.titleSlug, 'all'], process.cwd(), true);
    } catch (initialError) {
        console.error('Direct API call failed:', (initialError as Error).message);
        console.log('Attempting with Puppeteer...');

        try {
            const puppeteerResult = await getDailyLeetcodeChallengeWithPuppeteer();
            const question = puppeteerResult.data.activeDailyCodingChallengeQuestion.question;
            console.log('Daily Challenge (Puppeteer):', question);

            await executeCommand('bun', ['run', 'problems', question.titleSlug, 'all', '--non-interactive'], `${process.cwd()}/leetcode-solutions`, true);
        } catch (puppeteerError) {
            console.error('Puppeteer error:', puppeteerError);
            throw new Error('Both API and Puppeteer approaches failed');
        }
    }
}

/**
 * Main class to handle daily LeetCode challenge operations
 * @class
 */
class Daily {
    /**
     * Executes the daily LeetCode challenge processing
     * @static
     * @async
     * @returns {Promise<void>}
     */
    static async run(): Promise<void> {
        await getDailyLeetcodeChallenge();
    }
}

// Execute if this is the main module
if (require.main === module) {
    Daily.run().catch(console.error);
}

export { Daily };
