import sys

import twitter

import shaney

def get_tweet(text):
    for tweet in shaney.generate(text, 10000):
        if len(tweet) <= 140:
            return tweet


if __name__ == '__main__':
    uid = sys.argv[1]
    pwd = sys.argv[2]
    source_path = sys.argv[3]

    source = file(source_path)
    api = twitter.Api(uid, pwd)
    tweet = get_tweet(source.read())
    api.PostUpdate(tweet)
