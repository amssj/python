import nltk
##使用语料库模块处理 austen-persuasion.txt。这本书中有多少词标识符?多少词 类型?
gutenberg_words = nltk.corpus.gutenberg.words(fileids = 'austen-sense.txt')
print(len(gutenberg_words))
print(len(set(gutenberg_words)))

##使用布朗语料库阅读器 nltk.corpus.brown.words()或网络文本语料库阅读器 nltk. corpus.webtext.words()来访问两个不同文体的一些样例文本
A = nltk.corpus.brown.categories()
print(A)

B = nltk.corpus.brown.words(categories = 'adventure')
print(B)

#使用 state_union 语料库阅读器，访问《国情咨文报告》的文本。计数每个文档中 出现的 men、women 和 people。
# 随时间的推移这些词的用法有什么变化?

from nltk.corpus import state_union
from nltk import ConditionalFreqDist
cfd = ConditionalFreqDist(
    (target,fileid[:4])
     for fileid in state_union.fileids()
     for w in state_union.words(fileid)
     for target in ['men','women','people']
)
cfd.plot()


#在名字语料库上定义一个条件频率分布，显示哪个首字母在男性名字中比在女性名字 中更常用

from nltk.corpus import names
cfd1 = ConditionalFreqDist(
    (fileid,w.lower()[0])
    for fileid in names.fileids()
    for w in names.words(fileid)
)

cfd1.plot()

##写一个程序，找出所有在布朗语料库中出现至少 3 次的词。
from nltk.corpus import brown
from nltk import FreqDist
words = brown.words()
fd = FreqDist([w.lower() for w in words])
freq_words = [w for w in fd if fd[w] >=3]
print(freq_words)

