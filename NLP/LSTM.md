# LSTM #
--------

> LSTM은 기존 RNN의 고질적인 Gradient Vanishing 문제를 극복하기 위해 만들어 졌다.

## LSTM의 기본 구조

<img src = "/image/2021_02_25_01.png" width = "65%">

LSTM은 RNN의 hidden-state에 cell-state를 추가한 구조이다. 아래에는 LSTM의 수식을 정리해 놓는다. ⊙는 Hadamard product 연산자는 요소별 곱셈을 의미한다.

<img src = "/image/2021_02_25_02.png" width = "65%">

- f_t : forget gate로 '과거의 정보를 잊기 위한 게이트'다. h_t-1과 x_t를 받아서 시그모이드를 취해준 값이 forget gate가 내보내는 값이 된다.
- i_t : input gate로 '현재 정보를 기억하기 위한 게이트'다. h_t-1과 x_t를 받아서 시그모이드를 취하고, 또 같은 입력으로 하이퍼 볼릭 탄젠트를 취한 다음 Hadamard product 연산을 한 값이 input gate가 내보내는 값이 된다.

> **f_t, i_t, c_t**
>> <img src = "/image/2021_02_25_03.png" width = "50%">
>> <img src = "/image/2021_02_25_04.png" width = "50%">

-----------
### 출처 ###
* https://ratsgo.github.io/natural language processing/2017/03/09/rnnlstm/