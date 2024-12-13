(async () => {
  const fs: typeof import('fs').promises = require('fs').promises;
  const path = require('path');

  const dir = path.join(__dirname, 'python');
  const folders = await fs.readdir(dir);
  const problems: Record<string, string> = {};

  for (const folder of folders) {
    const files = await fs.readdir(path.join(dir, folder));
    for (const file of files) {
      const id = Number(file.split('-')[0]);
      problems[id] = folder;
    }
  }

  console.log(problems);
  await fs.writeFile(
    'constant.ts', 
    `export const problems = ${JSON.stringify(problems, null, 2)}`, 
    'utf-8'
  );
})();