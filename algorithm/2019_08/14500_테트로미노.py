def sol(s, y, x, result):
    global MAX

    if s == 3:
        if result > MAX:
            MAX = result
        return

    for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y + dy, x + dx
        if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
            visited[ny][nx] = 1
            sol(s+1, ny, nx, result + A[ny][nx])
            visited[ny][nx] = 0

def ppacu(s, y, x, result):
    global MAX

    if s == 3:
        if result > MAX:
            MAX = result
        return

    for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y + dy, x + dx
        if -1 < ny < N and -1 < nx < M and not visited[ny][nx]:
            visited[ny][nx] = 1
            ppacu(s+1, y, x, result + A[ny][nx])
            visited[ny][nx] = 0

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
visited = [[0]*M for i in range(N)]
MAX = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        sol(0, i, j, A[i][j])
        ppacu(0, i, j, A[i][j])
        visited[i][j] = 0

print(MAX)
