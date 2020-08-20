###路透社
import nltk
from nltk.corpus import reuters
reuters.fileids()
reuters.categories()
reuters.categories('training/9865')
reuters.categories(['training/9864','training/9880'])
reuters.fileids('barley')
reuters.fileids(['barley','corn'])

##就职演说

from nltk.corpus import inaugural
inaugural.fileids()
A = [fileid[:4] for fileid in inaugural.fileids()]
print(A)
##计数就职演说语料库中所有以america或citizen开始的词
cfd = nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))
cfd.plot()
