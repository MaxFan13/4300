import time
import pandas as pd
from twitter_mysql import TwitterAPI

def load_follows(filename):
    tw = TwitterAPI("root", "BillyBobJoe", "HW", "localhost")

    df = pd.read_csv(filename)

    start = time.time()
    count = 0

    for _, row in df.iterrows():
        follower = int(row["FOLLOWS_ID"])
        followee = int(row["USER_ID"])

        tw.follow(follower, followee)
        count += 1

    end = time.time()

    print(f"Inserted {count} follow relationships")
    print(f"Total time: {(end - start):} seconds")
    print(f"Follows per second: {count / (end - start):}")

if __name__ == "__main__":
    load_follows("follows.csv")