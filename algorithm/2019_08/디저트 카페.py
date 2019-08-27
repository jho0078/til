import sys
sys.stdin = open("디저트 카페_input.txt")

def sol(y, x, s):
    global y_start, x_start

    if s == 4:


    d = [(1,1), (1,-1), (-1,-1), (-1,1)]
    ny, nx = y + d[s][0], x + d[s][1]
    if -1 < ny < N and -1 < nx < N:
        if A[ny][nx] not in cafe:
            cafe.append(A[ny][nx])
            sol(ny, nx, s+1)
            sol(ny, nx, s)
        else:
            return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]

    for i in range(N-1):
        for j in range(1, N-1):
            y_start, x_start = i, j
            cafe = []
            sol(i, j)
