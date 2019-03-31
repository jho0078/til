def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def normal(y, x, c, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not iswall(ny, nx) and data[ny][nx] == c and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            normal(ny, nx, c, visited)

N = int(input())
table = [list(input()) for i in range(N)]
data = table
visited1 = [[0]*N for i in range(N)]
visited2 = [[0]*N for i in range(N)]

count = 0
for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            color = data[i][j]
            visited1[i][j] = 1
            normal(i, j, color, visited1)
            count += 1
print(count, end=" ")

count = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == "G":
            data[i][j] = "R"

count = 0
for i in range(N):
    for j in range(N):
        if visited2[i][j] == 0:
            color = data[i][j]
            visited2[i][j] = 1
            normal(i, j, color, visited2)
            count += 1
print(count)
