import json
with open("/Users/xiaogo627301968qq.com/exercise1/mensen.json", mode="r", encoding="utf-8") as fi:
    mydict = json.load(fi)
print(mydict)
print("Sheila is ",mydict["Sheila"])

