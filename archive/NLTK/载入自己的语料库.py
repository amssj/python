##载入自己的语料库 PlaintextCorpusreader会识别出所有txt文档，后面正则符号'.*'表示txt文档

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/xiaogo627301968qq.com/PycharmProjects/NLTK/source/lob'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(wordlists.fileids())
##访问指定文件的原始内容
raw = wordlists.raw("LU-A-BL")
print(raw)
