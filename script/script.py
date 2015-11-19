import json

f = open("tweets3.json", "r")
new_f = open("new_tweets.json", "w")

lines = f.readlines()

tweets = []

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

new_f.write(json.dumps(tweets))
