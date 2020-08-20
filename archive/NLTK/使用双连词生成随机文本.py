import nltk
##循环15次，找到word条件分布最高的词

def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word),
        word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text) ##生成双连词
cfd = nltk.ConditionalFreqDist(bigrams) ##以双连词生成条件分布
print(cfd['living']) ##指定某一个词生成条件分布 cfdist[condition] cfdist[condition][sample]此条件下给定样本的频率
generate_model(cfd,'living')
##cfdist.tabulate()条件频率分布制图
##cfdist.tabulate()指定样本和条件限制下制表
##cfdist1 < cfdist2 测试样本在cfdist1中出现的次数是否小于cfdist2中出现的次数
