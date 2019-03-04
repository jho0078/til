import sys
sys.stdin = open("나는 학급회장이다.txt")

n = int(input())
first = []
second = []
third = []
emptylist = []

for i in range(n):
    a, b, c = map(int, input().split())
    first.append(a)
    second.append(b)
    third.append(c)

max_score = max(sum(first), sum(second), sum(third))
sum_list = [sum(first), sum(second), sum(third)]

max_score = 0
max_idx = []
for i in range(3):
    if sum_list[i] > max_score:
        max_score = sum_list[i]
        max_idx = []
        max_idx.append(i)

    elif sum_list[i] == max_score:
        max_idx.append(i)

print(max_idx, max_score)
if len(max_idx) == 1:
    print(max_idx[0], max_score)

else:
    data = [first, second, third]
    for i in range(len(max_idx)):
        for j in range(len(data[]))



