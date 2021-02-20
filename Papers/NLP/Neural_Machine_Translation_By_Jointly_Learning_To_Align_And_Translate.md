# Neural Machine Translation By Jointly Learning To Align And Translate #
-----------
> **용어 정리**
>> - soft-alignment : attention 기법
>> - hard-alignment : 사람이 손수 원본 단어와 번역 단어를 매칭해 주는 방식

## Introduction

neural machine translation은 문장을 읽고 올바른 번역을 내놓는 단독이면서 큰 neural machine network를 만드는 시도를 했다. 가장 많이 제안된 neural machine translation 모델은 encoder-decoder 방식에 속하는 방법들이였다. encoder neural network는 source sentence를 읽고 길이가 고정된 벡터(fixed-length)로 encode한다. 이때 decoder는 encode된 vector로부터 번역(translatation)을 내보낸다. 언어 쌍을 위한 encoder, decoder를 가지고 있는 모든 encoder-decoder system은 주어진 source sentence 번역이 정확한 지를 나타내는 확률을 최대화 하기 위해 같이 학습된다.

그러나 encoder-decoder 방식은 잠재적인 문제점이 존재했는데, source sentence에 있는 사용 가능한 모든 정보를 길이가 고정된 벡터에 압축시켜야 한다는 점이였다. 이는 neural network로 하여금 자신이 학습한 문장보다 더 긴 문장을 만났을 경우 대처하는 것을 어렵게 만들게 된다. Cho et al.(2014b)에서는 input sentence의 길이가 늘어남에 따라 기본 encoder-decoder의 성능이 급격히 떨어지는 것을 보여주었다. 

이와 같은 이슈에 따라서, 저자들은 encoder-decoder 모델을 확장시켜 정렬과 번역을 동시에 배우는 접근법을 소개한다. 매 time마다 소개된 모델은 source sentence 에서 가장 집중되며 가장 연관있는 position들의 부분 집합을 찾고 번역한다. 그때 모델은 context vector에 기반하여 source position들과 이전에 만들어진 target word 에 관련된 target word를 예측한다.

이 접근방법의 가장 중요한 특징은 기존 encoder-decoder과는 달리 한정된 길이에 모든 input sentence를 encode하지 않는 다는 점이고, 대신에 input sentnece를 vector의 sequence로 encode하고  변환을 decoding 하는 동안 이러한 vector들의 부분 집합을 적응적으로 선택한다.

## Background: Neural Nachine Translation

neural machine translation의 관점에서는 parallel training corpus를 사용하는 문장 쌍의 조건부 확률을 최대화하기 위해 model의 파라미터를 학습한다. 조건부 분포가 training model에 의해 학습되었다면, translation에 해당하는 주어진 문장은 조건부 확률을 최대화하는 문장을 찾음으로써 생성될 수 있다. 

**RNN Encoder-Decoder**

Encoder-Decoder 프레임워크에서 encoder는 sequence of vector **x** = (x1,...xT_x)를 vector c로 읽는다. 가장 RNN을 사용하는 기본적인 접근법은 아래와 같다. 

<img src = '/image\2021_02_20_1.png'>

<img src = '/image\2021_02_20_2.png'>

ht ∈ R^n은 t번째 time의 hidden state이고, c는 hidden state의 sequence로부터 만들어진 vector들이다. q는 non-linear 함수인데 Sutskever et al. (2014)는 LSTM을 f와 q ({h1, · · · , hT }) = hT로 사용하였다. 

decoder는 주어진 context vector c와 이전 모든 예측된 단어들 {y1, · · · , yt'−1}을 예측에 사용하도록 훈련된다. 즉, decoder는 조인트 확률을 순서 조건부로 분해하여 변환에 대한 확률을 정의한다.

<img src = '/image\2021_02_20_3.png'>

**y** = (y1, · · · , yT_y). RNN과 함께 각 조건부 확률은 아래와 같이 modeled된다.

<img src = '/image\2021_02_20_4.png'>

g는 yt의 확률을 출력으로 하는 잠재적 multi-layered non-linear함수이고, st는 RNN의 hidden state이다. 알아두어야 하는 것은 RNN의 최신 모델이나 de-convolutional한 neural network와 같은 다른 architecture가 사용될 수 있다.

## Learning To Align And Translate

새로운 architecture의 neural network를 제안할 것인데, 새로운 architecture는 양방향 RNN을 encoder로 가지고 있고 translation을 decoding하는 동안 소스 문장을 통한 검색을 모방하는 decoder를 가지고 있다.

### **Decoder: General Description**

이 새로운 architecture에서 각 조건부 확률을 (2)와 동일하게 정의한다.

<img src = "/image\2021_02_20_5.png">

si는 RNN 아래와 같이 계산되는 i 번째 hidden state를 의미한다.

<img src = "/image\2021_02_20_6.png">

context vector ci는 encoder가 input sentence를 map한 annotation (h1, . . . , hT_x)에 의존한다. 각 annotation hi는 모든 input sequence의 정보를 input sequence의 i번째 단어 주변 부분에 얼마나 강하게 forcus하는지와 함께 포함하고 있다. 자세한 설명은 추후에 한다.

annotation hi와의 weighted sum을 통해 ci가 계산된다.

<img src = "/image\2021_02_20_7.png">

weight 각 annotation hj의 αij는 아래와 같이 계산된다.

<img src = "/image\2021_02_20_8.png">

<img src = "/image\2021_02_20_9.png">

eij는 input position j 주변과 output position i가 얼마나 잘 맞는지를 score하는 alignment model이다. score은 RNN hidden state si와 input sentence의 j번째 annotation hj에 기반을 두고 있다.

우리는 alignment model a를 제안된 system의 다른 component들과 함께 학습되는 feedforward neural network로서 매개변수화 한다(parameterize). 주목해야 할 점은 전통적 기계번역과 다르게 alignment가 잠재변수로 고려되지 않는다. 대신, alignment model이 cost function의 기울기가 backpropagete되게 하는 soft alignment를 직접 연산한다. 이 gradient는 alignment model과 전체 번역 model을 공동으로 훈련하는데 사용할 수 있다.

우리는 모든 annotation의 가중 합을 갖는 접근법을 expected annotation을 계산하는 것이라고 이해할 수 있다. expectation이란 가능한 모든 alignment를 의미한다. αij를 source word xj로부터 정렬되거나 번역된 target word yi의 확률이라고 해보자. 그때 i번째 context vector ci는 αij 확률과 함께 모든 annotation들로부터 기대되는 annotation일 것이다.

확률 α_ij( == αij) 또는 그것의 관련된 energy e_ij( == eij)는 다음 state s_i( == si)를 정하고 y_i( == yi)를 만드는 이전 hidden state s_i-1에 관하여 annotation h_j( == hj)의 중요성을 반영한다. 직감적으로, 이것은 decoder의 attention mechanism을 향상 시켜줄 것이다. 이제 decoder는 source sentence에서 집중해야하는 부분을 결정할 수 있다. decoder이 attention mechanism을 갖게 함으로써, encoder가 모든 source sentence의 정보를 고정된 길이의 vector로 압축해야 했던 부담을 완화시킬 수 있게 되었다.

<img src = "/image\2021_02_20_10.png">

### Encoder: Bidirectional RNN For Annotating Sequences

기존의 RNN과 다르게 제안하고 있는 scheme는 이전 단어들 뿐만 아니라 따라오는 단어들 또한 요약해 annotation으로 갖고 싶어 Bidirectional RNN(BiRNN)을 제안하였다. 

BiRNN은 forward, backward RNN을 가지고 있다. forward RNN f1은 input sequence를 순서대로(x_1에서 x_Tx의 순서대로) 읽고 forward hidden state(h1_1, . . . , h1_Tx)의 sequence를 계산한다. 이와 비슷하게 backward RNN f2는 input sequence를 반대 순서대로 읽고 backward hidden state의 sequence를 만들어낸다.

각 단어 x_j의 annotation을 forward hidden state h1과 backward hidden state h2를 연결시켜서 얻을 수 있다 i.e. h_j = [h1 ; h2]. 이 경우, h_j는 양 방향 모두의 요약(summarize)를 포함할 수 있게 된다. RNN의 더 좋게 현재 input을 표현하는 경향 때문에 annotation h_j는 x_j 주변의 단어에 초점을 잘 맞춘다. 이 annotation의 sequence는 decoder와 alignment model에서 후에 context vector를 계산하는데 사용된다(Eqs. (5)-(6)). 

Fig1에서 제안된 모델의 그래픽 삽화를 볼 수 있다.

## Experiment Settings

제안한 접근법을 통해 English-to-French 번역 과제를 평가할 것이다. ACL WMT'14에서 제공한 bilingual, parallel corpora를 사용한다. 2014년도 Cho가 제안한 RNN Encoder-Decoder 방법의 성능을 기록하고 비교할 것이다. 물론 같은 과정과 같은 데이터셋을 양 모델이 사용할 것이다.

### Dataset

WMT'14는 총 850M개의 English-French parallel corpora를 여러 corpora들을 합쳐 보유하고 있다. Cho et al.(2014a)에 기재된 절차에 따라 Axelrod et al.(2011)의 data selection 방법을 사용해 뭉쳐있는 corpus를 348M개의 크기로 줄인다. 우리는 encoder를 pre-tarin하기 위해 앞서 말한 데이터 말고는 어떠한 monolingual data를 사용하지 않았다. 

<img src = '/image\2021_02_20_11.png' width = '90%'>

development set (validation set)을 만들기 위해 news-test-2012와 news-test-2013 데이터를 합쳤고, 모델을 평가하기 위해 WMT'14의 test set(news-test-2014)을 사용했다(training 동안에 이 data를 사용하지 않음).

tokenization 이후, 우리 모델이 train되는 동안 각 언어마다 가장 많이 등장한 30,000 단어를 shortlist로 만들었다. 30,000개 이외의 단어들은 special token([UNK])으로 변환되었다. 이 외의 전처리는 더이상 진행하지 않았다 i.e. lowercasing, stemming.

### Models

두 가지 모델을 학습시켰는데, 하나는 RNN Encoder-Decoder 모델(RNNencdec, Cho et al., 2014a)이고, 나머지 하나는 우리가 제안한 RNNsearch모델이다. 이 모델들을 각각 두 번 학습시켰다: 첫 번째는 30개 단어 길이보다 긴 문장을 사용해 학습시켰고(RNNencdec-30, RNNsearch-30), 두 번째는 50개 단어 길이보다 긴 문장을 사용해 학습시켰다(RNNencdec-50, RNNsearch-50).

 RNNencdec의 encoder, decoder는 각각 1000 hidden unit들을 가지고 있다. RNNsearch의 encoder는 1000개의 hidden unit을 가지고 있는 forward, backward RNN을 포함하고 있다. decoder 또한 1000개의 hidden unit을 가진다. 두 가지 케이스에서 multilayer network를 각 target word의 조건부 확률을 계산하기 위한 single maxout hidden layer와 함께 사용한다.

추가로 SGD를 Adadelta와 각 모델을 학습시키기 위해 사용했다. 각 SGD는 80개 문장의 minibatch로 direction을 계산하고 업데이트 했다.

train이 종료되면, beam search를 사용해 조건부 확률을 대략적으로 감소시키는 번역을 찾았다. Sutskever et al.(2014)는 이 접근법을 그들의 neural machine translation model에 적용시켜 번역을 만들어냈다.

## Results

### Quantitative Results

<img src = "/image\2021_02_20_12.png" width = '90%'>

Table 1은 BLUE score를 사용해 번역의 성능을 측정한 표이다. 확실한 것은 RNNsearch가 기존의 RNNencdec을 월등히 뛰어넘는다는 것이다. 더 중요한 사실은 학습된 단어로만 구성된 문장이라고 했을때, RNNsearch는 기존의 phrase-based 번역 시스템(Moses) 만큼이나 성능이 뛰어나다는 것이다. 이것은 Moses가 RNNsearch와 RNNencdec를 train하는데 사용한 parallel corpora에 더해 418M 단어의 단일 언어 corpus를 훈련하는데 사용했다는 것을 감안하면 중요한 성과이다.

이 접근법을 구상하게 된 계기는 기본 encoder-decoder 접근법에서 고정된 길이의 context vector를 사용한다는 점이였다. 우리는 기존 encoder-decoder는 길이가 긴 문장이 들어오면 위의 이유로 성능이 떨어질것이라 판단했다. 실제로 Fig.2에서 RNNencdec는 길이가 긴 문장이 들어올 때 성능이 매우 떨어지는 것을 볼 수 있다. 반면 RNNsearch-30, 50은 길이가 긴 문장에 대해 더 강한 모습을 보여준다. 특히 RNNsearch-50은 문장 길이가 50 혹은 더 길든 성능 감소가 거의 없는 것을 보여준다.

### Qualitative Analysis

**Aligment**

<img src = "/image\2021_02_20_13.png">

Fig.3는 번역 문장과 기존 source sentence의 Eq.(6)에서 나온 annotation weights α_ij 를 보여주고 있다. 각 행은 annotation에 관련된 weight들을 나타낸다. 이 그림을 통해 target word를 만들기 위해 둥요하게 고려하는 source sentence를 볼 수있다.

영어와 프랑스어의 다른 어순 또한 제안한 이 모델이 잘 해석을 할 수 있다.

hard-alignment와 비교해서 soft-alignment의 힘은 Fig.3에서 확인할 수 있다. [l' homme]로 번역되는 [the man] source sentence를 고려하겠다. hard-alignment는 [the]를 [l']으로, [man]을 [homme]로 지정해 줄 것이다. 이것은 번역에 대해 별로 도움이 되지 않는다. [the]는 번역할 때 [le], [la], [les] 또는 [l']으로 번역할 수 있기 때문이다. 이런 문제를 우리의 soft-alignment는 model이 [the]와 [man]을 둘 다 보게 함으로써 해결하였다. 예를 들어, 우리는 model이 [the]를 [l']로 번역을 정확히 했다고 알 수 있다. 우리는 Fig.3에 제시된 모든 사례에서 비슷한 행동을 볼 수 있었다. 또 다른 soft-alignment의 이점은 source와 target phrase의 다른 길이를 [NULL]으로 mapping하지 않고 자연스럽게 처리한다는 것이다. 

**Long Sentences**

RNNsearch는 기존의 model(RNNencdec)보다 훨씬 긴 문장을 잘 번역한다. 이는 RNNsearch는 고정된 길이로 긴 문장을 완벽히 encoding할 필요가 없고 특정 단어를 둘러싸는 input sentence의 부분만 정확하게 encoding 할 필요가 있기 때문일 것이다.

예를 들어, test set의 source sentence를 고려해 보자. 

<img src = "/image\2021_02_20_14.png" width = '90%'>

RNNsearch-50은 아래와 같이 번역한다.

<img src = '/image\2021_02_20_15.png' width = '90%'>

RNNencdec-50은 souce sentence에서 [a medical center]까지 올바르게 번역한다. 그러나 밑줄 친 부분은 원본 문장의 뜻에서 벗어났다. 반면, RNNsearch는 어떠한 detail을 방출하지 않고  input 문장 전체 뜻을 온전히 보존하는 번역을 만들었다.

<img src = '/image\2021_02_20_16.png' width = '100%'>

test set의 또 다른 문장을 봐보자.

<img src = '/image\2021_02_20_17.png' width = '80%'>

RNNencdec-50이 번역한 것을 보면,

<img src = '/image\2021_02_20_18.png' width = '90%'>

이전의 예시와 같이, RNNencdec은 대략 30단어를 생성한 후 source sentence의 실제 뜻으로 부터 잃어버리기 시작했다(밑줄 친 부분). 이 포인트를 지난 후, 종료 따옴표 표시의 부족 같은 기본적인 실수와 함께 번역의 질이 매우 떨어졌다. 

다시, RNNsearch-50은 이 긴 문장을 정확히 번역할 수 있다:

<img src = "/image\2021_02_20_19.png" width = '90%'>

이미 제시 된 quantitative result와 함께, 이 질적인 발견들은 RNNsearch 모델이 기존 RNNencdec 모델보다 긴 문장을 번역할 때 더 믿을만 하다는 것을 보여준다.

## Conclusion

기존의 neural machine translation, 통칭 encoder-decoder 접근법은 전체 input sentence를 고정된 길이의 decoder가 decode해야 할 vector로 만들어야 한다. 이에 저자들은 이러한 방식이 긴 문장을 번역해야 할 때 문제점이 있을 것이라 추론했다.

이 논문에서 이러한 문제를 해결하는 새로운 architecture를 제안한다. (soft-)model이 각 대상 단어를 생성할 때 입력 단어 집합 또는 encoder가 계산한 annotation을 검색하도록 하여 기본 encoder-decoder를 확장했다. 이는 model이 모든 source sectence를 고정된 길이의 vector에 encode해야 하는 것에 대해 자유롭고 다음 target word를 만들 때 연관된 정보에만 집중할 수 있게 해준다. 다른 전통적 machine translation system들과는 달리, 정렬 메커니즘을 포함한 모든 변환 시스템 조각은 정확한 번역을 생성할 수 있는 더 나은 log-probability를 위해 공동으로 훈련된다.

-----------
### 출처 
* <https://arxiv.org/pdf/1409.0473.pdf?utm_source=ColumnsChannel>