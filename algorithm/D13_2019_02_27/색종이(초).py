import sys
sys.stdin = open("색종이(초).txt")

n = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for k in range(x, x+10):
            paper[j][k] = 1

result = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            result += 1

print(result)