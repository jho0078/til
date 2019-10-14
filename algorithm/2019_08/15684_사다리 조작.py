def check():
    for i in range(N):
        k = i
        for j in range(H):
            if A[j][k]:
                k += 1
            elif k > 0 and A[j][k-1]:
                k -= 1

        if k != i:
            return 0
    return 1


def sol(s, y, x):
    global MIN

    if s >= MIN:
        return

    if check():
        MIN = s

    if s == 3:
        return

    j = x
    for i in range(y, H):
        while j < N-1:
            if not A[i][j] and not A[i][j+1]:
                A[i][j] = 1
                sol(s+1, i, j+2)
                A[i][j] = 0
            j += 1
        j = 0
        i += 1


N, M, H = map(int, input().split())
A = [[0] * N for i in range(H)]
MIN = 4

for i in range(M):
    y, x = map(int, input().split())
    A[y - 1][x - 1] = 1

sol(0, 0, 0)
if MIN < 4:
    print(MIN)
else:
    print(-1)
