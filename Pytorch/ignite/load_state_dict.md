# load_state_dict #
------
## 설명 ##
state_dict로부터 engine을 세팅한다.

State dictionary는 key를 포함하고 있어야 한다: iteration 또는 epoch 그리고 max_epochs, epoch_length. 만약 engine_dict_user_keys가 key를 포함하고 있다면, state dictionary에도 있어야 한다. Iteration과 epoch 값은 0이 base다: 첫 번째 iteration 또는 epoch는 0이다.

이 방법은 사용자가 추가한 custom attributs를 삭제하지 않는다.

## Parameters ##
* state_dict(*Mapping*) - parameter를 포함하는 dict

## 예제 ##
```python
# Restore from the 4rd epoch
state_dict = {"epoch": 3, "max_epochs": 100, "epoch_length": len(data_loader)}
# or 500th iteration
# state_dict = {"iteration": 499, "max_epochs": 100, "epoch_length": len(data_loader)}

trainer = Engine(...)
trainer.load_state_dict(state_dict)
trainer.run(data)
```
------------
### 출처 ###
* <https://pytorch.org/ignite/engine.html>