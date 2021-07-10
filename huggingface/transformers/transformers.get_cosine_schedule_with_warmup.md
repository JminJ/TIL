# transformers.get_cosine_schedule_with_warmup
---
## 형태 및 설명

- transformers.get_cosine_schedule_with_warmup(*optimizer: torch.optim.optimizer.Optimizer, num_warmup_steps: int, num_training_steps: int, num_cycles: float = 0.5, last_epoch: int = - 1*)
- 최적화 프로그램에 설정된 초기 lr 사이의 코사인 함수 값을 따라 감소하는 학습률로 schedule을 만든다. 이 기간 동안 최적화 프로그램에 설정된 초기 lr과 0 사이에서 선형으로 증가하는 warmup 기간이 지나면된다.

## Parameters

- optimizer(***Optimizer***) - learning rate를 schedule하기 위한 optimizer.
- num_warmup_steps(***int***) - warmup phase를 위한 step들의 수
- num_training_steps(***int***) - training step들의 전체 수
- num_cycles(***float**, optimal,* defaults to 0.5) - cosine schedule 내의 wave들의 수(default들은 half-cosine을 따라 max value에서 부터 0까지 줄어든다).
- last_epoch(***int**, optimal,* defaults to -1) - training을 재개할 때 마지막 epoch의 index

## Returns

- 적합한 schedule과 **torch.optim.lr_schedulear.LambdaLR**

<img src = '/image/2021_05_03_01.png' width = '80%'>
---

### 출처
* <https://huggingface.co/transformers/main_classes/optimizer_schedules.html>