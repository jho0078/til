import sys
sys.stdin = open("프로세서 연결하기_input.txt")

def find(y, x):
    global idx, count, length, xys
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        for h in range(1, N):
            nx = x + dx[i] * h
            ny = y + dy[i] * h

            if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                if table[ny][nx] != 1:
                    for j in range(1, h):
                        table[y + dy[i] * j][x + dx[i] * j] = 2
                    count += 1
                    length += h
                    xys.append([y, x, h])
                    break
            elif table[ny][nx] == 1 or table[ny][nx] == 2:
                break

        idx += 1
        if idx < len(core):
            y = core[idx][0]
            x = core[idx][1]
            find(y, x)
        else:
            if count != 0:
                cores.append([count, length, xys])
                length = 0
                count = 0
                xys = []

T = int(input())
for tc in range(1, 2):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    core = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if table[i][j] == 1:
                core.append([i, j])
    xys = []
    cores = []
    length = 0
    count = 0
    idx = 0
    print(core)
    find(core[idx][0], core[idx][1])
    cores.sort(reverse=True)
    print(cores)





