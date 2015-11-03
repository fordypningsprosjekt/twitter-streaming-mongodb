#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import *
import json

file_ = open("tweets.json", "a")
tweets = []

class StdOutListener(StreamListener):

    def on_data(self, data):
        if len(tweets)>99:
            return False

        tweet = json.loads(data)

        if "created_at" in tweet and tweet["lang"]=="en" and not tweet["in_reply_to_status_id"]:
            tweets.append(json.loads(data))
            file_.write(data)
            print json.loads(data)["text"]

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.sample()
