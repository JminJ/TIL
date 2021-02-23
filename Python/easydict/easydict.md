# easydict #
-----
> Easydict 라이브러리는 dict값을 attribute로 사용할 수 있게 해준다.

## Colab에서 사용하게 된 이유
.ipynb파일을 사용할 때 argparse 라이브러리를 사용하는 대신 argument들을 parsing하기 위해 사용해 보았다.

## 예제
```python
import easydict
 
args = easydict.EasyDict({
 
        "batchsize": 100,
 
        "epoch": 20,
 
        "gpu": 0,
 
        "out": "result",
 
        "resume": False,
 
        "unit": 1000
 
})

# 아래에서는 위의 예제를 argparser로 실행할 때를 보여준다.

parser = argparse.ArgumentParser(description='Chainer example: MNIST')
 
parser.add_argument('--batchsize', '-b', type=int, default=100,
 
                    help='Number of images in each mini-batch')
 
parser.add_argument('--epoch', '-e', type=int, default=20,
 
                    help='Number of sweeps over the dataset to train')
 
parser.add_argument('--gpu', '-g', type=int, default=-1,
 
                    help='GPU ID (negative value indicates CPU)')
 
parser.add_argument('--out', '-o', default='result',
 
                    help='Directory to output the result')
 
parser.add_argument('--resume', '-r', default='',
 
                    help='Resume the training from snapshot')
 
parser.add_argument('--unit', '-u', type=int, default=1000,
 
                    help='Number of units')
 
args = parser.parse_args()
```
---------
### 출처 ###
* <https://worthpreading.tistory.com/56 >