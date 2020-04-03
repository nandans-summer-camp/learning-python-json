import json

def load_tweets(path):
    with open(path) as f:
        return [json.loads(li) for li in f]
