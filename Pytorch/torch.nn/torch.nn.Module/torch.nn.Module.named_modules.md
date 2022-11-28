# torch.nn.Module.named_modules
## 형태 및 설명
* torch.nn.Module.named_modules(*memo=None, prefix='', remove_duplicate=True*)
* network를 구성하는 모든 module들의 name, module을 반환하는 iterator를 return한다.

## Parameters 
* memo (*Optional[Set[Module]]*) - 이미 result에 더해진 module들의 set 저장할 memo
* prefix (*str*) - module의 이름에 더해질 prefix
* remove_duplicate (*bool*) - result에 복사된 module은 삭제할 것인지 아닌지
## Yields
* (str, Module) – 이름과 module의 Tuple
```
Note) 복사된 module들은 한번만 return된다. 아래 예제에서 l은 오직 한 번만 return될 것이다. 
```

## Example
```python
>>> l = nn.Linear(2, 2)
>>> net = nn.Sequential(l, l)
>>> for idx, m in enumerate(net.named_modules()):
...     print(idx, '->', m)

# 0 -> ('', Sequential(
#   (0): Linear(in_features=2, out_features=2, bias=True)
#   (1): Linear(in_features=2, out_features=2, bias=True)
# ))
# 1 -> ('0', Linear(in_features=2, out_features=2, bias=True))
```