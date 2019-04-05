def find(y, x):
    t = []
    que = []
    que.append([y,x])
    visited[y][x] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    while que:
        y, x = que.pop(0)

        c = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > M-1 or ny > N-1:
                continue
            if visited[ny][nx] == 0 and data[ny][nx] == 'X':
                visited[ny][nx] = 1
                que.append([ny,nx])
            if data[ny][nx] == '.':
                c += 1
        if c > 0:
            t.append([y, x])
    return t

N, M = map(int, input().split())
data = [list(input()) for i in range(N)]
# print(data)
visited = [[0]*M for i in range(N)]

flag = 0
for i in range(N):
    for j in range(M):
        if flag == 0 and data[i][j] == 'X' and visited[i][j] == 0:
            A = find(i,j)
            flag = 1
        if flag == 1 and data[i][j] == 'X' and visited[i][j] == 0:
            B = find(i,j)

# print(A)
# print(B)
a, b = len(A), len(B)
MIN = 0x7fffffff
for i in range(a):
    for j in range(b):
        d = abs(A[i][0] - B[j][0]) + abs(A[i][1] - B[j][1]) - 1
        if d < MIN:
            MIN = d
print(MIN)
# for i in range(N):
#     print(visited[i])
