import json 

f = open('../data/data.json')
data = json.load(f)

for tweet in data[:3]:
    print(tweet["text"])

f.close()