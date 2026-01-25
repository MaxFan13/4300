class Tweet:
    def __init__(self, tweet_id, user_id, tweet_ts, tweet_text):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.tweet_ts = tweet_ts
        self.tweet_text = tweet_text

class User:
    def __init__(self, follower_id, followee_id):
        self.follower_id = follower_id
        self.followee_id = followee_id