# End-to-End Learning #
-------------------
우리가 어떤 문제를 해결하기 위해서는 여러가지 스텝을 거치며 나아가야 한다. 이 end-to-end learning 은 이 스텝들을 하나의 신경망으로 재배치 해나가는 과정을 의밓사고 있다.

기존의 파이프라인을 구축하는 방식은 데이터의 크기가 적을 때 유용하고 이 end-to-end 방식은 데이터의 크기가 클 때 효율적이라고 한다.

![picture](/image/2021_01_10_1.png)

위 사진은 바이두 회사에서 얼굴 인식 문제를 푼 방식이다. 대신 두 문제로 나눈 다음 end-to-end learning을 진행한다. 하나는 사진에서 얼굴 부분만 인식하는 부분, 나머지 하나는 그 얼굴이 보유하고 있는 사람들과 일치하는지를 판별해주는 부분이다.

----------------
## 출처 ##
* <https://pongdangstory.tistory.com/424>
* <https://talkingaboutme.tistory.com/entry/MLY-end-to-end-learning의-예?category=538748>