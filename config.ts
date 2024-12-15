export const config = {
    twitter: {
        apiKey: process.env.TWITTER_API_KEY,
        apiSecret: process.env.TWITTER_API_SECRET,
        accessToken: process.env.TWITTER_ACCESS_TOKEN,
        accessTokenSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET
    },
    bluesky: {
        handle: process.env.BLUESKY_HANDLE,
        password: process.env.BLUESKY_PASSWORD
    },
    linkedin: {
        accessToken: process.env.LINKEDIN_ACCESS_TOKEN,
        userId: process.env.LINKEDIN_USER_ID
    }
};
