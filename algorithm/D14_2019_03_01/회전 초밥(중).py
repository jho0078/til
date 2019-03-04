import sys
sys.stdin = open("회전 초밥(중).txt")

N, d, k, C = map(int, input().split())

data = []
for i in range(N):
    data.append(int(input()))

dataplus = data + data[:k-1]

result = 0
max_counts = 0

for i in range(N):
    p = 1
    for j in range(k):
        if dataplus[i:i+k].count(dataplus[i:i+k][j]) != 1:
            p = 0
            break

    print(dataplus[i:i+k])
    if C in dataplus[i:i+k]:
        if len(set(dataplus[i:i + k])) > max_counts:
            max_counts = len(set(dataplus[i:i + k]))
    else:
        if len(set(dataplus[i:i + k])) + 1 > max_counts:
            max_counts = len(set(dataplus[i:i + k])) + 1

    if p == 1:
        if C in dataplus[i:i+k]:
            result = k
        else:
            result = k+1
            break

if result != 0:
    print(result)
else:
    print(max_counts)

