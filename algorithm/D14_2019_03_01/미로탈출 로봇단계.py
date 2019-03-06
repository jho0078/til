import sys
sys.stdin = open("미로탈출 로봇단계.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    else:
        False

N = int(input())
table = [list(map(int, list(input()))) for i in range(N)]
rotate = list(map(int, input().split()))

# 1, 2, 3, 4
# 아래, 왼쪽, 위, 오른쪽
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

y = 0
x = 0
idx = 0
count = 0
while True:
    i = rotate[idx] - 1

    nx = x + dx[i]
    ny = y + dy[i]

    if not iswall(ny, nx):
        if table[ny][nx] == 0:
            table[y][x] = 2
            x = nx
            y = ny
            count += 1
        elif table[ny][nx] == 1:
            idx = (idx + 1)%4
        elif table[ny][nx] == 2:
            print(count)
            break

    else:
        idx = (idx + 1) % 4







