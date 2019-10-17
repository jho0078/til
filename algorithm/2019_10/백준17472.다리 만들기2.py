import heapq

def check(y, x, k):
    q = [(y, x)]
    data[y][x] = k

    while q:
        y, x = q.pop(0)
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if -1 < ny < N and -1 < nx < M and data[ny][nx] == -1:
                q.append((ny, nx))
                data[ny][nx] = k

def fill_queue(a):
    global k

    for i in range(k):
        if graph[a][i] and graph[a][i] < 9999 and not visited[i]:
            heapq.heappush(que, (graph[a][i], i))

def prim():
    global k

    cnt = 0
    visited[1] = 1
    fill_queue(1)

    while que:
        w, n = heapq.heappop(que)

        if visited[n]:
            continue

        visited[n] = 1
        cnt += w
        fill_queue(n)

    if sum(visited) == k-1:
        return cnt
    else:
        return -1

N, M = map(int, input().split())
data = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            data[i][j] = -1

k = 1
for i in range(N):
    for j in range(M):
        if data[i][j] == -1:
            check(i, j, k)
            k += 1

graph = [[9999]*k for i in range(k)]

for i in range(N):
    for j in range(M):
        if data[i][j]:
            start = data[i][j]
            for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                h = 1
                flag = 0
                while h < max(N, M):
                    ny, nx = i + dy*h, j + dx*h
                    if ny < 0 or ny >= N or nx < 0 or nx >= M:
                        break

                    if data[ny][nx]:
                        end = data[ny][nx]
                        flag = 1
                        break

                    h += 1

                if flag:
                    if h-1 >= 2 and graph[start][end] > h-1:
                        graph[start][end] = h - 1

visited = [0]*k
que = []

print(prim())

for i in range(N):
    print(data[i])

for i in range(k):
    print(graph[i])