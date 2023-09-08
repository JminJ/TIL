# Incremental Learning

## Intro
Incremental Learning(증분학습)은 이전에 학습한 지식을 잊지 않으며 새로운 지식을 배워나감으로써 강화하는 머신러닝 기법이다. 

## Explaining Incremental Learning
기존의 batch learning은 전체 데이터셋을 통해 **한 번** 학습을 한다. 반면 Incremental learning은 새로운 데이터를 통해 model parameter를 확장해 업데이트한다(이것이 batch learning과의 극명한 차이이다).

## Benefits From Incremental Learning
### Efficient use of resources
Incremental learning은 적은 양의 데이터를 저장하므로 이는 상당한 메모리를 아낄 수 있다.
### Real-time adaptation
이 모델들은 변화를 즉시 적용할 수 있다. 뉴스기사를 추천하는 모델을 예로 들어보자면, 유저들의 선호도 변화를 바로 배울 수 있고 그들의 최신 흥미있는 주제에 따라 뉴스기사를 추천할 수 있다.
### Efficient Learning
Task를 더 작은 부분으로 나누게 되면 새로운 task를 빠르고 효과적으로 학습하는 machine learning 모델의 성능을 향상시킬 수 있다. 또한 incremental learning은 모델의 정확도를 높이는데 도움이 된다.
### Learning from non-stationary data
현실세계는 데이터가 급속도로 증가될 수 있다. 따라서 incremantal learning 모델은 매우 값어치가 있다. 날씨 예측 모델의 경우 가장 최근의 기후 데이터를 기반으로 지속적으로 예측을 강화할 수 있다.

## Limitations of Incremental Learning
### Catastrophic forgetting
"incremental learning"의 주된 challenge 중 하나로, 새로운 데이터를 배우면 이전에 학습한 정보를 잊는 경향이 있는 것을 말한다.
### Difficulty in handling concept drift
Incremental learning은 강화된 데이터를 처리하게끔 디자인 되어있으나 데이터 트렌드의 급격한 변화나 "concept change"가 되려 challenge가 될 수 있다.
### Risk of overfitting
Incremental learning은 데이터의 흐름에 의존하므로 전체 데이터의 분포를 표현하지 않는 최신 데이터를 기준으로 모델의 파라미터가 과하게 수정되버릴 수 있다. 

------
### 출처
* https://www.datacamp.com/blog/what-is-incremental-learning