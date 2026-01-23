--CREATE DATABASE data;

USE HW;

DROP TABLE IF EXISTS TWEET;
DROP TABLE IF EXISTS FOLLOWS;

CREATE TABLE TWEET (
    tweet_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    tweet_ts DATETIME NOT NULL,
    tweet_text VARCHAR(140) NOT NULL
);

CREATE TABLE FOLLOWS(
    follower_id INT,
    followee_id INT,
    PRIMARY KEY (follower_id, followee_id)
)

CREATE INDEX idx_tweet_user_id ON TWEET(user_id);

-- For queries filtering by timestamp (e.g., recent tweets)
CREATE INDEX idx_tweet_timestamp ON TWEET(tweet_ts DESC);

-- Composite index for user's tweets ordered by time
CREATE INDEX idx_tweet_user_ts ON TWEET(user_id, tweet_ts DESC);

-- Index on FOLLOWS table
-- For queries finding who a user follows (already covered by PK)
-- For queries finding followers of a user (reverse lookup)
CREATE INDEX idx_follows_followee ON FOLLOWS(followee_id, follower_id);