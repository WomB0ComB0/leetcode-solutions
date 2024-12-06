import axios from 'axios';
import { promises as fs } from 'fs';
import path from 'path';

async function fetchProblems() {
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

async function sortProblemsByDifficulty(problems: any[]) {
  const difficultyOrder = ['Easy', 'Medium', 'Hard'];
  problems.sort((a, b) => difficultyOrder.indexOf(a.difficulty) - difficultyOrder.indexOf(b.difficulty));
}

async function createSortedFiles(problems: any[]) {
  const languages = {
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

async function main() {
  const problems = await fetchProblems();
  await sortProblemsByDifficulty(problems);
  await createSortedFiles(problems);
}

class Problems {
  static async run() {
    await main();
  }
}

if (require.main === module) {
  Problems.run().catch(console.error);
}

export default Problems;
