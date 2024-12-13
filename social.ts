import { AtpAgent, BskyAgent, RichText } from '@atproto/api';
import { promises as fs } from 'fs';
import { SocialMediaImageUploader } from './social-upload';


interface SocialConfig {
  twitter?: {
    apiKey: string;
    apiSecret: string;
    accessToken: string;
    accessTokenSecret: string;
  };
  bluesky?: {
    handle: string;
    password: string;
  };
  linkedin?: {
    accessToken: string;
    userId: string;
  };
}

interface PostOptions {
  text: string;
  imagePath?: string;
  language: string;
  problemName: string;
}

export class SocialPoster {
  private config: SocialConfig;
  private clients: {
    bluesky?: BskyAgent;
    twitter?: any;
    linkedin?: any;
  } = {};
  private imageUploader: SocialMediaImageUploader;

  constructor(config: SocialConfig) {
    this.config = config;
    this.imageUploader = new SocialMediaImageUploader({
      twitter: {
        accessToken: config.twitter?.accessToken || '',
      },
      linkedin: {
        accessToken: config.linkedin?.accessToken || '',
        userId: config.linkedin?.userId || '',
      }
    });
  }

  async init() {
    const initPromises = [];

    if (this.config.bluesky) {
      initPromises.push(this.initBluesky());
    }

    if (this.config.twitter) {
      initPromises.push(this.initTwitter());
    }

    if (this.config.linkedin) {
      initPromises.push(this.initLinkedIn());
    }

    await Promise.allSettled(initPromises);
  }

  private async initBluesky() {
    if (!this.config.bluesky) return;

    try {
      const agent = new BskyAgent({ service: 'https://bsky.social' });
      await agent.login({
        identifier: this.config.bluesky.handle,
        password: this.config.bluesky.password
      });
      this.clients.bluesky = agent;
    } catch (error) {
      console.error('Bluesky initialization failed:', error);
    }
  }

  private async initTwitter() {
    if (!this.config.twitter) return;

    try {
      this.clients.twitter = {
        apiKey: this.config.twitter.apiKey,
        accessToken: this.config.twitter.accessToken
      };
    } catch (error) {
      console.error('Twitter initialization failed:', error);
    }
  }

  private async initLinkedIn() {
    if (!this.config.linkedin) return;

    try {
      this.clients.linkedin = {
        accessToken: this.config.linkedin.accessToken,
        userId: this.config.linkedin.userId
      };
    } catch (error) {
      console.error('LinkedIn initialization failed:', error);
    }
  }

  async postToAll(options: PostOptions) {
    const postPromises = Object.entries(this.clients)
      .filter(([_, client]) => client)
      .map(([platform, _]) => {
        switch (platform) {
          case 'bluesky':
            return this.postToBluesky(options);
          case 'twitter':
            return this.postToTwitter(options);
          case 'linkedin':
            return this.postToLinkedIn(options);
          default:
            return Promise.resolve();
        }
      });

    const results = await Promise.allSettled(postPromises);
    
    results.forEach((result, _) => {
      if (result.status === 'rejected') {
        console.error(`Post to platform failed:`, result.reason);
      }
    });
  }

  private async postToTwitter(options: PostOptions) {
    if (!this.clients.twitter) return;

    try {
      const data: any = { text: options.text };

      if (options.imagePath) {
        const mediaId = await this.imageUploader.uploadImage('twitter', options.imagePath);
        if (mediaId) {
          data.media = { media_ids: [mediaId] };
        }
      }

      const response = await fetch('https://api.twitter.com/2/tweets', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.clients.twitter.accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        throw new Error(`Twitter API error: ${response.statusText}`);
      }

      console.log(`Posted to Twitter: ${options.problemName} (${options.language})`);
    } catch (error) {
      console.error('Twitter post failed:', error);
      throw error;
    }
  }

  private async postToBluesky(options: PostOptions) {
    if (!this.clients.bluesky) return;

    try {
      const rt = new RichText({ text: options.text });
      await rt.detectFacets(this.clients.bluesky);

      let images;
      if (options.imagePath) {
        const imageData = await fs.readFile(options.imagePath);
        const response = await this.clients.bluesky.uploadBlob(new Uint8Array(imageData), {
          encoding: 'image/png'
        });

        images = [{
          image: response.data.blob,
          alt: `Code solution for ${options.problemName} in ${options.language}`
        }];
      }

      await this.clients.bluesky.post({
        text: rt.text,
        facets: rt.facets,
        embed: images ? {
          $type: 'app.bsky.embed.images',
          images
        } : undefined
      });

      console.log(`Posted to Bluesky: ${options.problemName} (${options.language})`);
    } catch (error) {
      console.error('Bluesky post failed:', error);
      throw error;
    }
  }

  private async postToLinkedIn(options: PostOptions) {
    if (!this.clients.linkedin) return;

    try {
      let asset = '';
      if (options.imagePath) {
        asset = await this.imageUploader.uploadImage('linkedin', options.imagePath) || '';
      }

      const data = {
        author: `urn:li:person:${this.config.linkedin?.userId}`,
        lifecycleState: 'PUBLISHED',
        specificContent: {
          'com.linkedin.ugc.ShareContent': {
            shareCommentary: {
              text: options.text
            },
            shareMediaCategory: asset ? 'IMAGE' : 'NONE',
            ...(asset && {
              media: [{
                status: 'READY',
                media: asset,
                title: {
                  text: `${options.problemName} (${options.language})`
                }
              }]
            })
          }
        },
        visibility: {
          'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
        }
      };

      const response = await fetch('https://api.linkedin.com/v2/ugcPosts', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${this.clients.linkedin.accessToken}`,
          'Content-Type': 'application/json',
          'X-Restli-Protocol-Version': '2.0.0'
        },
        body: JSON.stringify(data)
      });

      if (!response.ok) {
        throw new Error(`LinkedIn API error: ${response.statusText}`);
      }

      console.log(`Posted to LinkedIn: ${options.problemName} (${options.language})`);
    } catch (error) {
      console.error('LinkedIn post failed:', error);
      throw error;
    }
  }
}