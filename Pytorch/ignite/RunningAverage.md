# Running Average
-----

## 형태 및 설명

- ignite.metrics.RunningAverage(*src=None, alpha=0.98, output_transform=None, epoch_bound=True, device=None*)
- metric 또는 process함수 결과의 평균을 계산한다.

## Parameters

- src(*Optional[ignite.metrics.metric.Metric]*) - input source : Metric의 요소이거나 None. 이 latter는 process 함수의 결과를 갖는 engine.state.output과 동일하다.
- alpha(*float*) - running average decay factor, 기본값은 0.98
- output_transform(*Optional[Callable]*) - src가 None이고 process 함수의 output과 일치한다면 output을 transform하기 위해 사용되는 함수. 그렇지 않으면 None이어야 한다.
- epoch_bound(*bool*) - 각 epoch 이후 running average 재설정 여부(기본값은 True).
- device(*Optional[Union[str, torch.device]]*) - update들이 축적될 device를 설정한다. running average가 src의 디바이스를 사용하기 때문에 src가 Metric의 요소일 경우 None이어야 한다. 그렇지 않은 경우, 기본값은 CPU이다. metric에서 계산된 값이 tensor일 경우에만 해당된다.

## 예제

```python
from ignite.metrics import RunningAverage

alpha = 0.98
acc_metric = RunningAverage(Accuracy(output_transform=lambda x: [x[1], x[2]]), alpha=alpha)
acc_metric.attach(trainer, 'running_avg_accuracy')

avg_output = RunningAverage(output_transform=lambda x: x[0], alpha=alpha)
avg_output.attach(trainer, 'running_avg_loss')

@trainer.on(Events.ITERATION_COMPLETED)
def log_running_avg_metrics(engine):
    print("running avg accuracy:", engine.state.metrics['running_avg_accuracy'])
    print("running avg loss:", engine.state.metrics['running_avg_loss'])
```
----
### 출처 
* <https://pytorch.org/ignite/metrics.html#ignite.metrics.RunningAverage>