import json as js
#import requests as rq

#r = rq.get('https://raw.githubusercontent.com/Kinggred/Praktyki/quiz/quiz/text.json')

f = open("praktyki/062021/maks_grupinski/repo/quiz/text.json", "rt")
quest = js.loads(f.read())


print(quest)