import nltk
from nltk.book import *
###bigrams函数双连词
A = list(bigrams(["more","is","said","than","done"]))
print(A)

###找到比基于单个词的频率语气得到的更频繁出现的双连词 可以使用collocations
B = text4.collocations()
print(B)
C = text8.collocation_list()
print(C)

A = [len(w) for w in text1]
print(A)


from nltk.book import *
####文本中词语长度组成一个list；将词语长度生成一个词频分布表；展示所有的列表；不同词长的个数；频率最多的；某一个词的个数，频率
A = [len(w) for w in text1]
fdist = FreqDist([len(w) for w in text1])
fdist
B = fdist.keys()
print(B)
C = fdist.items()
print(C)
D = fdist.max()
print(D)
E = fdist[3]
print(E)
print(fdist.freq(3))

fdist.plot() ##绘制频率分布图
fdist.tabulate() ## 绘制频率分布表
fdist.plot(cumulative=True)
