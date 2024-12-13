import fs from 'node:fs/promises';
import FormData from 'form-data';

type Platform = 'twitter' | 'linkedin';

interface SocialMediaConfig {
  accessToken: string;
  userId?: string;
}

interface SocialMediaUploadConfig {
  twitter: SocialMediaConfig;
  linkedin: SocialMediaConfig;
}

interface ApiEndpoint {
  url: string;
  headers: Record<string, string>;
}

class SocialMediaImageUploader {
  private readonly config: SocialMediaUploadConfig;
  private readonly endpoints: Record<Platform, ApiEndpoint> = {
    twitter: {
      url: 'https://upload.twitter.com/1.1/media/upload.json',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    },
    linkedin: {
      url: 'https://api.linkedin.com/v2',
      headers: { 'Content-Type': 'application/json' }
    }
  };

  constructor(config: SocialMediaUploadConfig) {
    this.config = config;
  }

  public async uploadImage(platform: Platform, imagePath: string): Promise<string> {
    try {
      const imageData = await this.readImage(imagePath);
      return platform === 'twitter' 
        ? await this.handleTwitterUpload(imageData)
        : await this.handleLinkedInUpload(imageData);
    } catch (error) {
      throw new Error(`${platform} upload failed: ${error instanceof Error ? error.message : String(error)}`);
    }
  }

  private async readImage(path: string): Promise<Buffer> {
    try {
      return await fs.readFile(path);
    } catch (error) {
      throw new Error(`Failed to read image: ${error instanceof Error ? error.message : String(error)}`);
    }
  }

  private async makeRequest(
    platform: Platform, 
    endpoint: string, 
    options: { method?: string; body?: any; headers?: Record<string, string> } = {}
  ): Promise<Response> {
    const { url, headers } = this.endpoints[platform];
    const response = await fetch(`${url}${endpoint}`, {
      method: options.method || 'POST',
      headers: {
        Authorization: `Bearer ${this.config[platform].accessToken}`,
        ...headers,
        ...options.headers
      },
      body: options.body
    });

    if (!response.ok) {
      throw new Error(`${platform} API error: ${response.statusText}`);
    }

    return response;
  }

  private async handleTwitterUpload(imageData: Buffer): Promise<string> {
    const initResponse = await this.makeRequest('twitter', '', {
      body: new URLSearchParams({
        command: 'INIT',
        total_bytes: imageData.length.toString(),
        media_type: 'image/png'
      })
    });

    const { media_id_string } = await initResponse.json();

    const formData = new FormData();
    formData.append('command', 'APPEND');
    formData.append('media_id', media_id_string);
    formData.append('media', imageData, { filename: 'image.png', contentType: 'image/png' });
    formData.append('segment_index', '0');

    await this.makeRequest('twitter', '', {
      body: formData,
      headers: { 'Content-Type': `multipart/form-data; boundary=${formData.getBoundary()}` }
    });

    await this.makeRequest('twitter', '', {
      body: new URLSearchParams({
        command: 'FINALIZE',
        media_id: media_id_string
      })
    });

    return media_id_string;
  }

  private async handleLinkedInUpload(imageData: Buffer): Promise<string> {
    const registerResponse = await this.makeRequest('linkedin', 'assets?action=registerUpload', {
      body: JSON.stringify({
        registerUploadRequest: {
          recipes: ['urn:li:digitalmediaRecipe:feedshare-image'],
          owner: `urn:li:person:${this.config.linkedin.userId}`,
          serviceRelationships: [{
            relationshipType: 'OWNER',
            identifier: 'urn:li:userGeneratedContent'
          }]
        }
      })
    });

    const { value: { uploadMechanism, asset } } = await registerResponse.json();
    const { uploadUrl } = uploadMechanism['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'];

    await fetch(uploadUrl, {
      method: 'PUT',
      headers: {
        Authorization: `Bearer ${this.config.linkedin.accessToken}`,
        'Content-Type': 'image/png'
      },
      body: imageData
    });

    return asset;
  }
}

export { SocialMediaImageUploader };