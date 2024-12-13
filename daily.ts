/**
 * @fileoverview Fetches and processes the  daily LeetCode challenge, creating solution files across multiple languages
 */

import { promises as fs } from 'fs';
import axios from 'axios';
import path from 'path';

/**
 * Converts a string to kebab-case format
 * @param {string} str - The input string to convert
 * @returns {Promise<string>} The kebab-cased string with only lowercase letters, numbers and hyphens
 */
async function toKebabCase(str: string): Promise<string> {
    return str.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

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
    }

    return `${htmlToComment(problemContent)}${code}`;
}

/**
 * Fetches the daily LeetCode challenge and creates solution files in multiple languages
 * @throws {Error} If the API request fails or file operations fail
 */
async function getDailyLeetcodeChallenge() {
    const url = 'https://leetcode.com/graphql';

    try {
        const dailyQuery = await axios.post(url, {
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
      `
        }, {
            headers: {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            },
        });

        const question = dailyQuery.data.data.activeDailyCodingChallengeQuestion.question;
        const titleSlug = question.titleSlug;

        const [contentResponse, snippetsResponse] = await Promise.all([
            axios.post(url, {
                query: `
          query questionContent($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
              content
              mysqlSchemas
            }
          }
        `,
                variables: { titleSlug }
            }),
            axios.post(url, {
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
                variables: { titleSlug }
            })
        ]);

        const details: ProblemDetails = {
            content: contentResponse.data.data.question.content,
            codeSnippets: snippetsResponse.data.data.question.codeSnippets,
            difficulty: question.difficulty,
            questionId: question.questionId,
            title: question.title
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

        for (const [language, extension] of Object.entries(extensions)) {
            const dirPath = path.join(language, details.difficulty.toLowerCase());

            const fileName = language === 'dart'
                ? `${details.questionId}_${kebabTitle.replace(/-/g, '_')}.${extension}`
                : `${filePrefix}.${extension}`;

            const filePath = path.join(dirPath, fileName);

            try {
                await fs.access(filePath);
                existingFiles.push(filePath);
                console.log(`File already exists: ${filePath}`);
            } catch {
                await fs.mkdir(dirPath, { recursive: true });

                const snippet = details.codeSnippets.find(s => s.langSlug === language);
                const content = formatProblemFile(language, details.content, snippet?.code || '');

                await fs.writeFile(filePath, content);
                createdFiles.push(filePath);
                console.log(`Created file: ${filePath}`);
            }
        }

        if (existingFiles.length > 0) {
            console.log('\nExisting Challenge Files:');
            existingFiles.forEach(file => console.log(file));
        }

        if (createdFiles.length > 0) {
            console.log('\nNewly Created Challenge Files:');
            createdFiles.forEach(file => console.log(file));
        }

        console.log(`Successfully processed challenge files`);
    } catch (error) {
        console.error('Error: Failed to fetch daily LeetCode challenge', error);
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
    static async run() {
        await getDailyLeetcodeChallenge();
    }
}

// Execute if this is the main module
if (require.main === module) {
    Daily.run().catch(console.error);
}

export { Daily };
