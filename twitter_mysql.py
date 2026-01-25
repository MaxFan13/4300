from datetime import datetime
from db_utils import DBUtils
from twitter_objects import Tweet, User


class TwitterAPI:
    def __init__(self, user, password, database, host="localhost"):
        self.dbu = DBUtils(user, password, database, host)

    def close(self):
        """Close underlying DB connection"""
        self.dbu.close()

    def postTweet(self, user_id, tweet_text):
        """ Posts a tweet for a given user """
        sql = """
        INSERT INTO TWEET (user_id, tweet_ts, tweet_text)
        VALUES (%s, %s, %s)
        """
        self.dbu.insert_one(sql, (user_id, datetime.now(), tweet_text))

    def getUserTweets(self, user_id):
        """ Gets all tweets for a given user """
        query = f"""
        SELECT tweet_id, user_id, tweet_ts, tweet_text
        FROM TWEET
        WHERE user_id = {int(user_id)}
        ORDER BY tweet_ts DESC
        """
        df = self.dbu.execute(query)
        
        tweets = []
        for _, row in df.iterrows():
            tweet = Tweet(row['tweet_id'], row['user_id'], row['tweet_ts'], row['tweet_text'])
            tweets.append(tweet)
        return tweets

    def getAllTweets(self):
        """ Gets all tweets in the database """
        query = """
        SELECT tweet_id, user_id, tweet_ts, tweet_text
        FROM TWEET
        ORDER BY tweet_ts DESC
        """
        df = self.dbu.execute(query)
        
        tweets = []
        for _, row in df.iterrows():
            tweet = Tweet(row['tweet_id'], row['user_id'], row['tweet_ts'], row['tweet_text'])
            tweets.append(tweet)
        return tweets

    def follow(self, follower_id, followee_id):
        """ Follows a user """
        if follower_id == followee_id:
            return

        sql = """
        INSERT INTO FOLLOWS (follower_id, followee_id)
        VALUES (%s, %s)
        """
        self.dbu.insert_one(sql, (follower_id, followee_id))

    def unfollow(self, follower_id, followee_id):
        """ Unfollows a user."""
        sql = """
        DELETE FROM FOLLOWS
        WHERE follower_id = %s AND followee_id = %s
        """
        self.dbu.insert_one(sql, (follower_id, followee_id))

    def getFollowers(self, user_id):
        """ Gets all followers for a given user."""
        query = f"""
        SELECT follower_id, followee_id
        FROM FOLLOWS
        WHERE followee_id = {int(user_id)}
        ORDER BY follower_id
        """
        df = self.dbu.execute(query)
        
        users = []
        for _, row in df.iterrows():
            user = User(row['follower_id'], row['followee_id'])
            users.append(user)
        return users

    def getFollowees(self, user_id):
        """ Gets all users that a given user is following."""
        query = f"""
        SELECT follower_id, followee_id
        FROM FOLLOWS
        WHERE follower_id = {int(user_id)}
        ORDER BY followee_id
        """
        df = self.dbu.execute(query)
        
        users = []
        for _, row in df.iterrows():
            user = User(row['follower_id'], row['followee_id'])
            users.append(user)
        return users

    def get_timeline(self, user_id):
        """ Gets the 10 most recent tweets for a user's home timeline."""
        query = f"""
        SELECT t.tweet_id, t.user_id, t.tweet_ts, t.tweet_text
        FROM TWEET t
        WHERE t.user_id = {int(user_id)}
           OR t.user_id IN (
                SELECT followee_id
                FROM FOLLOWS
                WHERE follower_id = {int(user_id)}
           )
        ORDER BY t.tweet_ts DESC
        LIMIT 10
        """
        df = self.dbu.execute(query)
        
        tweets = []
        for _, row in df.iterrows():
            tweet = Tweet(row['tweet_id'], row['user_id'], row['tweet_ts'], row['tweet_text'])
            tweets.append(tweet)
        return tweets