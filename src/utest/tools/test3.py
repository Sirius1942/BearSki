import json
fo = open("h13.json", "r+",encoding='utf8')
a=fo.read()
print(type(a))
jstr=json.loads(a)
