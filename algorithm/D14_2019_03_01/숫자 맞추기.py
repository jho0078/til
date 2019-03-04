import sys
sys.stdin = open("숫자 맞추기.txt")

n = int(input())

first = []
second = []
third = []
score = [0]*n

for i in range(n):
    a, b, c = map(int, input().split())
    first.append(a)
    second.append(b)
    third.append(c)

for i in range(n):
    if first.count(first[i]) == 1:
        score[i] += first[i]

    if second.count(second[i]) == 1:
        score[i] += second[i]

    if third.count(third[i]) == 1:
        score[i] += third[i]

for i in range(n):
    print(score[i])

