# Attention is all you need #
--------------
Transformer 모델은 기존의 RNN/CNN 기반으로 구성된 모델들의 단점인 **계산량이 너무 많다는 문제점**을 해결하기 위해 이 방식에서 벗어나 self-attention만을 사용해 학습을 한다는 점이 특별하다.

<img src = '/image/2021_02_18_2.png'>

> * n : sequence의 길이
> * d : 표현 차원
> * k : kernel 사이즈
> * r : neiborhood의 수

기존 방식을 사용하는 모델들보다 얼마나 좋은 성과를 낼 수 있는지 의문이 생길 수 있다. 위 표에서 보여주듯 계산복잡도에서 훨씬 좋은 모습을 보이며 **네트워크의 긴 거리 의존성이 있는 단어 사이의 path 길이면**에서 유리하다.

## Encoder & Decoder ##

<img src = "/image/2021_02_18_3.png" width = "65%">

> 왼쪽이 encoder, 오른쪽이 decoder이다.

Transformer는 위의 Encoder-Decoder stack이 6개가 쌓여있는 구조를 가진다. 각 Encoder와 Decoder는 self-attention 메카니즘을 가지고 있다. 우선 Encoder와 Decode에 대한 설명을 아래에 적어보겠다.

### Encoder ###
* Encoder는 모델에서 처리하는 모든 기본 입력 차원을 512로 지정하였다 (Residual connection을 편하게 하기 위함).  
* 구성은 sub-layer 두 개와, multi-head self-attention,  position-wise fully connected feed-forward network로 이루어져 있다. 
* multi-head self-attention과 position-wise fully connected feed-forward network를 통과하고 sub-layer에서 residual connection을 이용해 준다 (Figure 1에서의 Add 부분). `이때 sub-layer의 output dimention을 embedding dimension과 맞춰준다`. ***즉 residual connection을 해주기 위해 차원을 맞춰줘야 하는 것이다.*** 이후 layer normalization을 적용해 준다.

### Decoder ###
* Encoder처럼 multi-head self-attention, position-wise fully connected feed-forward network를 가지고 있다. `하지만 multi-head self-connection을 수행할 때 Encoder의 결과와 Decoder의 결과값을 함께 계산해준다.`
* Encoder과 다르게 masked multi-head self-attention을 진행한다. `이를 통해 position i보다 이후의 position에 대해 attention을 주지 못하게 해준다.`
* sub-layer에 residual connection과 layer normalization을 수행한다.

## Attention ##

 <img src = '/image/2021_02_18_4.png'>

 위 그림에서 설명하듯 multi-head attention은 Scaled Dot-Product Attention이라고 불리는 attention들이 모여 구성된 형태이다. 따라서 Scaled Dot-Product Attention을 먼저 설명하고 후에 Multi-Head Attention을 설명하겠다.

### Scaled Dot-Product Attention ###

<img src = "/image/2021_02_18_5.png">

> * query : Q(Matrix)
> * key : K(Matrix)
> * value : V(Matrix)
> * d_k : key의 dimension(차원의 수)

Scaled Dot-Prduct Attention은 query, key, value를 각각 Q, K, V라는 인자로 받아 연산을 수행한다. 

우선 query와 모든 key값을 dot product 계산을 한다. 나온 결과값들에 모두 √d_k(루트)값으로 나눠준다. 이후 softmax 함수를 적용시켜 value의 weights들을 구해낸다.

<img src = "/image/2021_02_18_6.png">

* √d_k로 나눠주는 이유는 dot-product 값이 커질 수록 softmax 함수에서 기울기의 변화가 거의 없는 부분으로 가기 때문이다.
* attention의 원리 처럼 softmax를 거친 값에 value를 곱하면 query와 유사한 value일수록(중요한 value) 더 높은 값을 가지게 된다.

### Multi-Head Attention ###

<img src = "/image/2021_02_18_7.png">

다시 한번 설명하자면 Multi-Head Attention은 Scaled Dot-Pruduct Attention을 h번 쌓은 레이어다.  즉 동일한 Q, K, V에 각각 다른 weight matrix W를 곱해주는 것이다. Scaled Dot-Product를 d_h dimension의 key, value, query들로 한 번 실행하지 않고 각각 h번 key, value, query에 다른 학습된 linear projection을 수행한 이유는 이 방식이 더욱 성능이 좋고 병렬구조로 한번에 학습이 가능하다.

> Picture를 수식 및 그림으로 표현
> <img src = "/image/2021_02_18_8.png" width = "65%">
> <img src = "/image/2021_02_18_9.png" width = "65%">

## Self-Attention ##

Encoder의 multi-head attention과 Decoder의 masked multi-head attention, Encoder와 Decoder의 결과값이 만나는 multi-head attention에서 사용되는 self-attention을 참고 사이트를 통해 학습하고 정리해 보겠다.

### Encoder self-attention layer ###

<img src = "/image\2021_02_18_10.png" width = "25%">

Encoder의 multi-head attention layer에서 입력값은 Q, K, V이고 이들은 모두 같은 값을 가진다. 또한 모두 `이전 Encoder의 output을 가지고 오므로 이전 layer의 모든 position에 attention을 적용`해 줄 수 있게 된다. **만약 첫 번째 layer라면 positionnal encoding이 더해진 input embedding이 된다.**

### Decoder self-attention layer ###

<img src = "/image\2021_02_18_11.png" width = "25%">

Encoder의 multi-head attention과는 다르게 masking out을 해준 multi-head attention을 사용하였다. `masking out이 됐다는 말은 i번째 position에 대한 attention을 얻을 때 i번째 이후에 있는 모든 position을 input 값을 -∞으로 설정한 것이다.` **이렇게 하면 i번째  position 이후의 모든 positoin에 attention을 주는 경우가 없을 것이다.**

> masking 그림
> <img src = "/image\2021_02_18_12.png">

* masking out을 적용해주는 이유 : i번째 output을 다시 i+1번째 input으로 사용하는 **auto-regressive한 특성을 유지시키기 위해** masking out을 적용시켜 주었다.

### Encoder-Decoder Attention Layer ###

<img src = "/image\2021_02_18_13.png" width = "45%">

`query들은 masked multi-head attention에서 받고 key, value들은 Encoder에서 받아오게 된다.` 그래서 **Decoder의 모든 position에서 Encoder output의 모든 position에 attention을 줄 수 있게 된다.**

## Position-wise Feed-Forward Networks ##
Encoder와 Decoder의 모든 layer들은 fully connected feed-forward network를 포함하고 있다. 이는 각 position마다 적용되기 때문에 position-wise라고 불린다 (**각 position마다 적용된다는 것은 각 단어마다 적용된다는 뜻**).

Position-wise Feed-Forward Networks는 `두 번의 linear transformation과 한 번의 activation function ReLU`로 이루어져 있다.

<img src = "/image\2021_02_18_14.png">

> **수식 자세한 설명**
> 각 positoin마다 같은 parameter를 사용한다고 했으나 layer마다는 서로 다른 parameter를 사용해 학습한다. 그리고 이는 kernel size가 1인 Convolution Layer를 두 번 사용한 것과 같이 설명할 수 있다.

## Embeddings and Softmax ##
input token과 output token을 dimension이 d_model인 vector로 만들어 주기 위해 learned embedding을 사용한다. 또한 Decoder output를 다음 token의 확률로 바꾸기 위해서도 사용했다.

## Positional Encoding ##
recurrence도 convolution도 아니기 때문에 단어의 순서에 대한 상대적 또는 절대적 위치에 대한 정보를 더해주어야 한다. 따라서 Encoder와 Decoder의 input embedding에 Positonal Encoding을 더해주기로 했다. **Positional Encoding은 d_model과 같은 차원을 가지고 있으므로 Embedding vector와 더해질 수 있다**.

이 작업 과정에서 각각 다른 과정의 sine, cosine function을 사용하게 된다.

<img src = "/image\2021_02_18_15.png">

> **pos, i 설명**
> * pos : positoin
> * i : dimension

Positional Encoding의 각 dimension은 사인파형에 해당한다. 그 파장은 2π 에서 10000  2까지의 기하학적 진행을 형성한다. 

추가적으로 학습된 positional embedding 대신 sinusoidal version을 택한 이유는 **positional embedding 같은 경우에는 training보다 더욱 긴 sequence가 inference시에 입력으로 들어올 때 문제가 발생**하지만 **sinusoidal의 경우에는 const하기에 문제가 되지 않는다. 단지 계산을 더 많이 하기만 하면 될 뿐이다.**

------------
### 출처 & 참고 ###
* <https://pozalabs.github.io/transformer/>
* <https://dalpo0814.tistory.com/49>