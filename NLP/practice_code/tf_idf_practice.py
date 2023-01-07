# from https://wikidocs.net/31698 #

from sklearn.feature_extraction.text import CountVectorizer

# make DTM

corpus = [
    "I don't like you",
    "why don't you play soccer??",
    'what should I do'
]

vector = CountVectorizer()
# print(vector.fit_transform(corpus).toarray())
# print(vector.vocabulary_)

# use sklearn TfidfVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I don't like you",
    "why don't you play soccer??",
    'what should I do'
]

tfidfv = TfidfVectorizer().fit(corpus)
# print(tfidfv.transform(corpus).toarray())
# print(tfidfv.vocabulary_)

# implement version
import numpy as np
from typing import Dict, List

def _make_vocab(datas:List)->Dict:
    vocab = {}

    for d in datas:
        split_by_space = d.split(" ")
        for t in split_by_space:
            if t not in vocab.keys():
                vocab[t] = len(vocab.keys())
            
    return vocab

def tf(d:List, vocab:Dict)->np.ndarray:
    vocab_keys = list(vocab.keys())
    tf_result = np.zeros(shape=(len(d), len(vocab_keys)))

    for i in range(len(d)):
        temp_d = d[i]
        for j in range(len(vocab_keys)):
            temp_t = vocab_keys[j]
            t_count = temp_d.count(temp_t)

            tf_result[i][j] = t_count

    return tf_result
        
def df(d:List, vocab:Dict)->List:
    df_result = []
    vocab_keys = list(vocab.keys())
    for i in range(len(vocab_keys)):
        temp_t = vocab_keys[i]
        df_result.append(0) # define temp t into df_result

        for j in range(len(d)):
            temp_d = d[j]
        
            if temp_t in temp_d:
                df_result[i] += 1
            
    return df_result

def idf(df:List, n:int)->List:
    idf = []
    
    for i in range(len(df)):
        temp_idf = np.log(n/1+df[i])
        idf.append(temp_idf)

    return idf

def tf_idf(idf:List, tf:np.ndarray)->np.ndarray:
    idf = np.array(idf)
    tfidf_result = tf*idf.T

    return tfidf_result

ex_datas = [
    "저는 홍길동 입니다",
    "저는 노래를 좋아합니다",
    "지금도 노래를 듣고 있습니다"
]

vocab = _make_vocab(datas=ex_datas)

tf_result = tf(d=ex_datas, vocab=vocab)
# print(tf_result)
# print()
df_result = df(d=ex_datas, vocab=vocab)
idf_result = idf(df=df_result, n=tf_result.shape[0])
# print(idf_result)
# print()
tf_idf_result = tf_idf(idf=idf_result, tf=tf_result)
print(tf_idf_result)