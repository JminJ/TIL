# N-gram #
---------------
> **SLM(Statistical Language Model)**
Neural Language Model이 등장하기 전, Lanuage Model은 통계 기반의 Statistical Language Model(SLM)을 통해 NLP를 수행하였다. 하지만 SLM은 단점이 존재했는데 train corpus에 확률을 계산하고 싶은 문장이나 단어가 없다면 확률을 계산할 수 없다는 것이다. 그러나 참고하는 단어들을 줄인다면 train corpus에서 해당 단어들을 찾을 확률이 올라갈 수 있다.

## N-gram ##
참고하는 단어들의 수의 개수를 정하기 위한 기준을 위해 사용하는 것이 n-gram이다. n-gram은 n개의 연속적인 단어 나열을 의미한다. n개씩 단어 뭉치로 끊으며 하나의 토큰으로 간주한다. An adorable little boy is spreading smiles라는 문장으로 n에 대해서 n-gram을 구해보자.
* unigrams : an, adorable, little, boy, is, spreading, smiles
* bigrams : an adorable, adorable little, little boy, boy is, is spreading, spreading smiles
* trigrams : an adorable little, adorable little boy, little boy is, boy is spreading, is spreading smiles
* 4-grams : an adorable little boy, adorable little boy is, little boy is spreading, boy is spreading smiles

4-grams부터는 앞에 숫자를 붙여 부른다. 때때로는 unigram, bigram, trigram 또한 1-gram, 2-gram, 3-gram이라고 불리기도 한다.

n-gram을 통한 언어 모델에서는 다음 단어를 예측할 때 n-1개의 단어에만 의존한다. 4-gram을 이용한다고 한다면, 4개의 단어로 나눈 토큰에서 앞 3개의 단어만을 예측에 사용하고 마지막 1단어를 예측의 결과로 반환한다. 

<img src = '/image/2021_02_18_1.png'>

위의 그림에서 boy is spreading 다음에 올 단어를 예측하는 것은 n-1에 해당하는 앞의 3개의 단어만을 고려한다.

## N-gram LM(language model)의 한계 ##

앞의 그림에서 An adorable little은 무시되고 boy is spreading만을 사용해 다음 단어를 예측했다. 이런 경우 boy에 대한 사전 정보가 사라져 사랑스러운 소년인지 아니면 난폭한 소년인지 알 수가 없게 된다. 따라서 앞 문장과 뒤에 이어지는 문장이 자연스럽게 이어지지 않는 경우가 생길 수 있다. 이러한 n-gram에 대한 한계를 아래에 서술한다.

### (1) 희소 문제(Sparsity Problem) ###

문장의 모든 단어를 보는대신 앞의 몇 단어만 봄으로써 corpus 내에 카운트 할 수 있는 확률을 높일 수는 있었지만, n-gram 언어 모델은 여전히 n-gram에 대한 희소 문제가 존재한다.

### (2) n을 선택하는 것은 trade-off 문제 ###

n을 크게 선택한다면 원하는 문장으로 끝나거나 문맥이 맞을 수 있지만 corpus에서 해당 n-gram을 카운트할 수 있는 확률은 매우 작아진다(희소 문제가 심각해진다). 또한 n이 커지면 커질 수록 모델 사이즈가 커지게 된다.

반면에 n을 작게 선택한다면 corpus에서 카운트는 잘 되지만 근사의 정확도는 확률분포와 멀어지게 된다. n은 최대 5를 넘게 잡아서는 안 된다고 권장이 된다.

-----------------
### 출처 ###
* <https://wikidocs.net/21692>