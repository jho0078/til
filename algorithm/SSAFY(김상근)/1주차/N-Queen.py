import sys
sys.stdin = open("N-queen_input.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def choose(idx):
    global count

    if idx == N:
        count += 1
        return

    for i in range(N):
        if table[idx][i] == 0:
            marking(idx, i)
            choose(idx+1)

def marking(y, x):
    table[y][x] = 1
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for i in range(8):
        for h in range(1, N+1):
            nx = x + dx[i]*h
            ny = y + dy[i]*h
            if iswall(ny, nx):
                for j in range(1, h):
                    table[y + dy[i]*j][x + dx[i]*j] = 1
                break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [[0 for _ in range(N)] for _ in range(N)]
    # print(table)

    count = 0
    choose(0)
    print("#{} {}".format(tc, count))

    # for x in range(N):
    #     for y in range(N):
    #     queen(0, x)
    #     table[0][x]
    #
    # for y in range(N):
    #     if table
    #