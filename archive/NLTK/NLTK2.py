
from nltk.book import *

##链接两个链表
ex1 =["Hi","My","name","is","Liu Shujun",".","is"]
ex2 =["What","'s","your","name","?"]
print(ex1+ex2)
#链表中追加一个元素
ex1.append("I")

###元素的索引
print(text4[100])
## 找出一个词第一次出现的索引
print(text4.index("awaken"))
##文本切片
print(text4[11456:12000])


###可以把词用链表连接起来组成单个字符串，或者把字符串分割成一个链表
A = ''.join(['Monty','Python'])
print(A)

B = 'Monty Python'.split()
print(B)



##FreqDist寻找白鲸记中最常见的50个词

fdist1 = FreqDist(text1)
fdist1
##表达式key提供了文本中所有不同类型的链表，并转化为list
vocabulary1 = fdist1.keys()
vocab = list(vocabulary1)
a = vocab[:50]
print(a)
print(fdist1['whale'])
##查看前50个词的累计频率图
fdist1.plot(50,cumulative = True)
##查看剩余的词
b = fdist1.hapaxes()
print(b)

### 查找文本词汇中长度超过15个字符的词
V = set(text1)
long_words = [w for w in V if len(w) > 15]
a = sorted(long_words)
print(a)

### 查找text5中长度大于7，频率大于7的数据

fdist5 = FreqDist(text5)
A = sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7])
print(A)

