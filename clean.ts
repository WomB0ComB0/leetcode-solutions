import { promises as fs } from 'fs';
import path from 'path';

class FilenameCleaner {
  private static readonly PROGRAMMING_DIRECTORIES = [
    'python', 'typescript', 'javascript', 'java', 'cpp', 'c', 
    'csharp', 'dart', 'php', 'go', 'rust', 
    'ruby', 'swift', 'kotlin'
  ];

  private static toKebabCase(str: string): string {
    return str
      .replace(/([a-z])([A-Z])/g, '$1-$2')
      .replace(/\s+/g, '-')
      .replace(/[^a-zA-Z0-9-]/g, '')
      .toLowerCase();
  }

  private static toRoman(num: number): string {
    if (num <= 0) return '';
    const romanNumerals: [string, number][] = [
      ['M', 1000], ['CM', 900], ['D', 500], ['CD', 400],
      ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
      ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]
    ];

    return romanNumerals.reduce((result, [roman, value]) => {
      while (num >= value) {
        result += roman;
        num -= value;
      }
      return result;
    }, '');
  }

  static async cleanFilenames(directory: string): Promise<void> {
    try {
      const entries = await fs.readdir(directory, { withFileTypes: true });
      const seenNames = new Set<string>();

      for (const entry of entries) {
        if (!entry.isFile()) continue;

        const file = entry.name;
        const ext = path.extname(file);
        const baseName = path.basename(file, ext);
        const parts = baseName.split('.');
        const namePart = parts.slice(1).join('.'); 
        const kebabName = this.toKebabCase(namePart);

        const postfixMatch = kebabName.match(/-(\d+)$/);
        let finalName = kebabName;
        if (postfixMatch) {
          const number = parseInt(postfixMatch[1], 10);
          if (number > 0) {
            const roman = this.toRoman(number);
            finalName = kebabName.replace(/-\d+$/, `-${roman}`);
          }
        }

        let uniqueName = finalName;
        let counter = 1;
        while (seenNames.has(uniqueName) || await fs.access(path.join(directory, `${uniqueName}${ext}`)).then(() => true).catch(() => false)) {
          uniqueName = `${finalName}-duplicate-${counter}`;
          counter++;
        }
        seenNames.add(uniqueName);

        const oldFilePath = path.join(directory, file);
        const newFilePath = path.join(directory, `${uniqueName}${ext}`);

        await fs.rename(oldFilePath, newFilePath);
        console.log(`Renamed: ${file} → ${uniqueName}${ext}`);
      }
    } catch (error) {
      console.error(`Error processing directory ${directory}:`, error);
    }
  }

  static async run(baseDirectory: string = process.cwd()): Promise<void> {
    console.time('Filename Cleaning Duration');
    
    try {
      await Promise.all(
        this.PROGRAMMING_DIRECTORIES.map(async (dir) => {
          const fullPath = path.join(baseDirectory, dir);
          console.log(`Processing directory: ${dir}`);
          await this.cleanFilenames(fullPath);
        })
      );
    } catch (error) {
      console.error('Unexpected error in filename cleaning process:', error);
    } finally {
      console.timeEnd('Filename Cleaning Duration');
    }
  }
}

if (require.main === module) {
  FilenameCleaner.run().catch(console.error);
}

export default FilenameCleaner;