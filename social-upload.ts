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
            console.log(`Starting image upload for ${platform}...`);
            const imageData = await this.readImage(imagePath);
            console.log(`Successfully read image from ${imagePath}`);

            const result = platform === 'twitter'
                ? await this.handleTwitterUpload(imageData)
                : await this.handleLinkedInUpload(imageData);

            console.log(`Successfully uploaded image to ${platform}`);
            return result;
        } catch (error) {
            console.error(`${platform} upload failed:`, error);
            throw new Error(`${platform} upload failed: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    private async readImage(path: string): Promise<Buffer> {
        try {
            console.log(`Reading image from ${path}...`);
            const buffer = await fs.readFile(path);
            console.log(`Successfully read image (${buffer.length} bytes)`);
            return buffer;
        } catch (error) {
            console.error('Failed to read image:', error);
            throw new Error(`Failed to read image: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    private async makeRequest(
        platform: Platform,
        endpoint: string,
        options: { method?: string; body?: any; headers?: Record<string, string> } = {}
    ): Promise<Response> {
        const { url, headers } = this.endpoints[platform];
        const fullUrl = `${url}${endpoint}`;
        console.log(`Making ${options.method || 'POST'} request to ${fullUrl}`);

        const response = await fetch(fullUrl, {
            method: options.method || 'POST',
            headers: {
                Authorization: `Bearer ${this.config[platform].accessToken}`,
                ...headers,
                ...options.headers
            },
            body: options.body
        });

        if (!response.ok) {
            console.error(`${platform} API error:`, response.statusText);
            throw new Error(`${platform} API error: ${response.statusText}`);
        }

        console.log(`Request to ${fullUrl} successful`);
        return response;
    }

    private async handleTwitterUpload(imageData: Buffer): Promise<string> {
        console.log('Starting Twitter upload process...');

        const initResponse = await this.makeRequest('twitter', '', {
            body: new URLSearchParams({
                command: 'INIT',
                total_bytes: imageData.length.toString(),
                media_type: 'image/png'
            })
        });

        const { media_id_string } = await initResponse.json();
        console.log(`Initialized Twitter upload with media_id: ${media_id_string}`);

        const formData = new FormData();
        formData.append('command', 'APPEND');
        formData.append('media_id', media_id_string);
        formData.append('media', imageData, { filename: 'image.png', contentType: 'image/png' });
        formData.append('segment_index', '0');

        console.log('Appending media data to Twitter...');
        await this.makeRequest('twitter', '', {
            body: formData,
            headers: { 'Content-Type': `multipart/form-data; boundary=${formData.getBoundary()}` }
        });

        console.log('Finalizing Twitter upload...');
        await this.makeRequest('twitter', '', {
            body: new URLSearchParams({
                command: 'FINALIZE',
                media_id: media_id_string
            })
        });

        console.log('Twitter upload completed successfully');
        return media_id_string;
    }

    private async handleLinkedInUpload(imageData: Buffer): Promise<string> {
        console.log('Starting LinkedIn upload process...');

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
        console.log('Received LinkedIn upload URL');

        console.log('Uploading media to LinkedIn...');
        await fetch(uploadUrl, {
            method: 'PUT',
            headers: {
                Authorization: `Bearer ${this.config.linkedin.accessToken}`,
                'Content-Type': 'image/png'
            },
            body: imageData
        });

        console.log('LinkedIn upload completed successfully');
        return asset;
    }
}

export { SocialMediaImageUploader };
