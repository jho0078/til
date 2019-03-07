import sys
sys.stdin = open("Ladder1_input.txt")

def move(y, x):
    # 좌, 우, 위
    dx = [1, -1, 0]
    dy = [0, 0, -1]

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if not iswall(ny, nx):
            if table[ny][nx] == 1:
                if ny == 0:
                    table[ny][nx] = 3
                    return
                else:
                    table[y][x] = 3
                    x = nx
                    y = ny
                    move(ny, nx)

def iswall(y, x):
    if x < 0 or y < 0 or x >= 100 or y >= 100:
        return True

T = 10
for tc in range(1, T+1):
    num = int(input())
    table = [list(map(int, input().split())) for i in range(100)]

    for i in range(100):
        if table[99][i] == 2:
            x = i
            break

    move(99, x)
    for i in range(100):
        if table[0][i] == 3:
            print("#{} {}".format(tc, i))
