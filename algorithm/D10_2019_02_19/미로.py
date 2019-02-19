import sys
sys.stdin = open("미로_input.txt")

# 벽 판별
def iswall(y, x):
    if y < 0 or y > N-1 or x < 0 or x > N-1:
        return False
    else:
        return True

def maze(y, x):
    global flag

    # 위, 좌, 우, 아래 순으로 탐색
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if iswall(ny, nx) and miro[ny][nx] == 3:
            flag = 1
            return

        elif iswall(ny, nx) and miro[ny][nx] == 0:
            miro[y][x] = 1
            maze(ny, nx)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, list(input()))) for _ in range(N)]
    flag = 0

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                y = i
                x = j

    maze(y, x)


    print("#{} {}".format(tc, flag))




