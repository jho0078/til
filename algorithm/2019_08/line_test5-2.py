def dfs(x, y, time, main_visited):
    global count, min_time

    if x == a and y == b:
        min_time = time
        count += 1

    visited = [main_visited[i][:] for i in range(b+1)]

    dx = [1, 0]
    dy = [0, 1]
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= a and 0 <= ny <= b and not visited[ny][nx]:
            dfs(nx, ny, time+1, visited)

n, m = map(int, input().strip().split(' '))
a, b = map(int, input().strip().split(' '))
# 가로, 세로 (x, y)

visiteda = [[0] * (a + 1) for _ in range(b + 1)]

count = 0
min_time = 0x7fffffff

if a < 0 or b < 0 or a > n or b > m:
    print('fail')
else:
    dfs(0, 0, 0, visiteda)
    print(min_time)
    print(count)