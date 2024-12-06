import axios from 'axios';
import { promises as fs } from 'fs';
import path from 'path';

/**
 * Interface representing a LeetCode problem returned from the API
 * @interface
 */
interface LeetCodeProblem {
  /** The title of the problem */
  title: string;
  /** The difficulty level (Easy, Medium, Hard) */
  difficulty: string;
  /** The URL-friendly slug version of the title */
  titleSlug: string;
}

/**
 * Fetches the list of problems from LeetCode's GraphQL API
 * @returns {Promise<LeetCodeProblem[]>} Array of LeetCode problems with title, difficulty and slug
 * @throws {Error} If the API request fails
 */
async function fetchProblems(): Promise<LeetCodeProblem[]> {
  const url = 'https://leetcode.com/graphql';
  const query = {
    query: `
      query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
          categorySlug: $categorySlug
          limit: $limit
          skip: $skip
          filters: $filters
        ) {
          questions: data {
            title
            difficulty
            titleSlug
          }
        }
      }
    `,
    variables: {
      categorySlug: '',
      limit: 3374,
      skip: 0,
      filters: {},
    },
  };

  try {
    const response = await axios.post(url, query, {
      headers: {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      },
    });

    return response.data.data.problemsetQuestionList.questions;
  } catch (error) {
    console.error('Error fetching problems:', error);
    return [];
  }
}

/**
 * Sorts an array of LeetCode problems by difficulty level
 * @param {LeetCodeProblem[]} problems - Array of problems to sort
 * @returns {Promise<void>}
 */
async function sortProblemsByDifficulty(problems: LeetCodeProblem[]): Promise<void> {
  const difficultyOrder = ['Easy', 'Medium', 'Hard'];
  problems.sort((a, b) => difficultyOrder.indexOf(a.difficulty) - difficultyOrder.indexOf(b.difficulty));
}

/**
 * Interface mapping programming languages to their file extensions
 * @interface
 */
interface LanguageExtensions {
  [key: string]: string;
}

/**
 * Creates empty solution files for each problem across multiple programming languages
 * @param {LeetCodeProblem[]} problems - Array of problems to create files for
 * @returns {Promise<void>}
 * @throws {Error} If file operations fail
 */
async function createSortedFiles(problems: LeetCodeProblem[]): Promise<void> {
  const languages: LanguageExtensions = {
    python: 'py',
    typescript: 'ts',
    javascript: 'js',
    java: 'java',
    cpp: 'cpp',
    c: 'c',
    dart: 'dart',
    php: 'php',
    csharp: 'cs',
    go: 'go',
    rust: 'rs',
    ruby: 'rb',
    swift: 'swift',
    kotlin: 'kt',
  };

  for (const problem of problems) {
    const kebabTitle = problem.titleSlug;
    const difficulty = problem.difficulty.toLowerCase();

    for (const [language, extension] of Object.entries(languages)) {
      const dirPath = `${language}/${difficulty}`;
      const filePath = `${dirPath}/${kebabTitle}.${extension}`;

      try {
        await fs.access(filePath);
        console.log(`File already exists, skipping: ${filePath}`);
      } catch {
        await fs.mkdir(dirPath, { recursive: true });
        await fs.writeFile(filePath, '');
        console.log(`Created file: ${filePath}`);
      }
    }
  }
}

/**
 * Main execution function that orchestrates the problem fetching, sorting and file creation
 * @returns {Promise<void>}
 */
async function main(): Promise<void> {
  const problems = await fetchProblems();
  await sortProblemsByDifficulty(problems);
  await createSortedFiles(problems);
}

/**
 * Class that provides a static interface for running the problem processing pipeline
 */
class Problems {
  /**
   * Executes the main problem processing pipeline
   * @returns {Promise<void>}
   * @throws {Error} If any step in the pipeline fails
   */
  static async run(): Promise<void> {
    await main();
  }
}

if (require.main === module) {
  Problems.run().catch(console.error);
}

export default Problems;
