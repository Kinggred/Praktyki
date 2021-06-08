import json as js
import requests as rq

r = rq.get('https://raw.githubusercontent.com/Kinggred/Praktyki/quiz/quiz/text.txt')

print(r.content)