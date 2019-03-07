import sys
sys.stdin = open("미로_input.txt")

def iswall():
    if x < 0 or y < 0 or x >= N or y >= N:
        return True
    else:
        return False

def find():
    global N
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                return i, j

def maze(y, x):
    global flag
    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not iswall(ny, nx):
            if data[ny][nx] == 3:
                flag = 1
                return
            if data[ny][nx] == 0:
                x = nx
                y = ny
                maze(ny, nx)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, list(input()))) for i in range(N)]
    y, x = find()
    flag = 0
    maze(y, x)
    print("#{} {}".format(tc, flag))




