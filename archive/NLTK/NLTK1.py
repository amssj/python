
import nltk
nltk.download()

from nltk.book import *
##表示上下文
text1.concordance("monstrous")
text2.concordance("affection")
text3.concordance("lived")
## 哪些词出现在相似的上下文中
text1.similar("monstrous")
text2.similar("monstrous")
##分析两个或两个以上的词共同的上下文
text2.common_contexts(["monstrous","very"])


##离散图

text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])

##根据不同的风格产生一些随机文本
text4.generate()

text1.generate()

##len可以算出文本中所有的标识符 print将结果打印出来
print(len(text3))
##set获得text3的词汇表 文章中唯一的项目类型
sorted(set(text3))
print(sorted(set(text3)))
print(len(set(text3)))

###除法 用所有标识符的数量除以文章中项目的数量，注意需要用浮点除法，在3版本中是/ 如果是整数除法是//
print(len(text3)/len(set(text3)))

## 计算特定的词在文本中所占的比例
print(text3.count("smote"))
print(text4.count("a")/len(text4))
###生成两个函数
def lexical_diversity(text):
    return len(text)/len(set(text))
def percentage(count,total):
    return 100 * count/total
