import sys
sys.stdin = open("미로의 거리_input.txt")

def iswall(y, x):
    global N
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def allzero():
    for i in range(N):
        for j in range(N):
            if queue[i][j]:
                return False
    return True

def pop1():
    for i in range(N):
        for j in range(N):
            if queue[i][j] == 1:
                queue[i][j] = 0
                return i, j

def maze():
    global y_start, x_start

    queue[y_start][x_start] = 1

    while not allzero():
        y, x = pop1()

        dy = [-1, 0, 0, 1]
        dx = [0, 1, -1, 0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not iswall(ny, nx):
                if data[ny][nx] == 3:
                    return data[y][x]
                elif data[ny][nx] == 0:
                    queue[y][x] = 1
                    data[ny][nx] = data[y][x] + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, list(input()))) for _ in range(N)]
    # for i in range(N):
    #     print(data[i])
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                y_start = i
                x_start = j

    queue = [[0 for _ in range(N)] for _ in range(N)]
    print(maze())


