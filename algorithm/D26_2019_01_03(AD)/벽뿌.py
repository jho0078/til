def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= M:
        return True
    return False

def solution(y, x):

    count = -1
    queue = []
    queue.append([y,x])
    visited[y][x] = 1

    while queue:
        t = queue.pop(0)
        y, x = t[0], t[1]
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx):
                if ny == N-1 and nx == M-1:
                    visited[ny][nx] = visited[y][x] + 1
                    return visited[ny][nx]

                elif table[ny][nx] == 0 and visited[ny][nx] == 0:
                    queue.append([ny,nx])
                    visited[ny][nx] = visited[y][x] + 1

    return count

N, M = map(int, input().split())
table = [list(map(int, list(input()))) for i in range(N)]

w = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            w.append([i,j])

min_c = 1000000000
for i in range(len(w)):
    table[w[i][0]][w[i][1]] = 0
    visited = [[0] * M for i in range(N)]
    c = solution(0, 0)
    table[w[i][0]][w[i][1]] = 1
    if c != -1 and c < min_c:
        min_c = c

if min_c == 1000000000:
    print(-1)
else:
    print(min_c)