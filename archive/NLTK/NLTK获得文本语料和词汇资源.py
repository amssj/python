
import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(len(emma))

from nltk.corpus import gutenberg
gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')
print(emma)

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
print(macbeth_sentences[1037])
longest_len = max([len(s) for s in macbeth_sentences])
print(longest_len)
A = [s for s in macbeth_sentences if len(s) == longest_len]
print(A)

##words(),raw(),sents()
