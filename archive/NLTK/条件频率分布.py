import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word) ###条件，事件
    for genre in brown.categories()
    for word in brown.words(categories=genre))
print(cfd)
##只看两个condition
genre_word = [(genre,word)
              for genre in ['news','romance']
              for word in brown.words(categories=genre)]

print(len(genre_word))

print(genre_word[:4])
print(genre_word[-4:])
##输入变量名称检查它，确认有两个condition
cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
##查看条件是什么
print(cfd.conditions())
##查看每一个条件的频率分布
print(cfd['news'])
print(cfd['romance'])
##查看条件内容的列表
print(list(cfd['romance']))
##以索引的方式查看某一个词有多少个
print(cfd['romance']['could'])


#####绘制条件分布图和分布表
from nltk.corpus import inaugural
cfd1 = nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america','citizen']
    if w.lower().startswith(target))

cfd1.plot


from nltk.corpus import brown
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Sunday','Saturday']
cfd2 = nltk.ConditionalFreqDist(
    (genre,words)
    for genre in ['news','romance']
    for words in brown.words(categories=genre)
)
cfd2.plot(samples=days)

