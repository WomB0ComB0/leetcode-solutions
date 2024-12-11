/**
 * @fileoverview Revises LeetCode solution filenames to include question IDs as prefixes, using concurrent operations
 */

import { promises as fs } from 'node:fs';
import path from 'node:path';
import axios from 'axios';

interface QuestionData {
  titleSlug: string;
  questionFrontendId: string;
  difficulty: string;
}

/**
 * Configuration for supported programming languages and their file extensions
 * @type {Object.<string, string>}
 */
const LANGUAGE_EXTENSIONS: { [key: string]: string } = {
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

const DIFFICULTIES = ['easy', 'medium', 'hard'];

// Rate limiting configuration
const MAX_CONCURRENT_REQUESTS = 5;
const REQUEST_DELAY = 500; // ms between requests

/**
 * Creates a delay between operations
 * @param {number} ms - Milliseconds to delay
 * @returns {Promise<void>}
 */
const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

/**
 * Fetches question data from LeetCode's GraphQL API with rate limiting
 * @param {string} titleSlug - The URL-friendly title of the question
 * @returns {Promise<QuestionData>} Question details including ID and difficulty
 */
async function fetchQuestionData(titleSlug: string): Promise<QuestionData> {
  const query = `
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        titleSlug
        difficulty
      }
    }
  `;

  try {
    const response = await axios.post('https://leetcode.com/graphql', 
      {
        query,
        variables: { titleSlug }
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
      }
    );

    await delay(REQUEST_DELAY);
    return response.data.data.question;
  } catch (error) {
    console.error(`API request failed for ${titleSlug}:`, error instanceof Error ? error.message : String(error));
    throw error;
  }
}

/**
 * Processes a single file
 * @param {string} file - Filename to process
 * @param {string} langDir - Language directory path
 * @param {string} difficulty - Difficulty level
 * @param {string} extension - File extension
 * @returns {Promise<void>}
 */
async function processFile(file: string, langDir: string, difficulty: string, extension: string) {
  const difficultyDir = path.join(langDir, difficulty);
  
  try {
    const titleSlug = file.replace(`.${extension}`, '');
    const questionData = await fetchQuestionData(titleSlug);
    
    const expectedDir = questionData.difficulty.toLowerCase();
    if (expectedDir !== difficulty) {
      const correctDir = path.join(langDir, expectedDir);
      await fs.mkdir(correctDir, { recursive: true });
    }

    const newFilename = `${questionData.questionFrontendId}-${titleSlug}.${extension}`;
    const sourcePath = path.join(difficultyDir, file);
    const targetPath = path.join(langDir, expectedDir, newFilename);
    
    await fs.rename(sourcePath, targetPath);
    
    console.log(`Renamed: ${file} -> ${newFilename}`);
    if (expectedDir !== difficulty) {
      console.log(`Moved from ${difficulty} to ${expectedDir}`);
    }
  } catch (error) {
    console.error(`Error processing ${file}:`, error instanceof Error ? error.message : String(error));
  }
}

/**
 * Processes files in a directory with concurrency control
 * @param {string} langDir - Language directory path
 * @param {string} difficulty - Difficulty level
 * @param {string} extension - File extension
 * @returns {Promise<void>}
 */
async function processDirectory(langDir: string, difficulty: string, extension: string) {
  const difficultyDir = path.join(langDir, difficulty);
  
  try {
    const files = await fs.readdir(difficultyDir);
    const relevantFiles = files.filter(file => 
      file.endsWith(`.${extension}`) && file !== 'revision.ts'
    );

    // Collect all file processing promises
    const fileProcessingPromises = relevantFiles.map(file => processFile(file, langDir, difficulty, extension));

    // Process files in chunks to control concurrency
    for (let i = 0; i < fileProcessingPromises.length; i += MAX_CONCURRENT_REQUESTS) {
      const chunk = fileProcessingPromises.slice(i, i + MAX_CONCURRENT_REQUESTS);
      await Promise.all(chunk);
    }
  } catch (error) {
    if (error instanceof Error && 'code' in error && error.code !== 'ENOENT') {
      console.error(`Error processing directory ${difficultyDir}:`, error.message);
    }
  }
}

/**
 * Main class to handle filename revision operations
 * @class
 */
class Revision {
  /**
   * Executes the filename revision process
   * @static
   * @async
   */
  static async run() {
    const currentDir = process.cwd();
    console.log('Starting filename revision process...');

    // Process languages concurrently
    const languageTasks = Object.entries(LANGUAGE_EXTENSIONS).map(
      async ([lang, ext]) => {
        const langDir = path.join(currentDir, lang);
        
        try {
          await fs.access(langDir);
          console.log(`Processing ${lang} solutions...`);
          
          // Process difficulties concurrently within each language
          await Promise.all(
            DIFFICULTIES.map(difficulty => 
              processDirectory(langDir, difficulty, ext)
            )
          );
        } catch (error) {
          if (error instanceof Error && 'code' in error && error.code !== 'ENOENT') {
            console.error(`Error processing ${lang} directory:`, error.message);
          }
        }
      }
    );

    await Promise.all(languageTasks);
    console.log('Filename revision process completed');
  }
}

// Execute if this is the main module
if (require.main === module) {
  Revision.run().catch(console.error);
}

export default Revision;