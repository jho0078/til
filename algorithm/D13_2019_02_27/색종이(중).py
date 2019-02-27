import sys
sys.stdin = open("색종이(중).txt")

def iswall(y, x):
    if y < 0 or x < 0 or y > 99 or x > 99:
        return True
    else:
        return False

n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    y, x = map(int, input().split())

    for j in range(y, y+10):
        for k in range(x, x+10):
            paper[j][k] = 1

# 전체 넓이
area = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            area += 1

# 내부 넓이
inside = 0
for y in range(100):
    for x in range(100):
        dx = [1, -1, 0, 0] # 우, 좌, 하, 상
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if not iswall(ny, nx) and paper[ny][nx] == 0:
                break
        else:
            inside += 1

print(area-inside)

# for i in range(100):
#     print(paper[i])
# count = 0
#
# for i in range(100):
#     for j in range(100):
#         if paper[i][j] == 1:
#             count += 1
#
# print(count)



