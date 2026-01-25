
CREATE DATABASE IF NOT EXISTS HW;

USE HW;

DROP TABLE IF EXISTS TWEET;
DROP TABLE IF EXISTS FOLLOWS;

CREATE TABLE TWEET (
    tweet_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    tweet_ts DATETIME DEFAULT CURRENT_TIMESTAMP,
    tweet_text VARCHAR(140) NOT NULL
);

CREATE TABLE FOLLOWS(
    follower_id INT,
    followee_id INT,
    PRIMARY KEY (follower_id, followee_id)
);

CREATE INDEX tweet_user ON TWEET(user_id);
CREATE INDEX tweet_timestamp ON TWEET(tweet_ts DESC); -- Index for timestamp
CREATE INDEX tweet_user_ts ON TWEET(user_id, tweet_ts DESC); -- Indexes tweets by user and time
CREATE INDEX follows_followee ON FOLLOWS(followee_id, follower_id);
