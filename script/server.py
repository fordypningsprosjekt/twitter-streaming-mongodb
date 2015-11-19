#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.escape
import tornado.ioloop
import tornado.web
import tornado
import collections
from urllib import urlopen
import json

class ApiHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header('Access-Control-Allow-Origin', '*')
		self.set_header('Content-Type', 'application/json')

		f = open("tweets3.json", "r")

		lines = f.readlines()

		tweets = []
		api = {}

		for i in range (0, len(lines)):
			json_line = json.loads(lines[i])

			temp = {}
			temp["id"] = json_line["id"]
			temp["text"] = json_line["text"]
			temp["index"] = i
			temp["positive"] = 0
			temp["neutral"] = 0
			temp["negative"] = 0
			temp["voted_by"] = []

			tweets.append(temp)

		api["tweets"] = tweets

		self.write(json.dumps(api, indent=4, ensure_ascii=False))

application = tornado.web.Application([
    (r"/", ApiHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
