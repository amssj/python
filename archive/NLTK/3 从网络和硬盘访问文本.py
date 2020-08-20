##从网页访问在线文本
from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
url = urlopen('https://www.bbc.co.uk/news')
html = url.read()
print(type(html)) ##查看raw的种类
print(html[:75])
print(len(html))

raw =BeautifulSoup(html).get_text()
tokens = nltk.word_tokenize(raw)
print(len(tokens))

print(raw.find('last'))
print(raw.rfind('disappear'))

tokens = tokens[96:399]
print(tokens)
text = nltk.Text(tokens)
print(text.concordance('gene'))
