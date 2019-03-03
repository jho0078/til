import sys
sys.stdin = open("창고다각형.txt")

N = int(input())

pillars = []
for i in range(N):
    L, H = map(int, input().split())
    pillars.append([L, H])

pillars.sort()

area = 0
height = pillars[0]

idx1 = 0
height = pillars[0][1]
for i in range(1, N):
    if pillars[i][1] >= height:
        area += (pillars[i][0] - pillars[idx1][0])*height
        height = pillars[i][1]
        idx1 = i

pillars = pillars[::-1]

idx2 = 0
height = pillars[0][1]
for i in range(1, N):
    if pillars[i][1] >= height:
        area += -(pillars[i][0] - pillars[idx2][0]) * height
        height = pillars[i][1]
        idx2 = i

pillars = pillars[::-1]
area += (pillars[-idx2-1][0] - pillars[idx1][0] + 1)*pillars[idx1][1]

print(area)

