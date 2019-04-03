def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= M:
        return True
    return False

def solution():

    queue = []
    queue.append((0,0,0))
    visited[0][0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y, z = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not iswall(nx, ny):
                if table[nx][ny] == 0 and visited[nx][ny][z] == -1:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx,ny,z))

                if z == 0 and table[nx][ny] == 1 and visited[nx][ny][z+1] == -1:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    queue.append((nx,ny,z+1))


N, M = map(int, input().split())
table = [list(map(int, list(input()))) for i in range(N)]
visited = [[[-1]*2 for j in range(M)] for i in range(N)]
solution()

if visited[N-1][M-1][0] == -1:
    print(visited[N-1][M-1][1])
elif visited[N-1][M-1][1] == -1:
    print(visited[N-1][M-1][0])
else:
    print(min(visited[N-1][M-1]))