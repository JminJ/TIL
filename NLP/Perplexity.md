# Perplexity #
------
## PPL(Perplexity)

PPL은 언어 모델을 평가하기 위한 내부 평가 지표이다. 테스트 문장에 대한 확률(likelihood)를 구하고, PPL에 넣어 앞서 말한 듯 언어 모델의 성능을 평가한다. 

다른 평가 지표와는 다르게 PPL은 언어 모델이 헷갈리는 정도의 평균을 구한 것이므로 낮으면 낮을수록 언어모델의 성능이 높은 것이다(다음 단어 예측 확률이 높다는 뜻).

<img src = "/image\2021_02_25_05.png">

위는 문장 W의 길이가 N이라고 했을 때의 PPL 식이다.

위의 식에 chain rule을 적용하면 아래의 식과 같아진다.

<img src = "/image/2021_02_25_06.png">

여기에 n-gram을 적용하는 것 또한 가능하다.

<img src = "/image\2021_02_25_07.png">

## 분기 계수(Branching factor)

PPL은 선택할 수 있는 가능한 경우의 수를 의미하는 분기 계수이다. 앞서 말했지만 언어 모델이 특정 시점에서 평균적으로 몇 개의 선택지를 가지고 고민하고 있는지를 의미한다. PPL이 10일 경우는 다음 단어를 예측하는 모든 시점마다 평균적으로 10개의 단어를 헷갈리고 있다는 의미가 된다. 

<img src = "/image\2021_02_25_08.png">

위는 PPL이 10일때의 식 계산의 예이다.

이러한 PPL을 통해 두 개의 언어 모델의 성능을 대략적으로 판단할 수 있다. 하지만 이때 주의할 점은 정량적으로 양이 많고, 또한 도메인에 알맞은 동일한 테스트 데이터를 사용해야 이 비교의 신뢰도가 높아진다.

------
### 출처 ###
* <https://wikidocs.net/21697>