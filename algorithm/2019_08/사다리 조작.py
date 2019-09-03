def check():
    for x in range(N):
        k = x
        for y in range(H):
            if A[y][k]:
                k += 1
            elif k > 0 and A[y][k-1]:
                k -= 1

        if x != k:
            return False
    return True

def sol(s, y, x):
    global MIN

    if MIN <= s:
        return

    if check():
        if s < MIN:
            MIN = s

    if s == 3:
        return

    i = y
    j = x

    while i < H:
        while j < N-1:
            if not A[i][j] and not A[i][j+1]:
                A[i][j] = 1
                if j + 2 < N-1:
                    sol(s+1, i, j+2)
                else:
                    sol(s+1, i+1, 0)
                A[i][j] = 0

            elif A[i][j]:
                j += 1

            j += 1
        j = 0
        i += 1


N, M, H = map(int, input().split())
A = [[0]*N for i in range(H)]
MIN = 4

for i in range(M):
    y, x = map(int, input().split())
    A[y-1][x-1] = 1

sol(0, 0, 0)
if MIN < 4:
    print(MIN)
else:
    print(-1)

