##网络和聊天文本
import nltk
from nltk.book import *
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65],'...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])

##布朗语料库
from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories='news'))
print(brown.words(fileids=['cg22']))
print(brown.sents(categories=['news','editorial','reviews']))

news_text = brown.words(categories='news')
fdist = FreqDist([w.lower() for w in news_text])
modals = ['can','could','may','might','must','will']
for m in modals:
    print(m + ':',fdist[m])

modals1 = ['what','when','where','who','why']
for m in modals1:
    print(m + ':',fdist[m])


from nltk.corpus import brown

cfd= nltk.ConditionalFreqDist(
(genre,word)
for genre in brown.categories()
for word in brown.words(categories=genre)
)
genres=['news','religion','hobbies','science_fiction','romance','humor']
modals=['can','could','may','might','must','will']
print(cfd.tabulate(conditions=genres,samples=modals))
