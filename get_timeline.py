import random
import time
from twitter_mysql import TwitterDB


def get_random_user_ids(db):
    """
    Get all distinct users who follow someone.
    We only pick users who actually HAVE a home timeline.
    """
    query = """
    SELECT DISTINCT follower_id
    FROM FOLLOWS
    """
    df = db.db.select(query)
    return df["follower_id"].tolist()


def benchmark_home_timelines(iterations=100_000):
    tw = TwitterDB()

    users = get_random_user_ids(tw)
    if not users:
        raise RuntimeError("No users with follows found.")

    start = time.time()

    for _ in range(iterations):
        user_id = random.choice(users)
        tw.get_timeline(user_id)

    end = time.time()
    elapsed = end - start

    print(f"Timeline refreshes: {iterations}")
    print(f"Total time: {elapsed:.2f} seconds")
    print(f"Timelines per second: {iterations / elapsed:.2f}")


if __name__ == "__main__":
    benchmark_home_timelines()
