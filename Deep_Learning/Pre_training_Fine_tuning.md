# Pre-training과 Fine-tuning
-----
## Pre-training

 Multi Layered Perceptron(MLP)에서 weight와 bias를 좋게 초기화 시키는 방법. 초기화가 끝나고 나면 supervised learning, 즉 fine-tuning을 해줘야 한다. 

 또한 pre-training은 unsupervised learning이 가능하기에 label이 없는 큰 데이터를 넣어 학습시킬 수 있다는 장점이 있다.

## Fine-tuning

 이미 학습되어 있는 모델(pre-train model)을 바탕으로 새로운 task에 맞게 변형하고 pre-train model의 weight로부터 학습을 update하는 방법을 말한다.

 fine-tuning은 모델의 parameter를 미세하게 조정하는 행위다. 개와 고양이 분류 모델을 만들 때 ResNet과 같은 다른 데이터로 학습된 모델을 가져와 나의 추가 data를 투입해 이미 학습된 model parameter를 update한다. 중요한 점은 기존에 학습이 된 layer에 내 data를 추가로 학습시켜 parameter를 update하는 것이다.

---

### 출처

- [https://eehoeskrap.tistory.com/186](https://eehoeskrap.tistory.com/186)
- [https://blackpudding1996.tistory.com/3](https://blackpudding1996.tistory.com/3)