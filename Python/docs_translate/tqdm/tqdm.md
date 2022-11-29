# tqdm #
-------------
* for문의 상태를 바 형태로 나타내 주는 라이브러리.
* for문의 in 부분을 tqdm()으로 감싸주면 사용이 가능하다.

```python
from tqdm import tqdm

for i in tqdm(range(9e6)):
    pass
```