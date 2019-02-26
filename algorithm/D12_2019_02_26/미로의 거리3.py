import sys
sys.stdin = open("미로의 거리_input.txt")

def iswall(y, x):
    global N
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def maze():

    while y_queue:
        y = y_queue.pop(0)
        x = x_queue.pop(0)

        dy = [-1, 0, 0, 1]
        dx = [0, 1, -1, 0]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not iswall(ny, nx):
                if data[ny][nx] == 3:
                    return data[y][x]//2 - 1
                elif data[ny][nx] == 0:
                    y_queue.append(ny)
                    x_queue.append(nx)
                    data[ny][nx] = data[y][x] + 2

        if not y_queue:
            return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                y_start = i
                x_start = j

    y_queue = [y_start]
    x_queue = [x_start]
    print("#{} {}".format(tc, maze()))