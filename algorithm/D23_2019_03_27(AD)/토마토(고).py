def iswall(y,x):
    global X, Y
    if y < 0 or x < 0 or y >= N or x >= M:
        return True
    return False

def solution():
    day = 1
    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]
        table[y][x] = -1


        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not iswall(ny, nx) and table[ny][nx] == 0 and visited[ny][nx] == 0:
                queue.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
                day = visited[ny][nx]

    return day - 1

M, N = map(int, input().split())
table = [list(map(int, input().split())) for i in range(N)]
visited = [[0]*M for i in range(N)]

queue = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            queue.append([i,j])
            visited[i][j] = 1

day = solution()
flag = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print(day)
else:
    print(-1)



