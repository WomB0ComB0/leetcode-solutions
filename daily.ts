import { promises as fs } from 'fs';
import axios from 'axios';

async function toKebabCase(str: string): Promise<string> {
  return str.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

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

    const extensions: { [key: string]: string } = {
      c: 'c',
      java: 'java',
      go: 'go',
      dart: 'dart',
      javascript: 'js',
      'c++': 'cpp',
      'c#': 'cs',
      typescript: 'ts',
      php: 'php',
      rust: 'rs',
      python: 'py',
      kotlin: 'kt',
    };

    for (const [key, value] of Object.entries(extensions)) {
      const dirPath = `${key}/${difficulty.toLowerCase()}`;
      const filePath = `${dirPath}/${kebabTitle}.${value}`;

      console.log(`Creating directory: ${dirPath}`);
      await fs.mkdir(dirPath, { recursive: true });

      console.log(`Creating file: ${filePath}`);
      await fs.writeFile(filePath, '');
    }

    console.log(`Successfully created challenge files`);
  } catch (error) {
    console.error('Error: Failed to fetch daily LeetCode challenge', error);
  }
}

if (require.main === module) {
  getDailyLeetcodeChallenge();
}
