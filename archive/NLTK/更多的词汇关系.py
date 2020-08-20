###更多的词汇关系（局部与整体）
from nltk.corpus import wordnet as wn
print(wn.synset('tree.n.01').part_meronyms())
print(wn.synset('tree.n.01').substance_meronyms())
print(wn.synset('tree.n.01').member_holonyms())

for synset in wn.synsets('mint',wn.NOUN):
    print(synset.name() + ':', synset.definition())

print(wn.synset('mint.n.04').part_holonyms())
print(wn.synset('mint.n.04').substance_holonyms())
##动词之间也有关系。例如:走路的动作包括抬脚的动作，所以走路蕴涵着抬脚。一些动
#词有多个蕴涵:

print(wn.synset('walk.v.01').entailments())
print(wn.synset('eat.v.01').entailments())

###词条之间的词汇关系，反义词
print(wn.lemma('supply.n.02.supply').antonyms())
print(wn.lemma('rush.v.01.rush').antonyms())
print(wn.lemma('horizontal.a.01.horizontal').antonyms())
print(dir(wn.synset('harmony.n.02')))#查看词汇关系和同义词集上定义的其他方法

##语义相似度
##连接到同一个根的两个同义词集可能有一些共同的上位词，如果两个同义词集共同用一个
##非常具体的上位词，他们一定有密切的关系
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
print(right.lowest_common_hypernyms(minke))
print(right.lowest_common_hypernyms(orca))
print(right.lowest_common_hypernyms(tortoise))
print(right.lowest_common_hypernyms(novel))
##通过查找每个同义词集深度量化一般性的概念
print(wn.synset('baleen_whale.n.01').min_depth())
print(wn.synset('whale.n.02').min_depth())
##wordnet同义词集的集合上定义了类似的函数能够深入观察，path_similarityassigns是基于上位词层次结构中相互连接的概念之间的最短路径在0-1范围内的打分
print(right.path_similarity(minke))
print(right.path_similarity(orca))
print(right.path_similarity(tortoise))
print(right.path_similarity(novel))

# https://www.jianshu.com/p/c692eb0a5e88 wordnet的介绍
