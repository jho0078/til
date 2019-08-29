

def bfs(y, x, size, num):
    global time

    if not fish or fish[0][0] >= size:
        return

    q = []
    q.append((y, x))
    V = [[0] * N for _ in range(N)]
    V[y][x] = 1
    eat = [999, 999]
    shortest = 999
    while q:
        y, x = q.pop(0)

        if V[y][x] > shortest:
            break

        for dy, dx in (1,0), (-1,0), (0,1), (0,-1):
            ny, nx = y + dy, x + dx
            if -1 < ny < N and -1 < nx < N:
                if size >= A[ny][nx] and not V[ny][nx]:
                    q.append((ny, nx))
                    V[ny][nx] = V[y][x] + 1
                    if A[ny][nx] and size > A[ny][nx]:
                        shortest = V[y][x]
                        if eat[0] > ny:
                            eat[0], eat[1] = ny, nx
                        elif eat[0] == ny and eat[1] > nx:
                            eat[0], eat[1] = ny, nx

    if eat[0] == 999:
        return
    A[eat[0]][eat[1]] = 0

    for i in range(len(fish)):
        if fish[i][1] == eat[0] and fish[i][2] == eat[1]:
            fish.pop(i)
            break

    time += shortest
    num += 1
    if num == size:
        size += 1
        num = 0

    bfs(eat[0], eat[1], size, num)


N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

fish = []
for i in range(N):
    for j in range(N):
        if 0 < A[i][j] < 7:
            fish.append([A[i][j], i, j])
        elif A[i][j] == 9:
            A[i][j] = 0
            shark = (i, j)

time = 0
fish.sort()
bfs(shark[0], shark[1], 2, 0)
print(time)