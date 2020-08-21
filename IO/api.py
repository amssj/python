from urllib.request import urlopen
import json
from pprint import pprint
antwoord=urlopen('https://www.googleapis.com/books/v1/volumes?q=inauthor:"Niklas+Luhmann"').read()
data=json.loads(antwoord.decode("utf-8"))
pprint(data)