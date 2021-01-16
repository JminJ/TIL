from nltk.tokenize import sent_tokenize

text = '안녕하세요 저는 정민주라고 합니다. 요즘 자연어 처리에 관심을 쏟아부어 공부하고 있습니다. 하루 하루를 알차게 보내고 싶습니다~!'
n_t_list = sent_tokenize(text)
print(n_t_list)