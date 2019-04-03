def isallik():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if table[z][y][x] == 0:
                    return 0
    return 1

def iswall(z, y, x):
    if z < 0 or y < 0 or x < 0 or z >= H or y >= N or x >= M:
        return True
    return False

def solution():

    day = 1
    while queue:
        t = queue.pop(0)
        z, y, x = t[0], t[1], t[2]
        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if not iswall(nz, ny, nx) and table[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                queue.append([nz,ny,nx])
                table[nz][ny][nx] = 1
                visited[nz][ny][nx] = visited[z][y][x] + 1
                day = visited[nz][ny][nx]

    return day-1

M, N, H = map(int, input().split())
table = [[list(map(int, input().split())) for j in range(N)] for i in range(H)]
visited = [[[0]*M for j in range(N)] for i in range(H)]
# print(table)

queue = []
for z in range(H):
    for y in range(N):
        for x in range(M):
            if table[z][y][x] == 1:
                queue.append([z,y,x])
                visited[z][y][x] = 1

d = solution()
if isallik():
    print(d)
else:
    print(-1)


