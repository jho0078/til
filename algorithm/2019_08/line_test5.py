def sol():
    global min_time, count

    q = [[0, 0]]
    visited[0][0] = 1
    while q:
        x, y = q.pop(-1)

        # if visited[y][x] > min_time:
        #     return min_time - 1

        if x == a and y == b:
            count += 1
            min_time = visited[y][x]

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= a and 0 <= ny <= b and not visited[ny][nx]:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1


n, m = map(int, input().strip().split(' '))
a, b = map(int, input().strip().split(' '))
# 가로, 세로 (x, y)

n, m, a, = 24

visited = [[0] * (a+1) for _ in range(b+1)]
count = 0
min_time = 0x7fffffff

if a < 0 or b < 0 or a > n or b > m:
    print('fail')
else:
    sol()
    print(min_time-1)
    print(count)