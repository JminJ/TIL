# GCN
---
GCN(Graph Convolution Network)은 Graph network에 CNN의 Convolution 개념을 적용한 방식이다.  따라서 CNN의 특징이 GCN에서도 나타나게 된다.

- CNN의 특징
    - 특징 1 : Weight sharing
    - 특징 2 : Learn local feature

 이 특징들이 어떻게 나타나는 지 알기 위해선 몇 가지 해야 하는 일이 있다. 우선 Graph data를 표현하기 위해 Adjacency matrix(노드 연결 관계) A, Feature matrix(노드의 속성들) H를 만든다.  

- 설명에 사용 될 그래프

    <img src = '/image/2021_05_05_01.png'>

- 그래프의 A, H

    <img src = '/image/2021_05_05_02.png'>

    - A의 0번째 행을 설명하자면 그래프에서 노드 0와 연결된 노드가 1, 4이기에 자신을 포함한 0, 1, 4 열이 1으로 표기된 것이다.
    - H의 열의 개수는 데이터의 feature 개수와 같다.

Hidden state는 W행렬과 b에 의해 업데이트 되는데 이 과정에서 CNN의 특징이 나타난다.

- Hidden state 업데이트 식

    <img src = '/image/2021_05_05_03.png'>

- Weight sharing : 각 H(l) state는 모두 동일한 W(l)를 곱해주는 것을 볼 수 있다. 이것이 weight를 공유하며 연산한다는 의미를 보인다.
- Learn local feature : 노드 1의 경우는 2, 3, 4 노드와 인접하고 있으므로 H1 state는 H1, H2, H3, H4에 의해서만 영향을 받아야 한다.

- 일반화 된 Hidden state 업데이트 식

    <img src = '/image/2021_05_05_04.png'>

    일반화는 A를 곱해주기만 하면 끝나게 된다. 하지만 A를 곱해주는 이유는 꽤나 복잡하다고 생각한다(주관적 입니다).

    <img src = '/image/2021_05_05_05.png'>

     각각의 H state는 자신과 연결된 state에 의해서만 영향을 받는다. 하지만 위 그림에서의 H*W 행렬은 column N이 모든 H state들의 N번째 weight filter를 곱했을 때 나온 값들이다. 하지만 새로 업데이트되는 H state는 자신과 관련이 있는 state와 같은 weight filter를 곱해 나온 모든 값들을 더해야 한다.

    <img src = '/image/2021_05_05_06.png'>

    따라서 관계에 대한 정보를 담고 있는 A행렬을 H*W 행렬에 곱해주게 되면 우리가 원하는 H state를 얻을 수 있게 된다.

    ### ReadOut

     마치 CNN에서 Fully-Connected layer를 통해 flatten을 시키고 softmax를 통해 분류 작업을 하는 것 처럼 GCN에서도 readout-layer라는 것이 존재한다.

    - GCN 모델 구조

        <img src = '/image/2021_05_05_07.png'>

    그렇다면 Readout-layer가 필요한 이유는 무엇일까, 그 이유는 같은 네트워크를 가지고 있는 그래프 일지라도 Adjacency matrix가 다를 수 있기 때문이다. 즉 노드간의 edge(연결) 정보가 같아도 회전, 대칭에 의해 행렬 내 값의 순서가 달라질 수 있기 때문이다.

    - Readout-layer가 필요한 이유

        <img src = '/image/2021_05_05_08.png'>

출처 : [https://ganghee-lee.tistory.com/27](https://ganghee-lee.tistory.com/27)