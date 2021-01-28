# from https://wikidocs.net/31698 #

from sklearn.feature_extraction.text import CountVectorizer

# make DTM

corpus = [
    "I don't like you",
    "why don't you play soccer??",
    'what should I do'
]

vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray())
print(vector.vocabulary_)

# use sklearn TfidfVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I don't like you",
    "why don't you play soccer??",
    'what should I do'
]

tfidfv = TfidfVectorizer().fit(corpus)
print(tfidfv.transform(corpus).toarray())
pritn(tfidfv.vocabulary_)