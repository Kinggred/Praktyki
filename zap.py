import json
import requests as rq

r = rq.get('https://raw.githubusercontent.com/Kinggred/Praktyki/main/text.txt')

print(r.content)