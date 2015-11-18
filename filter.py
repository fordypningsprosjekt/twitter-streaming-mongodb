# json-objects with only id and text

import json
import re

file_ = open("tweets3.json", "a")
tweets = []

class StdOutListener(StreamListener):

    def on_data(self, data):
        if len(tweets)>10000:
            return False

        tweet = json.loads(data)

        if "created_at" in tweet and tweet["lang"]=="en" and (".@" not in tweet["text"]) and not (tweet["in_reply_to_status_id"] or tweet["entities"]["urls"] or ("retweeted_status" in tweet)):
            if not "media" in tweet["entities"]:
                tweets.append(json.loads(data))
                file_.write(data)

        return True

    def on_error(self, status):
        print status

