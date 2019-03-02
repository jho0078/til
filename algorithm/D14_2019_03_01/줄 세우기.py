import sys
sys.stdin = open("줄 세우기.txt")

n = int(input())
data = list(map(int, input().split()))

line = []
for i in range(n):
    if data[i] == 0:
        line.append(i+1)
    else:
        line.insert(-data[i], i+1)

print(' '.join(map(str, line)))

