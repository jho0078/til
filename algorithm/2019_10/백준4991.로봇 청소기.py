def findmin(s, p, d):
    global k, MIN

    if d > MIN:
        return

    if s == k:
        MIN = min(MIN, d)

    for i in range(k+1):
        if not check[i]:
            check[i] = 1
            findmin(s+1, i, d + graph[p][i])
            check[i] = 0

def BFS(y, x, n):
    global k, flag

    visited = [[0]*w for _ in range(h)]
    que = [(y, x)]
    visited[y][x] = 1
    chk = [0]*(k+1)
    chk[n] = 1

    while que:
        y, x = que.pop(0)
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if -1 < ny < h and -1 < nx < w and not visited[ny][nx] and data[ny][nx] != 'x':

                que.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

                if data[ny][nx] != -1:
                    t = data[ny][nx]
                    # print("t", t)
                    graph[n][t] = visited[y][x]
                    graph[t][n] = visited[y][x]
                    chk[t] = 1
                    if sum(chk) == k+1:
                        # print("chk", chk)
                        flag = 1
                        return



while 1:
    w, h = map(int, input().split())
    if not w and not h:
        break

    data = [list(input()) for _ in range(h)]

    k = 0
    position = []
    for i in range(h):
        for j in range(w):
            if data[i][j] == '*':
                k += 1
                data[i][j] = k
                position.append((i, j, k))

            elif data[i][j] == 'o':
                data[i][j] = 0
                position.insert(0, (i, j, 0))

            elif data[i][j] == '.':
                data[i][j] = -1


    graph = [[0]*(k+1) for _ in range(k+1)]
    print(k)
    for i in range(h):
        print(data[i])

    flag = 0
    for i in range(k):
        flag = 0
        y, x, n = position[i][0], position[i][1], position[i][2]
        print(y, x, n)
        BFS(y, x, n)
        if not flag:
            break

    # if not flag:
    #     print(-1)
    #     continue

    for i in range(k+1):
        print(graph[i])

    check = [0]*(k+1)
    check[0] = 1
    MIN = 0x7fffffff
    findmin(0, 0, 0)
    print(MIN)




