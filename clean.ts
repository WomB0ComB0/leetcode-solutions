import { promises as fs } from 'fs';
import path from 'path';

class FilenameCleaner {
  private static readonly PROGRAMMING_DIRECTORIES = [
    'python', 'typescript', 'javascript', 'java', 'cpp', 'c', 
    'c#', 'c++', 'dart', 'php', 'csharp', 'go', 'rust', 
    'ruby', 'swift', 'kotlin'
  ];

  private static sanitizeFileName(fileName: string): string {
    // Handle LeetCode-style filenames like "1310.XORQueriesOfASubarray"
    const parts = fileName.split('.');
    if (parts.length > 1 && /^\d+$/.test(parts[0])) {
      return parts.slice(1).join('.');
    }
    return fileName;
  }

  private static toKebabCase(str: string): string {
    return str
      .replace(/([a-z])([A-Z])/g, '$1-$2')
      .replace(/\s+/g, '-')
      .replace(/[^a-zA-Z0-9-]/g, '')
      .toLowerCase();
  }

  static async cleanFilenames(directory: string): Promise<void> {
    try {
      const files = await fs.readdir(directory);
      const seenNames = new Set<string>();

      for (const file of files) {
        const ext = path.extname(file);
        const baseName = path.basename(file, ext);
        const sanitizedName = this.sanitizeFileName(baseName);
        const kebabName = this.toKebabCase(sanitizedName);

        let uniqueName = kebabName;
        let counter = 1;
        while (seenNames.has(uniqueName)) {
          uniqueName = `${kebabName}-${counter}`;
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