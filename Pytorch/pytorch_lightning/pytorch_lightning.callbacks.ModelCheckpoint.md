# pytorch_lightning.callbacks.ModelCheckpoint
---
## 형태 및 설명
- pytorch_lightning.callbacks.model_checkpoint.ModelCheckpoint(*dirpath=None, filename=None, monitor=None, verbose=False, save_last=None, save_top_k=None, save_weights_only=False, mode='min', auto_insert_metric_name=True, every_n_train_steps=None, every_n_val_epochs=None, period=None*)
- model을 quantity를 monitoring함으로써 주기적으로 저장한다. LightningModule에서 log() 또는 log_dict()로 log를 기록 된 모든 metric은 monitor key의 후보이다.
- 학습이 끝난 뒤, best_model_path를 사용해 가장 좋은 checkpoint file과 best_model_score에서 score를 얻는다.

## Parameters

- dirpath(Union[str, Path, None]) - model file이 저장 될 directory. 기본적으로 dirpath는 None이며 runtime 동안 Trainer's default_root_dir 또는 weights_save_path argument들에 의해 정해진 location에 적재될 것이다, 그리고 만약 Trainer가 logger를 사용한다면, path는 logger name과 version을 포함하고 있을 것이다.
- filename(Optional[str]) - checkpoint의 filename이다. auto-filled될 named formatting option들을 포함할 수 있다. 기본적으로 filename은 None이며, '{epoch}-{step}'으로 세팅될 것이다.
- monitor(Optional[str]) - 모니터 할 수량. 기본적으로 None이고 오직 마지막 epoch의 checkpoint만을 저장한다.
- verbose(bool) - verbosity mode. 기본값 : False.
- save_last(Optional[bool]) - True일 경우, 언제나 마지막 epoch의 model을 last.ckpt 파일에 저장한다. 기본값 : None.
- save_top_k(Optional[int]) - 만약 save_top_k == k일 경우, 모니터 된 quantity들에 따라 최고의 k model이 저장된다. save_top_k == 0일 경우 모든 model들이 저장되지 않고, save_top_k == -1일 경우, 모든 model들은 저장된다. monitor들은 모든 period epoch들에서 체크된다. 만약 save_top_k가 2 이상이고 callback이 epoch 내에서 여러번 호출됬다면 저장된 file의 이름은 v1부터 시작하는 version count가 더해진다.
- mode(str) - {min, max} 중 하나. 만약 save_top ≠ 0이라면, 현재 저장된 file을 덮어쓰는 것을 결정은 모니터 될 수량의 maximization 또는 minimization을 기준으로 만들어진다. 'val_acc'를 위한 결정은 'max'여야 하고, 'val_loss'를 위한 것은 'min'이어야 한다.
- save_weights_only(bool) - True일 시, model의 weight들 만이 (model.save.weights(filepath))에 저장된다, True가 아닐 시는 전체 model이 (model.save(filepath))에 저장된다.
- every_n_train_steps(Optional[int]) - checkpoint들 사이에서 training step의 수. every_n_train_steps == None or every_n_train_steps == 0이라면, training 동안 저장을 skip하며 every_n_train_steps = 0로 세팅한다. 이 값은 None non-negative이어야 한다. 이는 every_n_val_epochs와 상호 배타적이어야 한다.
- every_n_val_epochs(Optional[int]) - checkpoint들 사이에서 validation epoch들의 수. every_n_val_epochs == None or every_n_val_epochs == 0이라면, validation에서 저장을 skip하고 every_n_val_epochs = 0으로 세팅한다. 이 값은 None non-negative이어야 한다. 이는 every_n_train_epochs와 상호 배타적이어야 한다. ModelCheckpoint(..., every_n_val_epochs=V)와 Trainer(max_epochs=N, check_val_every_n_epoch=M)의 setting은 every_n_val_epochs와 check_val_every_n_epoch의 두 값이 E를 균등하게 나누는 0<E≤N에서 checkpoint만 저장한다.
- period(Optional[int]) - checkpoint 사이의 간격(numer of epochs)

## 예제

```python
>>> from pytorch_lightning import Trainer
>>> from pytorch_lightning.callbacks import ModelCheckpoint

# saves checkpoints to 'my/path/' at every epoch
>>> checkpoint_callback = ModelCheckpoint(dirpath='my/path/')
>>> trainer = Trainer(callbacks=[checkpoint_callback])

# save epoch and val_loss in name
# saves a file like: my/path/sample-mnist-epoch=02-val_loss=0.32.ckpt
>>> checkpoint_callback = ModelCheckpoint(
...     monitor='val_loss',
...     dirpath='my/path/',
...     filename='sample-mnist-{epoch:02d}-{val_loss:.2f}'
... )

# save epoch and val_loss in name, but specify the formatting yourself (e.g. to avoid problems with Tensorboard
# or Neptune, due to the presence of characters like '=' or '/')
# saves a file like: my/path/sample-mnist-epoch02-val_loss0.32.ckpt
>>> checkpoint_callback = ModelCheckpoint(
...     monitor='val/loss',
...     dirpath='my/path/',
...     filename='sample-mnist-epoch{epoch:02d}-val_loss{val/loss:.2f}',
...     auto_insert_metric_name=False
... )

# retrieve the best checkpoint after training
checkpoint_callback = ModelCheckpoint(dirpath='my/path/')
trainer = Trainer(callbacks=[checkpoint_callback])
model = ...
trainer.fit(model)
checkpoint_callback.best_model_path
```

---

### 출처

- [https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.callbacks.model_checkpoint.html#pytorch_lightning.callbacks.model_checkpoint.ModelCheckpoint](https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.callbacks.model_checkpoint.html#pytorch_lightning.callbacks.model_checkpoint.ModelCheckpoint)