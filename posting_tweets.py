import csv
import time
from twitter_mysql import TwitterDB

def post_tweets_from_csv(filename):
    tw = TwitterDB()

    start = time.time()
    count = 0

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for user_id, tweet_text in reader:
            tw.post_tweet(int(user_id), tweet_text)
            count += 1

    end = time.time()
    elapsed = end - start

    print(f"Inserted {count} tweets")
    print(f"Total time: {elapsed:.2f} seconds")
    print(f"Tweets per second: {count / elapsed:.2f}")

if __name__ == "__main__":
    post_tweets_from_csv("tweets.csv")
