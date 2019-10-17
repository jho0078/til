from itertools import combinations

def spread(c, empty):
    global MIN

    que = list(c)
    visited = [[0]*N for _ in range(N)]
    for i in range(M):
        visited[que[i][0]][que[i][1]] = 1

    time = 0
    while que:
        y, x = que.pop(0)
        if visited[y][x] != time:
            if not empty:
                break
            time = visited[y][x]

        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and (not data[ny][nx] or data[ny][nx] == 2):
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] > MIN:
                    return MIN

                que.append((ny, nx))
                if not data[ny][nx]:
                    empty -= 1

    # for i in range(N):
    #     print(visited[i])

    time = 0
    if not empty:
        for i in range(N):
            time = max(time, max(visited[i]))
        return time - 1

    return MIN

N, M = map(int, input().split())
data = [list(map(int, input().split())) for i in range(N)]

virus = []
empty = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            virus.append((i, j))
        elif not data[i][j]:
            empty += 1

com = list(combinations(virus, M))

MIN = 999999
for c in com:
    MIN = min(MIN, spread(c, empty))

if MIN != 999999:
    print(MIN)
else:
    print(-1)
    # print(c)
    # print(list(c))