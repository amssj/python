##词汇列表语料库
##过滤文本：计算文本中的词汇表，删除所有在现有的词汇列表中出现的元素，只留下罕见或拼写错误的词
import nltk
from nltk.corpus import stopwords
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha)
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)
A = unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
print(A)

B = unusual_words(nltk.corpus.nps_chat.words())
print(B)
##去除停用词后的文本占整体文本的多少
def fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

C = fraction(nltk.corpus.reuters.words())
print(C)
##找到同时出现在两个文件中的名字，即暧昧的名字
names = nltk.corpus.names
print(names.fileids())
male_names = names.words('male.txt')
female_names = names.words('female.txt')
D = [w for w in male_names if w in female_names]
print(D)
##查看最后一个字母的分布在两个文件中的体现
cfd = nltk.ConditionalFreqDist(
    (fileid,name[-2])
    for fileid in names.fileids()
    for name in names.words(fileid)
)

cfd.plot()
print(len(names.words('male.txt')))
print(len(names.words('female.txt')))
