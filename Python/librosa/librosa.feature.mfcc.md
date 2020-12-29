# librosa.feature.mfcc #
-------------
## 형태 및 설명 ##
* librosa.feature.mfcc(*y=None, sr=22050, S=None, n_mfcc=20, **kwargs*)
* Mel-frequency cepstral 계수
## Parameters ##
* y (*np.ndarray [shape=(n,)] or None*) - audio 시계열
* sr (*number > 0 [scalar]*) - y의 sampling rate
* S (*np.ndarray [shape=(d, t)] or None*) - log-power Mel spectrogram
* S (*np.ndarray [shape=(d, t)] or None*) - log-power Mel spectrogram
* kwargs (*additional keyword arguments*) - 시계열 input에서 동작하는 경우 melspectrogram에 대한 arguments.

## 예제 ##
```python
import librosa

y, sr = librosa.load(librosa.util.example_audio_file())
librosa.feature.mfcc(y=y, sr=sr)
'''
array([[ -5.229e+02,  -4.944e+02, ...,  -5.229e+02,  -5.229e+02],
       [  7.105e-15,   3.787e+01, ...,  -7.105e-15,  -7.105e-15],
       ...,
       [  1.066e-14,  -7.500e+00, ...,   1.421e-14,   1.421e-14],
       [  3.109e-14,  -5.058e+00, ...,   2.931e-14,   2.931e-14]])
'''
```
--------------
## 출처 ##
* <http://man.hubwiz.com/docset/LibROSA.docset/Contents/Resources/Documents/generated/librosa.feature.mfcc.html>