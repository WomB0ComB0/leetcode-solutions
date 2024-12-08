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

/**
 * Fetches the daily LeetCode challenge and creates solution files in multiple languages
 * @throws {Error} If the API request fails or file operations fail
 */
async function getDailyLeetcodeChallenge() {
  const url = 'https://leetcode.com/graphql';
  const query = {
    query: `
      query questionOfToday {
        activeDailyCodingChallengeQuestion {
          question {
            title
            difficulty
            topicTags {
              name
            }
          }
        }
      }
    `,
  };

  console.log('Fetching daily LeetCode challenge...');

  try {
    const response = await axios.post(url, query, {
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      },
    });

    const question = response.data.data.activeDailyCodingChallengeQuestion.question;
    const title = question.title;
    const difficulty = question.difficulty;
    const language = question.topicTags[0]?.name || 'unknown';

    console.log('Challenge details:');
    console.log(`Title: ${title}`);
    console.log(`Difficulty: ${difficulty}`);
    console.log(`Primary topic: ${language}`);

    const kebabTitle = await toKebabCase(title);

    /**
     * Mapping of programming languages to their file extensions
     * @type {Object.<string, string>}
     */
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

    for (const [key, value] of Object.entries(extensions)) {
      const dirPath = path.join(key, difficulty.toLowerCase());
      const filePath = path.join(dirPath, `${kebabTitle}.${value}`);

      try {
        await fs.access(filePath);
        existingFiles.push(filePath);
        console.log(`File already exists: ${filePath}`);
      } catch {
        await fs.mkdir(dirPath, { recursive: true });
        await fs.writeFile(filePath, '');
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

export default Daily;