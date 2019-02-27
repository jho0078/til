import sys
sys.stdin = open("색종이(중).txt")

n = int(input())
paper = [[0 for _ in range(102)] for _ in range(102)]

for i in range(n):
    y, x = map(int, input().split())

    for j in range(y+1, y+11):
        for k in range(x+1, x+11):
            paper[j][k] = 1

for i in range(100):
    print(paper[i])
length = 0
for y in range(102):
    for x in range(102):
        if paper[y][x] == 1:
            dx = [1, -1, 0, 0] # 우, 좌, 하, 상
            dy = [0, 0, 1, -1]
            for i in range(4):
                nx = x +dx[i]
                ny = y +dy[i]
                if paper[ny][nx] == 0:
                    length += 1

print(length)