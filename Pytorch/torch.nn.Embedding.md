# torch.nn.Embedding #
-------------------
## 형태 ##
* torch.nn.Embedding(*num_embeddings: int, embedding_dim: int, padding_idx: Optional[int] = None, max_norm: Optional[float] = None, norm_type: float = 2.0, scale_grad_by_freq: bool = False, sparse: bool = False, _weight: Optional[torch.Tensor] = None*)

## Parameter 설명 ##
* num_embeddings(int) - embeddings된 dictionary 의 사이즈
* embedding_dim(int) - 각 embedding vector의 사이즈
* padding_idx(int, optional) - 지정된 경우, padding_idx로 주어진 embedding vector를 만났을 때 0으로 초기화 한다.
* padding_idx(int, optional) - 지정된 경우, padding_idx로 주어진 embedding vector를 만났을 때 0으로 초기화 한다.
* norm_type(float, optional) - max_norm 옵션에 맞게 계산할 수 있도록 p-norm의 p를 지정한다.(기본값은 2)
* scale_grad_by_freq(boolean, optional) - 주어진 경우, gradient를 mini-batch에 있는 단어 빈도의 역순으로 조정한다.(기본값은 false)
* sparse(bool, optional) - 만약 True인 경우, gradient w.r.t weight matrix는 sparse tensor가 된다.

## 예제 ##
```python
import torch.nn

embedding = nn.Embedding(10, 3)
input = torch.LongTensor([[1,2,4,5], [4,3,2,9]])
embedding(input)
/*tensor([[[-0.0251, -1.6902,  0.7172],
         [-0.6431,  0.0748,  0.6969],
         [ 1.4970,  1.3448, -0.9685],
         [-0.3677, -2.7265, -0.1685]],

        [[ 1.4970,  1.3448, -0.9685],
         [ 0.4362, -0.4004,  0.9400],
         [-0.6431,  0.0748,  0.6969],
         [ 0.9124, -2.3616,  1.1151]]])*/

embedding = nn.Embedding(10, 3, padding_idx=0)
input = torch.LongTensor([[0,2,0,5]])
embedding(input)
/* tensor([[[ 0.0000,  0.0000,  0.0000],
         [ 0.1535, -2.0309,  0.9315],
         [ 0.0000,  0.0000,  0.0000],
         [-0.1655,  0.9897,  0.0635]]]) */
```
----------------
## 출처 ##
* <https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html>