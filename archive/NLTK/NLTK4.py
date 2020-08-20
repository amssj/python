
from nltk.book import *
##条件
sent7
A = [w for w in sent7 if len(w) < 4]
print(A)
B = [w for w in sent7 if len(w) <= 4]
print(B)
C = [w for w in sent7 if len(w) == 4]
print(C)
D = [w for w in sent7 if len(w)!= 4]
print(D)

E = sorted([w for w in set(text1)if w.endswith('ableness')])
print(E)
F = sorted([term for term in set(text4) if 'gnt'in term])
print(F)
G = sorted([item for item in set(text6) if item.istitle()])
print(G)
H = sorted([item for item in set(sent7) if item.isdigit()])
print(H)

I = sorted([w for w in set(text7) if '-' in w and 'index' in w])
print(I)

J = sorted([a for a in set(text3) if a.istitle() and len(a) > 10])
print(J)

K = sorted([w for w in set(sent7) if not w.islower()])
print(K)

L = sorted([t for t in set(text2) if "cie" in t or 'cei' in t])
print(L)

len(text1)
len(set(text1))
len(set([w.islower for w in text1]))
M = len(set([w.islower for w in text1 if w.isalpha()]))
print(M)


