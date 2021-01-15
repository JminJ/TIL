# Principle of Counting2 #
-------------------
## 배워볼 것 ##
* permutation(순열)
* counting principle 2

## 정리 ##
> ***permutation***

n개의 구분이 가능한 주체 또는 객체를 순서대로 나열할 때의 총 방법의 수. 즉 서로 다른 n가의 문자를 나열하는 방법과 동일하다.

![image1](/image/2021_01_15_1.png)

> ***counting principle 2***

어떠한 n개의 객체가 주어졌을 때 이것을 나열할 시 n1, n2, ... nm개의 완전해 똑같은 객체가 있는 것과 같다.

![image2](/image/2021_01_15_2.png)

## 예제 ##
> **x, y, z의 3개의 문자를 나열하는 가지 수는? (permutation)**

이 문제에서 n은 문자의 개수를 의미하므로 n = 3, 총 가지수는 3!이 된다.
이를 확률용어로 *permutation of n* 라고 부른다.

> **bookmark라는 단어를 나열하는 방법의 수는? (counting principle 2)**

전체 나열 가능한 순열은 8개의 객체가 있으므로 (8)!가 된다.
이 문자들 중 구분이 가지 않는 같은 단어를 찾으면 o, k가 각각 2개씩 있으므로 최종적인 답은 (8)! / (2)!(2)!가 된다.

--------------
## 출처 ##
* <https://m.blog.naver.com/rlakk11/60155204164>