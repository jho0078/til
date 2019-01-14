공유폴더    \\192.168.212.40

id : student

pw : ssafy0102



#### 코딩 테스트 단계별 취득

| 단계   | 난이도/ 필수 역량                                      |
| ------ | ------------------------------------------------------ |
| EXPERT |                                                        |
| PRO    |                                                        |
| AD     | 완전검색(재귀함수 개념 파악 필요), DP(Dynamic Program) |
| IM     | 다중 for문을 자유자재로 잘 다룰 수 있는 정도           |



https://swexpertacademy.com/



#### 언어별 실행 방법 차이

- 인터프리터 : 한 줄씩 실행, 느림 (ex. python)


- 컴파일러 : 한 번에 실행



#### 정렬의 종류

선택, 버블, 삽입  : 쉬움, 오래걸림.

퀵, 병합, 카운팅  : 복잡하고 어려움, 실행시간이 짧음.



#### 알고리즘 구현 단계

연필로 설계 → 코딩



#### 시간 복잡도(빅-오 표기법)의 알고리즘 연산 수

O(1)

O(logn) - 이진탐색

O(n) - 순차탐색

O(nlogn) - Quick, Merge, Heap                     P

O(n^2) - 선택, Bubble, 삽입

O(n^3) - 모든 쌍 최단경로

------

O(2^n) - 부분집합(멱집합)                          NP

O(n!) - TSP, 순열



call by value

call by reference



www.swexpertacademy.com 문제 풀이

파이참에서 view_input.txt 파일을 만들어서 input.txt안에 있는 값들을 복사해서 붙여넣기 and 저장

불러오는 방법

```
import sys                              #제출 할 때 위 두 줄은 주석처리
sys.stdin = open("view_input.txt")
T = 10   #test 횟수
for tc in range(T):
    ans = 0
    N =int(input())
    data = list(map(int, input().split()))
    
    
    print("#{} {}".format(tc+1, ans))
```