import sys
sys.stdin = open("등산로 조성_input.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def findmaxh():
    maxh = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] > maxh:
                maxh = table[i][j]

    for i in range(N):
        for j in range(N):
            if table[i][j] == maxh:
                top.append([i, j])

    return maxh

def search(y, x, count):
    global max_count

    if count > max_count:
        max_count = count

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not iswall(ny, nx) and table[ny][nx] < table[y][x]:
            search(ny, nx, count+1)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]

    top = []
    maxh = findmaxh()

    max_count = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == maxh:
                a = [i, j]
            else:
                a = []

            # 좌표마다 공사하여 깎을 수 있는 모든 경우(0~K)를 적용
            for k in range(K+1):
                table[i][j] -= k

                # 최대높이를 공사할 경우 탐색 리스트에서는 제외외
                for m in range(len(top)):
                    if top[m] == a:
                        continue
                    else:
                        search(top[m][0], top[m][1], 0)
                table[i][j] += k

    print("#{} {}".format(tc, max_count+1))





