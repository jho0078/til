def solution():

    q1 = []
    q2 = []
    q1.append([xr,yr])
    q2.append([xb,yb])
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    while 1:
        x1, y1 = q1.pop(0)
        for i in range(4):
            dx, dy = x1 + dx[i], y1 + dy[i]
            I

T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    D = [list(input()) for i in range(R)]
    for i in range(R):
        for j in range(C):
            if D[i][j] == 'R':
                xr, yr = i, j
            elif D[i][j] == 'B':
                xb, yb = i, j
            # elif D[i][j] == 'H':
            #     xh, yh = i, j



