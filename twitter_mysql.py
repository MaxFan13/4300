

from follows import Follows

class TwitterAPI:

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = Follows(user, password, database, host)

    def tweet(self, pat):
        sql = "INSERT INTO TWEET (tweet_id, user_id, tweet_ts, tweet_text) VALUES (%s, %s, %s, %s) "
        val = (pat.tweet_id, pat.user_id, pat.tweet_ts, pat.tweet_text)
        self.dbu.insert_one(sql, val)

    def follows(self, user_id):
        sql = """
                select user_id, follows_id
                from follows
                where user_id = %s
        """
        val = (user_id,)
        df = self.dbu.execute(sql, val)
        return df

