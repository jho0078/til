def check(y, x, d):
    n = 0
    q = []
    for k in range(len(d)):
        for h in range(P):
            ny, nx = y + d[k][0] * h, x + d[k][1] * h
            if ny < 0 or ny > N - 1 or nx < 0 or nx > M - 1 or A[ny][nx] == 6:
                break
            elif A[ny][nx] == 0:
                A[ny][nx] = 1
                n += 1
                q.append((ny, nx))

    return n, q

def back(q):
    for i in range(len(q)):
        A[q[i][0]][q[i][1]] = 0

def sol(s, start, num):
    global MAX

    if s == len(cctv):
        MAX = max(MAX, num)

    for i in range(start, len(cctv)):
        y, x = cctv[i][0], cctv[i][1]

        if cctv[i][2] == 1:
            d = [[(1,0)], [(-1,0)], [(0,1)], [(0,-1)]]
            for j in range(4):
                n, q = check(y, x, d[j])
                sol(s+1, i+1, num + n)
                back(q)

        elif cctv[i][2] == 2:
            d = [[(1,0), (-1,0)], [(0,1), (0,-1)]]
            for j in range(2):
                n, q = check(y, x, d[j])
                sol(s + 1, i + 1, num + n)
                back(q)

        elif cctv[i][2] == 3:
            d = [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(0,-1), (-1,0)]]
            for j in range(4):
                n, q = check(y, x, d[j])
                sol(s + 1, i + 1, num + n)
                back(q)

        elif cctv[i][2] == 4:
            d = [[(-1,0), (0,1), (1,0)], [(0,1), (1,0), (0,-1)], [(1,0), (0,-1), (-1,0)], [(0,-1), (-1,0), (0,1)]]
            for j in range(4):
                n, q = check(y, x, d[j])
                sol(s + 1, i + 1, num + n)
                back(q)

        elif cctv[i][2] == 5:
            d = [(1,0), (-1,0), (0,1), (0,-1)]
            n, q = check(y, x, d)
            sol(s + 1, i + 1, num + n)
            back(q)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
cctv = []
P = max(N, M)
MAX = 0


empty = 0
for i in range(N):
    for j in range(M):
        if A[i][j] != 0 and A[i][j] != 6:
            cctv.append([i, j, A[i][j]])
        if A[i][j] == 0:
            empty += 1

sol(0, 0, 0)
print(empty - MAX)