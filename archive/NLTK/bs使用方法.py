from bs4 import BeautifulSoup

#https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc)
print(soup.prettify()) ##按照标准的缩进格式输出
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))
for link in soup.find_all('a'):
    print(link.get('href'))##从文档中找出所有a标签的链接
print(soup.get_text()) ##从文档中获取所有文字内容
