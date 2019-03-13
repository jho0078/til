import sys
sys.stdin = open("프로세서 연결하기_input.txt")

# def iswall(y, x):
#     if y < 0 or x < 0 or x >= N or y >= N:
#         return True
#     return False

def compare(y, x):
    if y < len(core) and x < len(core[y]):
        print(core[y][x], y, x)
        compare(y+1, x)
        compare(y, x+1)
    elif x == len()

def connect(y, x, idx):

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        for h in range(1, N):
            nx = x + dx[i]*h
            ny = y + dy[i]*h
            if nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
                if table[ny][nx] != 1:
                    core[idx].append([ny, nx])
                    break
                else:
                    break
            elif table[ny][nx] == 1:
                break


T = int(input())
for tc in range(1, 2):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    core = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if table[i][j] == 1:
                core.append([[i,j]])

    print(core)
    for idx in range(len(core)):
        connect(core[idx][0][0], core[idx][0][1], idx)

    for idx in range(len(core)):
        print(core[idx])

    compare(0, 0)
    # for i in range(len(core)):
    #     for j in range(2, len(core[i]-2)):
    #         abs(core[i][0] - core[i][j][0]) + abs(core[i][1] - core[i][j][1])





