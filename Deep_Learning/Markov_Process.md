# Markov Process #
------------
> **"확률론에서 마르코프 연쇄는 메모리를 갖지 않는 이산 확률 과정이다"**

확률과정은 시간이 진행함에 따라 상태가 확률적으로 변화하는 과정을 의미한다. 확률론적 관점에서 어떠한 확률 분포를 따르는 random varuable이 discrete한 time interval마다 값을 생성하는 것을 말한다. time interval이 discrete하고, 현재의 state가 이전 state에만 영향을 받는 확률 과정이 Markov Process이다.

## Markov Property ##
다른 확률 과정과 구분되는 점은 Markov Property를 갖는 확률 과정이라는 점이다. Markov Property는 과거에 어떤 state에 도달, 거쳐왔든지 다음 state에 갈 확률은 항상 같다는 성질이다. 이 때문에 memoryless property라고도 불린다.
* Pr(S_t+1 = s' | S_0, S_1, . . ., S_t) = Pr(S_t+1 = s' | S_t)
위의 수식은 여러 state를 거쳐오면서 t+1 state에 s'라는 state에 도달할 확률이 직전 t시간의 state에서 state s'로 올 확률이 같다는 것을 표현한다. 즉 0부터 t-1시간까지의 정보는 이미 t시간의 state가 가지고 있다는 가정이 전제되어 있는 것이다.

<img src = "/image/2021_02_17_1.png" width = "60%">

위의 그림은 나(?)의 방학생활을 Markov Chain으로 표현한 것이다. 한 state에서 다른 state로 이동할 확률의 총합은 1을 유지하면서 여러 state들이 연쇄적으로 이어져 있는것을 볼 수 있다. 'sleep' state는 terminal state로 다른 state로의 이동이 없는 마지막 state가 된다. 즉 무한대의 시간이 지나고 나면 terminal state로 수렴하는 것을 stationary distribution이라고 부른다.

## State Transition Probability Matrix ##
state들 간에 이동하는 것을 transition(전이)라고 부른다. 이는 확률로 나타낼 수 있는데 이를 state transition probability matrix라고 한다. 아래에 수식을 적어둔다.

* P_ss' = Pr(S_t+1 = s' | S_t = s)

위의 그림에 나온 transition probability를 행렬로 정리한 것을 state transition probability matrix라고 한다. 아래에 내 방학의 Markov Chain을 state transition probability matrix로 표현해 보았다.

<img src = "/image/2021_02_17_2.png" width = "60%">

----------------
### 출처 ###
* <https://sumniya.tistory.com/3>