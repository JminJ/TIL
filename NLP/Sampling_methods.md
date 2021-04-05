# Sampling methods
-----
## Sampling

 Beam search, Greedy search의 경우 문장에 들어가는 단어들을 확률이 높은 쪽으로만 찾아가다 보니 쉽게 예측이 가능하고 신박하지 않다는 단점이 있다. 따라서 사람처럼 신박한 단어를 사용하는 문장을 만들고자 하였는데 이때 추가된 성질이 random성이다.

 **Sampling은 조건부 확률 분포에 따라 무작위하게 다음 단어를 선택하는 방법이다**. 수식은 아래와 같다.

<img src = '/image\2021_04_05_01.png'>

[sampling에 대한 자세한 자료](https://huggingface.co/blog/how-to-generate?fbclid=IwAR2BZ4BNG0PbOvS5QaPLE0L3lx7_GOy_ePVu4X1LyTktQo-nLEPr7eht1O0)

## Top-k sampling

Top-k sampling은 다음 단어로 올 수 있는 후보들 중 상위 k개의 요소들만 고려하는 방식을 말한다. 아래 그림을 통해 예시를 보고 추가적인 이해를 해보자.

<img src = '/image\2021_04_05_02.png'>

이 예시는 k가 일 때를 가정했다. k가 이기에 두 분포에서 나타나는 후보의 개수는 6개 씩이다. 이 방법은 상당히 간단하며 성능이 우수했기에 많이 사용되었다. 하지만 이 방식에도 단점이 존재했는데 왼쪽의 분포는 10개의 모든 후보들이 비슷한 분포를 가지고 있기에 "people", "house" 또한 좋은 후보가 될 수 있으나 선택되지 못했고 오른쪽의 분포에서는 "stops", "down", "a"는 매우 값이 낮지만 k의 개수가 6개라는 점 때문에 후보로 채택된 것을 볼 수 있다. 이 방법은 모델의 창의성을 지나치게 저하하면서도 모델이 이상한 단어를 샘플링할 위험이 있는 것이다.

## Top-p sampling

Top-k sampling의 단점을 보완하는 아이디어인 Top-p sampling을 설명하겠다. 

<img src = '/image\2021_04_05_03.png'>

아까 그림과 비슷하나 말하고자 하는 이야기는 다른 그림이다. 달라진 점은 후보들의 개수다. Top-k sampling은 고정된 개수의 후보만을 고려했지만 Top-p sampling은 확률 분포들의 크기에 따라 동적으로 개수가 달라진다. p를 92%로 지정하고 분포들의 합이 92%가 넘는 최소한의 후보들을 고르고 나머지 후보들은 사용하지 않는다. 

분포를 조금 더 자세히 설명하면 왼쪽의 경우 "nice"..."house"까지의 분포 합이 94%이기에 9개의 후보가 선택된 것이고 오른쪽의 경우 "drives"..."turns"까지 분포의 합이 97%이기에 3개의 후보를 선택한 것이다.

---

### 출처

- [https://huggingface.co/blog/how-to-generate?fbclid=IwAR2BZ4BNG0PbOvS5QaPLE0L3lx7_GOy_ePVu4X1LyTktQo-nLEPr7eht1O0](https://huggingface.co/blog/how-to-generate?fbclid=IwAR2BZ4BNG0PbOvS5QaPLE0L3lx7_GOy_ePVu4X1LyTktQo-nLEPr7eht1O0)
- [https://littlefoxdiary.tistory.com/46](https://littlefoxdiary.tistory.com/46)