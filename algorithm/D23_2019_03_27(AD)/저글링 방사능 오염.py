def iswall(y,x):
    global X, Y
    if y < 0 or x < 0 or y >= Y or x >= X:
        return True
    return False

def solution(y, x):

    time = 3
    queue = []
    queue.append([y,x])
    visited[y][x] = 3

    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]
        table[y][x] = 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx) and table[ny][nx] == 1 and visited[ny][nx] == 0:
                queue.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
                time = visited[ny][nx]

    return time


X, Y = map(int, input().split())
table = [list(map(int, list(input()))) for i in range(Y)]

x, y = map(int, input().split())
visited = [[0]*X for i in range(Y)]

print(solution(y-1, x-1))
count = 0
for i in range(Y):
    for j in range(X):
        if table[i][j] == 1:
            count += 1
print(count)
for i in range(Y):
    print(table[i])
print()
for i in range(Y):
    print(visited[i])

# 7 8
# 0010111
# 0011000
# 0001100
# 1011111
# 1111011
# 0011100
# 0011100
# 0001000
# 3 5