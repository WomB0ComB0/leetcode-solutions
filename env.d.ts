export declare global {
  namespace NodeJS {
    interface ProcessEnv {
      TWITTER_API_KEY: string;
      TWITTER_API_SECRET: string;
      TWITTER_ACCESS_TOKEN: string;
      TWITTER_ACCESS_TOKEN_SECRET: string;
      BLUESKY_HANDLE: string;
      BLUESKY_PASSWORD: string;
      LINKEDIN_ACCESS_TOKEN: string;
      LINKEDIN_USER_ID: string;
    }
  }
}