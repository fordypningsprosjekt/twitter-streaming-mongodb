#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from keys import *
import json
import re

file_ = open("tweets3.json", "a")
tweets = []

class StdOutListener(StreamListener):

    def on_data(self, data):
        if len(tweets)>10000:
            return False

        tweet = json.loads(data)

        if "created_at" in tweet and tweet["lang"]=="en" and (".@" not in tweet["text"]) and not (tweet["in_reply_to_status_id"] or tweet["entities"]["urls"] or ("retweeted_status" in tweet)) and not "media" in tweet["entities"] and not "@" == tweet["text"][0] and tweet["text"] > 5:
            tweets.append(json.loads(data))
            file_.write(data)

        return True

    def on_error(self, status):
        print status

class twitterStats():
    file_.read

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.sample()
