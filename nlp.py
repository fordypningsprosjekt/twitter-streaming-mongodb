import json
from pprint import pprint

data = []
with open('tweets2.json') as f:
    for line in f:
        data.append(json.loads(line))

for json in data: 
	print json["text"]