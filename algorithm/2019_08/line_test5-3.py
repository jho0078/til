def sol():
    global min_time, count

    q = [[0, 0]]
    visited[0][0] = 0
    while q:
        x, y = q.pop(-1)

        dx = [1, 0]
        dy = [0, 1]
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= a and 0 <= ny <= b and visited[ny][nx] > visited[y][x] + 1:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1

    min_time = visited[b][a]


n, m = map(int, input().strip().split(' '))
a, b = map(int, input().strip().split(' '))
# 가로, 세로 (x, y)

n, m, a, = 24

visited = [[0x7fffffff] * (a+1) for _ in range(b+1)]
visited[0][0] = 0
count = 0
min_time = 0x7fffffff

if a < 0 or b < 0 or a > n or b > m:
    print('fail')
else:
    sol()
    print(min_time)
    print(count)



while q:
    x, y = q.pop(-1)



    dx = [-1, 0]
    dy = [0, -1]
    num = 0
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= a and 0 <= ny <= b:
            q.append([nx, ny])


min_time = visited[b][a]
