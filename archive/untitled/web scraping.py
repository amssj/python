import requests
import cssselect
from lxml import html

baseurl = "https://www.politifact.com/factchecks/list/?page={}&speaker=donald-trump"

for i in range(26):
    url = baseurl.format(str(i+1))
    response = requests.get(url)
    tree = html.fromstring(response.text)
    links = tree.cssselect('.m-statement__quote a')
    for link in links:
        link_address = link.attrib["href"]

contents = tree.cssselect('.')


##reviews = tree.xpath('//div[@class="reviews-single__text"]')
#reviewstext = [r.text.strip() for r in reviews]

#print(len(reviews),"reviews scraped. The first 60 characters of each:")
#i = 0
#for review in reviewstext:
   # print("Review",i,":",review[:60])
   # i+=1

