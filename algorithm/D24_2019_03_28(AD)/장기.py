def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= M:
        return True
    return False

def jangi(y, x):

    queue = []
    queue.append([y, x])
    visited[y][x] = 1
    count = 1

    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx) and table[ny][nx] == 0:
                if i == 0 or i == 1:
                    dx2 = [dx[i], dx[i]]
                    dy2 = [1, -1]
                else:
                    dx2 = [1, -1]
                    dy2 = [dy[i], dy[i]]

                for j in range(2):
                    nx2 = nx + dx2[j]
                    ny2 = ny + dy2[j]
                    if not iswall(ny2, nx2):
                        if ny2 == s and nx2 == k:
                            # print(y, x, ny2, nx2)
                            visited[ny2][nx2] = visited[y][x]
                            count = visited[ny2][nx2]
                            return count

                        elif table[ny2][nx2] == 0 and visited[ny2][nx2] == 0:
                            queue.append([ny2, nx2])
                            visited[ny2][nx2] = visited[y][x] + 1
                            count = visited[ny2][nx2]



N, M = map(int, input().split())
R, C, S, K = map(int, input().split())
r, c, s, k = R -1, C-1, S-1, K-1

table = [[0]*M for i in range(N)]
visited = [[0]*M for i in range(N)]

print(jangi(r, c))

for i in range(N):
    print(visited[i])