def dfs(x, y, time):
    global count, min_time

    if x == a and y == b:
        min_time = time
        count += 1

    dx = [1, 0]
    dy = [0, 1]
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= a and 0 <= ny <= b not visted[ny][nx]:

            dfs(nx, ny, time+1)

n, m = map(int, input().strip().split(' '))
a, b = map(int, input().strip().split(' '))
# 가로, 세로 (x, y)



count = 0
min_time = 0x7fffffff
visited = [[]]

if a < 0 or b < 0 or a > n or b > m:
    print('fail')
else:
    dfs(0, 0, 0)
    print(min_time)
    print(count)

# 24 24
# 24 24