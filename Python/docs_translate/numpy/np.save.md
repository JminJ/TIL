# np.save #
----------------
## 형태 및 설명 ##
* numpy.save(file, arr, allow_pickle = True, fix_imports = True)
* Numpy의 .npy format을 통해 array를 binary 파일로 저장한다.
## Parameters ##
* file(*file, str or pathlib.Path*) - 저장될 data의 File 또는 filename. 만약 file이 file-object일 경우 이름은 바뀌지 않는다. 하지만 file이 string 또는 Path일 경우 filename에 .npy extension이 존재하지 않을 경우 더해질 것이다. 
* arr(*array_like*) - 저장될 array 데이터.
* allow_pickle(*bool, optional*) - Python pickle을 사용해 object array를 저장하는 것을 허용한다. pickle을 허용하지 않는 이유는 보안성과 이식성 때문이다. 기본값은 True.
* fix_imports(*bool, optional*) - Python 3의 object array에 있는 object를 Python 2 호환 방식으로 pickle된 경우에만 유용합니다. fix_imports가 True이면 pickle은 새로운 Python 3 이름을 Python 2에 사용된 이전 모듈 이름에 매핑하여 pickle 데이터 스트림을 Python 2로 읽을 수 있도록 시도합니다.
## 예제 ##
```python
import numpy as np

x = np.arange(10)
np.save(outfile, x)

np.load(outfile)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
---------------
## 출처 ##
* <https://numpy.org/doc/stable/reference/generated/numpy.save.html>