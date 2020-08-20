# import csv ##want to load an external module
import json
# name = []
# age = []
# height = []
#
# with open('/Users/xiaogo627301968qq.com/exercise1/mensen.csv',encoding='utf-8',mode='r',newline='') as csvfile: ## we want to open a file and assigns a name to that so-called file object
#     reader = csv.reader(csvfile,delimiter=',')
#     for row in reader: ##把每行中的name,age,height分别读取到name,age和height的list中
#         name.append(row[0])
#         age.append(row[1])
#         height.append(row[2])
# print("Done!")
#
# print(name)
# print(age)
# print(height)
#
# output = zip(age, height, name) ##zip 将每个命令粘合在一起
#
# with open("test.csv",mode="w", encoding="utf-8")as fo: ##将所有内容存储到新文件中
#     writer=csv.writer(fo)
#     writer.writerows(output)
#
##打开json文件
# with open("/Users/xiaogo627301968qq.com/exercise1/mensen.json",mode='r',encoding='utf-8') as fi:
#     mydict = json.load(fi)
# print(mydict)
# print("Sheilar is ",mydict["Sheilar"]) ##这句如何理解
#
#将文字输入为json文件
# ages = {'Sheilar':28, 'Anne':23, 'John':22,"Bas":25, "Mark":26}
# with open("/Users/xiaogo627301968qq.com/exercise1/mensen.json", mode='w',encoding='utf-8')as fo:
#     json.dump(ages,fo)
#
##Getting to know API
from urllib.request import urlopen ##import a module to download data from URL, a module to read JSON data
from pprint import pprint ## import a module that prints json objects in a more readable way

antwoord = urlopen('https://www.googleapis.com/books/v1/volumes?q=inauthor:"Niklas+Luhmann"').read()
data = json.loads(antwoord.decode("utf-8")) ##transforms the bunch of bytes into a string. json.loads()-a JSON string can be directly translated to a Python dict
pprint(data)
###json.load()takes a file object(which we don't have here), json.loads () a string

pprint(data["items"][1]["volumeInfo"]['language'])


