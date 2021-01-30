# RNN과 batch_first의 관계 #
--------------------------------------

## batch_first? ##
RNN에 feed 해줄 input 차원의 형태가 기존 [seq_len, batch_size, input_size]의 형태에서 [batch_size, seq_len, input_size]가 되는 것을 말한다.
## hidden_state ##
그렇다면 hidden state의 차원 형태 또한 변경되어야 할까?? 답은 그렇지 않다. hidden state 차원의 형태는 기존 [num_layers * num_directions, batch, hidden_state]로 동일하게 나타난다.***즉 batch_first = True 유무와 무관하다.***

------------------
### 출처 ###
* <https://seducinghyeok.tistory.com/8>