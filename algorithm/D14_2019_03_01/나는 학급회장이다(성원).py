import sys
sys.stdin = open("나는 학급회장이다.txt")

N = int(input())
input_list = [list(map(int, input().split())) for _ in range(N)]
input_list = list(zip(*input_list))
# 입력값
# [[3, 1, 2], [2, 3, 1], [3, 1, 2], [1, 2, 3], [3, 1, 2], [1, 2, 3]]

# zip 각 후보의 점수리스트
# [(3, 2, 3, 1, 3, 1), (1, 3, 1, 2, 1, 2), (2, 1, 2, 3, 2, 3)]
score = [0] * 3

# 각 후보의 점수 합, 3의 갯수, 2의 갯수 를 요소로 같는 리스트 생성
for i in range(3):
    score[i] = [sum(input_list[i]), input_list[i].count(3), input_list[i].count(2)]

# score = [[13, 3, 1], [10, 1, 2], [13, 2, 3]]
# max함수를 사용하면 리스트의 첫번째 값을 먼저 비교한다. [13, 3, 1] [13, 2, 3]
# 첫 번째 값이 같다면 두 번째 값을 비교하여 더 큰 값을 가지는 리스트를 반환한다.
max_score = max(score)

if score.count(max_score) == 1:
    max_idx = score.index(max(score))
    print('{} {}'.format(max_idx+1, max_score[0]))
else:
    print("0 {}".format(max_score[0]))