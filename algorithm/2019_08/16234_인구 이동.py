def check(y, x):
    global flag, visited

    union = []
    union.append([y, x])
    q = []
    q.append([y, x])
    visited[y][x] = 1

    SUM = 0
    while q:
        y, x = q.pop(0)
        SUM += A[y][x]
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and L <= abs(A[y][x] - A[ny][nx]) <= R:
                q.append([ny, nx])
                union.append([ny, nx])
                visited[ny][nx] = 1

    if len(union) > 1:
        flag = 1
        for uni in union:
            A[uni[0]][uni[1]] = SUM//len(union)


def sol():
    global flag, visited

    flag = 1
    count = 0
    while flag:
        flag = 0
        visited = [[0] * N for i in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    check(i, j)

        for i in range(len(A)):
            print(A[i])
        print()

        if flag == 0:
            return count

        count += 1

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

print(sol())
