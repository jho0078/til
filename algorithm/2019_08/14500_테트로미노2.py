def sol(y, x):

    dy = [0, -1, 1, -1, 1, -1, 1, 0]
    dx = [-1, 0, 0, 0, 0, 0, 0, 1]

    k = 0
    while k < 2:
        if k == 0 and x > M - 3:
            continue
        if k == 1 and y > N - 3:
            continue

        if k == 0:
            result = A[y][x] + A[y][x + 1] + A[y][x + 2]
        else:
            result = A[y][x] + A[y + 1][x] + A[y + 2][x]

        for i in range(8):
            ny, nx = y + dy, x + dx
            if 2 < i <= 4:
                if k == 0:
                    nx += 1
                else:
                    ny += 1
            elif 4 < i < 8:
                if k == 0:
                    nx += 2
                else:
                    ny += 2

            if -1 < ny < N and -1 < nx < M:
                if result + A[ny][nx] > MAX:
                    MAX = result + A[ny][nx]

        tmp = dy[:]
        dy = dx[:]
        dx = tmp[:]
        k += 1

def square(y,x):
    global MAX

    if x > M - 2 or y > N - 2:
        return

    result = 0
    for i in range(2):
        for j in range(2):
            result += A[y+i][x+j]
    if result > MAX:
        MAX = result

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
MAX = 0

for i in range(N):
    for j in range(M):
        sol(i, j)
        square(i, j)
