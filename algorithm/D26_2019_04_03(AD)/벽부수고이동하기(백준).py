def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= M:
        return True
    return False

def solution(y, x):
    global min_c

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
                    visited[ny][nx] = visited[y][x] + 1
                    # count = visited[ny][nx] -2
                    if visited[ny][nx] > min_c + 1:
                        return -1
                    queue.append([ny,nx])

    return count

N, M = map(int, input().split())
table = [list(map(int, list(input()))) for i in range(N)]

# print(N)
# print(table)

w = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            w.append([i,j])

# print(w)
min_c = 1000000000
for i in range(len(w)):
    table[w[i][0]][w[i][1]] = 0
    visited = [[0] * M for i in range(N)]
    # for k in range(N):
    #     print(table[k])
    # print()
    # for k in range(N):
    #     print(visited[k])
    # print()
    c = solution(0, 0)
    table[w[i][0]][w[i][1]] = 1
    if c != -1 and c < min_c:
        min_c = c

if min_c == 1000000000:
    print(-1)
else:
    print(min_c)

# 6 4
# 0100
# 0010
# 1000
# 0000
# 0111
# 0000