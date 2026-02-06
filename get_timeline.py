import random
import time
from twitter_mysql import TwitterAPI


def getHomeTimeline(refreshes=100_000):
    tw = TwitterAPI("root", "BillyBobJoe", "HW", "localhost")

    users = tw.get_users()

    start = time.time()

    for _ in range(refreshes): 
        user_id = random.choice(users) # Randomly choose a user
        tweets = tw.get_timeline(user_id) # Get the user's timeline
        
        for tweet in tweets:
            _ = tweet.tweet_id
            _ = tweet.user_id
            _ = tweet.tweet_ts
            _ = tweet.tweet_text

    end = time.time()
    elapsed = end - start

    print(f"Timeline refreshes: {refreshes}")
    print(f"Total time: {elapsed:} seconds")
    print(f"Timelines per second: {refreshes / elapsed:}")


if __name__ == "__main__":
    getHomeTimeline()