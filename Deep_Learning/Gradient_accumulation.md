# Gradient Accumulation #
-----
> 이 글은 [Gradient Accumulation: Overcoming Memory Constraints in Deep Learning](https://towardsdatascience.com/gradient-accumulation-overcoming-memory-constraints-in-deep-learning-36d411252d01) 을 번역 및 정리한 글입니다.

### Intro

Deep Learning을 할 때 GPU가 없다는 것은 매우 골치아픈 일이다. 물론 Colab이나 Kaggle에서 GPU를 사용할 수 있지만 우리가 언제나 MNIST 같은 작은 모델을 만들수는 없는 노릇이다.

### Introduction

state-of-the-art 모델을 학습시키기 위해서는 GPU는 꼭 필요하다. 하지만 겨우 하나를 장만한다 하더라도 GPU Memory의 부족 현상이 나타나게 된다. 그래서 이제는 큰 batch size로 모델을 학습할 때 보는 OOM(Out Of Memory) 에러가 익숙해질 지경이다. 특히 이 문제는 state-of-the-art computer vision 알고리즘에서 많이 나타난다. 최근의 아키텍쳐들인 UNet, ResNet-152, RCNN, Mask-RCNN는 매우 큰 memory를 요구한다. 이런 이유로 깊은 모델을 학습할 때 높은 확률로 OOM 에러가 발생하게 된다. 

아래에 pytorch에서 발생하는 OOM 에러를 적어 두었다.

```
RuntimeError: CUDA out of memory. Tried to allocate 44.00 MiB (GPU 0; 10.76 GiB total capacity; 9.46 GiB already allocated; 30.94 MiB free; 9.87 GiB reserved in total by PyTorch)
```

실무자들이 OOM 에러를 즉시 해결할 수 있는 방법은 2가지가 있다.

1. batch size를 줄인다.
2. 이미지의 dimension을 줄인다.

90%의 상황에서는 위 두 방법으로 해결이 가능하다. 하지만 나머지의 상황에서는 이 방법들로는 해결이 어렵다. 이 상황들을 살펴보자.

<img src = '/image/2021_03_06_01.png'>

Kaggle 대회인 [Understanding Clouds from Satellite Images](https://www.kaggle.com/c/understanding_cloud_organization/overview) 에서 볼 수 있는 사진이다. 이 과제는 구름의 type들을 구분하는 것이다. 이 이미지들은 1400 X 2100의 사이즈로 매우 큰 사진들이다. 잘 이해할 수 있듯이, 이미지의 dimension을 너무 줄이면 매 분마다의 패턴과 텍스쳐들이 학습하는데 중요한 요소들인 이 과제에 매우 악영향을 줄 수 있다. 이 때문에 가능한 옵션은 오직 batch size를 줄이는 것 뿐이다.

### Gradient Accumulation

gradient accumulation의 아이디어의 배경은 무식할 정도로 쉽다. SGD처럼 minu-batch가 끝날 때마다 loss와 gradient들을 계산하는 것이지만, 모델의 parameter들을 업데이트하는 것보다는 기다라며 연속적인 batch에 대한 gradient들을 모은다. 그 후 특정한 batch 수를 넘기면 축적한 gradient들에 기반해 parameter들을 업데이트 한다. 이 방법은 매우 많은 이미지들을 가진 mini-batch를 갖는것과 같은 목적을 띈다.

- batch-size가 4개의 이미지고 5번의 step을 거쳤을 경우, 이는 batch-size가 20개의 이미지를 가지고 동작하는 것과 거의 같은 목적을 같게 된다.

### Implementation

pytorch에서 Gradient Accumulation을 구현해 보았다(이 코드는 [번역한 글](https://towardsdatascience.com/gradient-accumulation-overcoming-memory-constraints-in-deep-learning-36d411252d01)에서 발췌하였습니다).

```python
model.zero_grad()                                   # Reset gradients tensors
for i, (inputs, labels) in enumerate(training_set):
    predictions = model(inputs)                     # Forward pass
    loss = loss_function(predictions, labels)       # Compute loss function
    loss = loss / accumulation_steps                # Normalize our loss (if averaged)
    loss.backward()                                 # Backward pass
    if (i+1) % accumulation_steps == 0:             # Wait for several backward steps
        optimizer.step()                            # Now we can do an optimizer step
        model.zero_grad()                           # Reset gradients tensors
        if (i+1) % evaluation_steps == 0:           # Evaluate the model when we...
            evaluate_model()                        # ...have no gradients accumulated
```

우리는 optimizer.step()을 batch들의 수 인 accumulation_steps에 의해 parameter들을 업데이트 한다. 또한 model.zero_grad()는 축적된 gradient들을 초기화시키기 위해 같은 시간에 불려진다.

------
### 출처

- [https://towardsdatascience.com/gradient-accumulation-overcoming-memory-constraints-in-deep-learning-36d411252d01](https://towardsdatascience.com/gradient-accumulation-overcoming-memory-constraints-in-deep-learning-36d411252d01)