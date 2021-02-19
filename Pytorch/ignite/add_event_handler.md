# add_event_handler #
------------
## 형태 및 설명 ##
* add_event_handler(*event_name: Any, handler: Callable, *args: Any, **kwargs: Any*) → ignite.engine.events.RemovableEventHandle
* 선택한 event가 실행될 때 실행될 event handler가 추가된다.

## Parameters ##
* event_name - handler에 추가될 event 또는 event의 list. 가능한 event들은 Events 또는 `reguster_events()`에 의해 추가된 `event_name`로부터 온다.
* handler(callable) - 발동되어야 할 callable event handler. 그것의 signature에는 어떠한 제약도 없다. 첫 번째 인자는 선택적으로 engine일 수 있으며, Engine object, handler가 바인딩 되어 있다.
* *args - handler을 거쳐야 하는 선택적 args.
* *kwargs - handler을 거쳐야 하는 선택적 keyword args.

## Returns ##
* handler에서 삭제가 가능한 `RemovableEventHandle`.

## 예제 ##
```python
engine = Engine(process_function)

def print_epoch(engine):
    print(f"Epoch: {engine.state.epoch}")

engine.add_event_handler(Events.EPOCH_COMPLETED, print_epoch)

events_list = Events.EPOCH_COMPLETED | Events.COMPLETED

def execute_something():
    # do some thing not related to engine
    pass

engine.add_event_handler(events_list, execute_something)
```

------------------
### 출처 ###
* <https://pytorch.org/ignite/engine.html>