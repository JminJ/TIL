# label smoothing #
-----
## Introduction

 우리는 모델을 학습 시킬 때 수 많은 종류의 label로 분류된 많은 양의 데이터를 다룬다. 당연히 많은 양의 데이터는 우리의 모델을 강하게 만들어 줄 최고의 재료일 테지만 데이터 중간 중간 잘못 label된 데이터가 숨어있다면 이는 되려 모델이 잘못된 방향으로 학습하게 하는 주범이 될 수 있다. 

 강아지와 고양이의 사진을 분류하는 모델을 예로 들어본다. 인터넷에서 최대한 사진을 긁어 모았고 이를 손수 label을 달아주어 학습 데이터 셋을 만들었다. 그러나 새벽에 졸린 상태로 labeling을 하는 바람에 많은 양의 고양이 사진을 강아지 사진이라고 labeling하고 말았다. 그러면 일반적인 binary calssification학습에 사용되는 loss 식은 아래와 같다.

<img src = '/image/2021_03_28_1.png'>

이 경우 label은 0 또는 1로 주어지므로 언제나 고양이는 0, 강아지는 1이라는 것을 의미한다. 그러나 아까 말했듯 labeling의 오류가 발생하는 경우에는 이는 무조건 0, 1이라는 가정이 틀리게 된다. 따라서 잘못된 loss의 영향을 줄이기 위해 label을 smooth하게 부여하는 것이 **label smoothing**의 아이디어다.

## label smoothing

 

```
new_onehot_labels = 
    onehot_labels * (1-label_smoothing) + label_smoothing/num_classes
```

label smoothing의 수식이다. 앞서 예를 든 고양이/강아지 이진 분류 문제를 예를 들면 새로운 label을 아래와 같이 계산할 수 있다(label smoothing == 0.2).

```
new_onehot_labels = 
    1 * (1-0.2) + 0.2/2 = 0.9
```

따라서 원래 0으로 부여되어있던 고양이 label의 경우, 1 - 0.9 = 0.1로 계산이 된다. 

---

### 출처

- [https://3months.tistory.com/465](https://3months.tistory.com/465)
- [https://ratsgo.github.io/insight-notes/docs/interpretable/smoothing](https://ratsgo.github.io/insight-notes/docs/interpretable/smoothing)