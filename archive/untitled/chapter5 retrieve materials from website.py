from urllib.request import Request, urlopen
import json


# req = Request('https://www.google.com/search?tbm=bks&sxsrf=ACYBGNQ2aRfwlotB8bDq6ly1412OI3D-Dw:1582034734324&tbm=bks&q=inauthor:%22Niklas+Luhmann%22&sa=X&ved=0ahUKEwiw__HSotvnAhXUwAIHHYpuDNkQ9AgIOjAB&biw=864&bih=650&dpr=1', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
#
# niklas = json.loads(webpage.decode('utf-8'))
# for boek in niklas['items']:
#     print(boek['volumeInfo']['authors'],":",boek['volumeInfo']['title'])

luhmann=urlopen('https://www.googleapis.com/books/v1/volumes?q=inauthor:"Niklas+Luhmann"').read()
niklas=json.loads(luhmann.decode("utf-8"))

for boek in niklas["items"]:
    print (boek["volumeInfo"]["authors"],": ",boek["volumeInfo"]["title"])

pagecount = []
for boek in niklas["items"]:
    pagecount.append(int(boek["volumeInfo"]["pageCount"]))
print("the average length of a book by Luhmann is",sum(pagecount)/len(pagecount),"pages")

totalpages = 0
numberofbooks = 0
for boek in niklas["items"]:
    pages=int(boek["volumeInfo"]["pageCount"])
    print(pages)
    totalpages=totalpages+pages
    numberofbooks=numberofbooks+1
print("The average length of a book by Luhmann is",totalpages/numberofbooks,"pages")
