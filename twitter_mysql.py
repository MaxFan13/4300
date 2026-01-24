from datetime import datetime
from db_utils import DBUtils


class TwitterAPI:
    def __init__(self, user, password, database, host="localhost"):
        self.dbu = DBUtils(user, password, database, host)

    def postTweet(self, user_id, tweet_text):
        query = """
        INSERT INTO TWEET (user_id, tweet_ts, tweet_text)
        VALUES (%s, %s, %s)
        """
        self.dbu.write(query, (user_id, datetime.now(), tweet_text))

    def getUserTweets(self, user_id):
        query = """
        SELECT tweet_id, user_id, tweet_ts, tweet_text
        FROM TWEET
        WHERE user_id = %s
        ORDER BY tweet_ts DESC
        """
        return self.dbu.select(query, (user_id,))

    def getAllTweets(self):
        query = """
        SELECT tweet_id, user_id, tweet_ts, tweet_text
        FROM TWEET
        ORDER BY tweet_ts DESC
        """
        return self.dbu.select(query)

    def follow(self, follower_id, followee_id):
        if follower_id == followee_id:
            return

        query = """
        INSERT IGNORE INTO FOLLOWS (follower_id, followee_id)
        VALUES (%s, %s)
        """
        self.dbu.write(query, (follower_id, followee_id))

    def unfollow(self, follower_id, followee_id):
        query = """
        DELETE FROM FOLLOWS
        WHERE follower_id = %s AND followee_id = %s
        """
        self.dbu.write(query, (follower_id, followee_id))

    def getFollowers(self, user_id):
        query = """
        SELECT follower_id
        FROM FOLLOWS
        WHERE followee_id = %s
        ORDER BY follower_id
        """
        return self.dbu.select(query, (user_id,))

    def getFollowees(self, user_id):
        query = """
        SELECT followee_id
        FROM FOLLOWS
        WHERE follower_id = %s
        ORDER BY followee_id
        """
        return self.dbu.select(query, (user_id,))

    def get_timeline(self, user_id):
        query = """
        SELECT t.tweet_id, t.user_id, t.tweet_ts, t.tweet_text
        FROM TWEET t
        WHERE t.user_id = %s
           OR t.user_id IN (
                SELECT followee_id
                FROM FOLLOWS
                WHERE follower_id = %s
           )
        ORDER BY t.tweet_ts DESC
        LIMIT 10
        """
        return self.dbu.select(query, (user_id, user_id))
