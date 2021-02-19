# on #
------
## 형태 및 설명 ##
* on(*event_name: Any, *args: Any, **kwargs: Any*) → Callable

## Parameters ##

- event_name - handler에 추가될 event. 가능한 event들은 Events 또는 register_events()를 통해 추가된 event_name로부터 와야 한다.
- *args - handler를 거쳐야 하는 선택적 args.
- *kwargs - handler를 거쳐야 하는 선택적 keyword args.

## 예제 ##
```python 
engine = Engine(process_function)

@engine.on(Events.EPOCH_COMPLETED)
def print_epoch():
    print(f"Epoch: {engine.state.epoch}")

@engine.on(Events.EPOCH_COMPLETED | Events.COMPLETED)
def execute_something():
    # do some thing not related to engine
    pass
```

----------
### 출처 ###
* <https://pytorch.org/ignite/engine.html>