# pandas.errors.ParserError: field larger than field limit (131072)
----
> csv 파일은 보통 매우 큰 크기를 가지고 있기에 field limit 보다 field가 커서 생기는 에러

## 해결

```python
import sys
import csv

csv.field_size_limit(sys.maxsize) # field size 한계를 늘리는 식으로 에러를 고칠 수 있다
```

---

### 출처

- [https://www.codegrepper.com/code-examples/python/_csv.Error%3A+field+larger+than+field+limit+(131072)](https://www.codegrepper.com/code-examples/python/_csv.Error%3A+field+larger+than+field+limit+%28131072%29)