###WordNet是面向语义的英语词典，与传统辞典类似，但结构更丰富。nltk中包括英语WordNet，共有155287个单词和117659个同义词。
import nltk
from nltk.corpus import wordnet as wn
print(wn.synsets('motorcar'))
##car.n.01被称为synset或同义词集，意义相同的词的集合

##访问同义词集
print(wn.synset('car.n.01').lemma_names())
##结果现实 ['car', 'auto', 'automobile', 'machine', 'motorcar']
##同义词一般的定义
print(wn.synset('car.n.01').definition())

print(wn.synset('car.n.01').examples())

##同义词集和词的配对叫做词条
##得到同义词集的所有词条
print(wn.synset('car.n.01').lemmas())

##查找特定的词条
print(wn.lemma('car.n.01.automobile'))

##得到一个词条对应的同义词集
print(wn.lemma('car.n.01.automobile').synset())

##得到一个词条的名字
print(wn.lemma('car.n.01.automobile').name())

##automobile或者motocar这意义明确的只有一个同义词集，car有五个同义词集
print(wn.synsets('car'))

for synset in wn.synsets('car'):
    print(synset.lemma_names())

print(wn.lemmas('car'))

print(wn.synsets('dish'))
##访问所有包含dish的词条
for synset in wn.synsets('dish'):
    print(synset.lemma_names())
print(wn.synset('dish.n.01').definition())
print(wn.synset('dish.n.01').examples())
print(wn.lemmas('dish'))


###wordnet的层次结构
#WordNet的同义词集对应于抽象的概念，它们并不总是有对应的英语词汇。这些概念在 层次结构中相互联系在一起。一些概念也很一般，如实体、状态、事件;这些被称为独一无 二的根同义词集。

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms() ##查看下位词
print(types_of_motorcar[26])
a = sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())
print(a)

##访问上位词浏览层次结构
print(motorcar.hypernyms)
paths = motorcar.hypernym_paths() ##查看路径
print(len(paths))
A = [synset.name for synset in paths[0]]
print(A)
B = [synset.name for synset in paths[1]]
print(B)

print(motorcar.root_hypernyms())

print(nltk.app.wordnet())

