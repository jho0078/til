import sys
sys.stdin = open("최소비용_input.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def Prim(N, y, x):

    visited = [[0] * N for i in range(N)]
    D[y][x] = 0
    for i in range(N*N):
        min = 99999999999

        for j in range(N):
            for k in range(N):
                if not visited[j][k] and D[j][k] < min:
                    min = D[j][k]
                    min_y = j
                    min_x = k
        visited[min_y][min_x] = 1

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for j in range(4):
            if not iswall(min_y + dy[j], min_x + dx[j]):
                if table[min_y + dy[j]][min_x + dx[j]] > table[min_y][min_x]:
                    if D[min_y + dy[j]][min_x + dx[j]] > D[min_y][min_x] + 1 + (table[min_y + dy[j]][min_x + dx[j]] - table[min_y][min_x]):
                        D[min_y + dy[j]][min_x + dx[j]] = D[min_y][min_x] + 1 + (table[min_y + dy[j]][min_x + dx[j]] - table[min_y][min_x])
                else:
                    if D[min_y + dy[j]][min_x + dx[j]] > D[min_y][min_x] + 1:
                        D[min_y + dy[j]][min_x + dx[j]] = D[min_y][min_x] + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    D = [[99999999] * N for i in range(N)]
    Prim(N, 0, 0)
    print("#{} {}".format(tc, D[N-1][N-1]))