import time
import pandas as pd
from twitter_mysql import TwitterAPI

def post_tweets(filename):
    tw = TwitterAPI("root", "BillyBobJoe", "HW", "localhost")

    df = pd.read_csv(filename)

    start = time.time()
    count = 0

    for _, row in df.iterrows(): # Iterating through the data and posting the tweet
        user_id = int(row["USER_ID"])
        tweet_text = row["TWEET_TEXT"]

        tw.postTweet(user_id, tweet_text)
        count += 1

    end = time.time()

    print(f"Posted {count} tweets")
    print(f"Total time: {end - start:} seconds")
    print(f"Tweets per second: {count / (end - start):}")

if __name__ == "__main__":
    post_tweets("tweet.csv")