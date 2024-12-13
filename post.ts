import axios from 'axios';
import { createInterface } from 'readline';
import { promises as fs } from 'fs';
import path from 'path';
import { generateRaySoImage } from './ray';
import { problems } from './constant';
import { SocialPoster } from './social';
import { config } from './config';

interface RaysoOptions {
    code: string;
    title?: string;
    theme?: string;
    background?: boolean;
    darkMode?: boolean;
    padding?: number;
    language?: string;
}

async function promptYesNo(question: string): Promise<boolean> {
    const rl = createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise((resolve) => {
        rl.question(`${question} (y/n): `, (answer) => {
            rl.close();
            resolve(answer.toLowerCase().startsWith('y'));
        });
    });
}

async function promptLanguages(languages: { [key: string]: string }): Promise<string[]> {
    const rl = createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log('\nAvailable languages:');
    Object.keys(languages).forEach((lang, index) => {
        console.log(`${index + 1}. ${lang}`);
    });

    return new Promise((resolve) => {
        rl.question('\nEnter language numbers (comma-separated) or "all": ', (answer) => {
            rl.close();
            if (answer.toLowerCase() === 'all') {
                resolve(Object.keys(languages));
            } else {
                const selectedIndices = answer.split(',').map(n => parseInt(n.trim()) - 1);
                const selectedLanguages = selectedIndices
                    .filter(i => i >= 0 && i < Object.keys(languages).length)
                    .map(i => Object.keys(languages)[i]);
                resolve(selectedLanguages);
            }
        });
    });
}

async function generateCodeImage(options: RaysoOptions): Promise<Uint8Array> {
    try {
        return generateRaySoImage(options.code, {
            language: options.language,
            title: options.title,
            theme: options.theme,
            darkMode: options.darkMode,
            padding: options.padding,
            background: options.background
        });
    } catch (error) {
        console.error('RaySo generation error:', error);
        throw error;
    }
}

async function processCodeFile(
    filePath: string,
    languages: { [key: string]: string }
): Promise<void> {
    try {
        await fs.access(filePath);
        const fileContent = await fs.readFile(filePath, 'utf-8');
        const fileName = path.basename(filePath);
        const difficulty = path.basename(path.dirname(filePath));
        const problemName = path.parse(fileName).name;

        console.log(`Processing file: ${fileName}`);

        const useAllLanguages = await promptYesNo('Generate images for all languages?');
        const selectedLanguages = useAllLanguages ?
            Object.keys(languages) :
            await promptLanguages(languages);

        console.log(`\nGenerating images for: ${selectedLanguages.join(', ')}`);

        const socialPoster = new SocialPoster(config);
        await socialPoster.init();

        for (const lang of selectedLanguages) {
            const langDir = path.join(lang, difficulty);
            const imagesDir = path.join(langDir, 'images');
            const langFilePath = path.join(langDir, `${problemName}.${languages[lang]}`);

            try {
                await fs.access(langFilePath);
                const langFileContent = await fs.readFile(langFilePath, 'utf-8');
                await fs.mkdir(imagesDir, { recursive: true });

                const options: RaysoOptions = {
                    code: langFileContent,
                    language: lang,
                    title: `${problemName} (${lang})`,
                    theme: 'candy',
                    darkMode: true,
                    padding: 32
                };

                const imageData = await generateCodeImage(options);
                const imagePath = path.join(imagesDir, `${problemName}_${lang}.png`);
                await fs.writeFile(imagePath, imageData);
                console.log(`Generated image: ${imagePath}`);

                const postText = `LeetCode ${problemName} solution in ${lang}\n#leetcode #${lang} #programming`;
                await socialPoster.postToAll({
                    text: postText,
                    imagePath,
                    language: lang,
                    problemName
                });

            } catch (error) {
                console.error(`Failed to process ${lang}:`, error);
            }
        }
    } catch (error) {
        if (error instanceof Error && 'code' in error && error.code === 'ENOENT') {
            console.error(`File not found: ${filePath}`);
        } else {
            console.error(`Error processing file:`, error);
        }
    }
}

const languages: Record<string, string> = {
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

async function findFile(problemId: string): Promise<string | null> {
    const diff = problems[problemId as keyof typeof problems];
    if (!diff) {
        console.error(`No difficulty found for problem ID: ${problemId}`);
        return null;
    }

    console.log({ problemId, diff });

    const pythonDir = path.join('python', diff);
    try {
        const files = await fs.readdir(pythonDir);
        const targetFile = files.find(file => file.startsWith(`${problemId}-`));

        if (!targetFile) {
            console.error(`No file found starting with ID: ${problemId}`);
            return null;
        }

        const problemName = path.parse(targetFile).name;
        console.log(`Found problem: ${problemName}`);

        for (const [lang, ext] of Object.entries(languages)) {
            const filePath = path.join(lang, diff, `${problemName}.${ext}`);
            try {
                await fs.access(filePath);
                return filePath;
            } catch { }
        }
    } catch (error) {
        console.error(`Error searching for problem: ${error}`);
    }

    return null;
}

async function main() {
    const problemName = Bun.argv[2];

    if (!problemName) {
        console.error('Please provide a problem name');
        console.error('Example: bun post.ts 2692-take-gifts-from-the-richest-pile');
        process.exit(1);
    }

    const filePath = await findFile(problemName);
    if (!filePath) {
        console.error(`Could not find problem: ${problemName}`);
        process.exit(1);
    }

    await processCodeFile(filePath, languages);
}

if (require.main === module) {
    main().catch(console.error);
}

export { processCodeFile, languages };

