## tokenization
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize, sent_tokenize
word_example = "I love Python and R,and I have typed 'hello, world' to prove my loyalty to these two cute software. I also hope to make some friends! But most important, I hope I can strengthen my academic career."
print(sent_tokenize(word_example))
print(word_tokenize(word_example))
for i in word_tokenize(word_example):
    print(i)
##去除停用词
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
words = word_tokenize(word_example)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)
## 标准化stemmer.
from nltk.stem.porter import PorterStemmer
porter=nltk.PorterStemmer()
##test stemmer 检验词干提取器是否加载成功
porter.stem('going')
word_example = [porter.stem(i)for i in words]
## 词形还原 lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
word ="".join(lemmatizer.lemmatize(w)for w in words)
lemmatizer.lemmatize('was','v')
## 词性标准
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories=None)
unigram_tagger=nltk.UnigramTagger(brown_tagged_sents)
tag=unigram_tagger.tag(words)
nltk.pos_tag(words)
print(nltk.pos_tag(words))
## 构建词语——文档矩阵 tf-IDF矩阵
import textmining
def termdocumentmatrix_example():
    doc1 = "I love Python and R,and I have typed 'hello, world' to prove my loyalty to these two cute software. "
    doc2 = 'I also hope to make some friends!'
    doc3 = 'But most important, I hope I can strengthen my academic career.'
tdm = textmining.TermDocumentMatrix()
tdm.add_doc("doc1")
tdm.add_doc("doc2")
tdm.add_doc("doc3")
corpus = ['Your first document.',
          'Your second document.',
          'Your third document.']
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1)
vectorizer.fit_transform(corpus)
print(vectorizer.fit_transform(corpus))


            ##print(tagged)
    ##except Exception as e:
        ##print(str(e))

##process_content()
