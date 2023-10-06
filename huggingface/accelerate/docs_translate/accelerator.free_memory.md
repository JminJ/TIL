# Accelerator.free_memory()
참조된 내부 object를 모두 해제하고 garbage collator를 호출한다. 해당 method는 다른 Model/Optimizer를 학습시킬 시 호출되어야 한다. 또한 Accelerator.step을 0으로 초기화한다.

### Example
```Python
from accelerate import Accelerator

accelerator = Accelerator()
model, optimizer, scheduler = ...
model, optimizer, scheduler = accelerator.prepare(model, optimizer, scheduler)
accelerator.free_memory()

del model, optimizer, scheduler
```

------
### 출처
* https://huggingface.co/docs/accelerate/package_reference/accelerator#accelerate.Accelerator.free_memory