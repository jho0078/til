import sys
sys.stdin = open("등산로 조성_input.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def search(y, x, count):
    global max_count

    if count > max_count:
        max_count = count

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not iswall(ny, nx) and visited[ny][nx] == 0 and table[ny][nx] < table[y][x]:
            visited[ny][nx] = 1
            search(ny, nx, count+1)




    # for i in range(N):
    #     print(visited[i])
    # print()
    #
    # max_distance1 = 0
    # for i in range(N):
    #     for j in range(N):
    #         if visited[i][j] > max_distance1:
    #             max_distance1 = visited[i][j]




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]

    maxh = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] > maxh:
                maxh = table[i][j]

    top = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == maxh:
                top.append([i, j])
    print(top)
    max_distance = 0

    max_count = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] != maxh:

                table[i][j] -= K
                for k in range(len(top)):
                    visited = [[0 for _ in range(N)] for _ in range(N)]
                    search(top[k][0], top[k][1], 0)

                    # if d > max_distance:
                    #     max_distance = d
                table[i][j] += K

    print(max_count)





