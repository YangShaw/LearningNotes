
import json

jsonlist = []
with open('http.log', 'r') as f:
    for line in f.readlines():
        jsonstr = json.loads(line)
        jsonlist.append(jsonstr)

with open('conncontent.txt', 'w') as f:
    for data in jsonlist:
        if(data["cat"]=="conn"):
            f.write(json.dumps(data)+"\n")

