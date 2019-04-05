def check(ny, nx, y, x):
    if D[ny][nx] == '#':
        return y, x
    else:
        return ny, nx

def solution(yr,xr,yb,xb,xh,yh):

    que = []
    que.append([yr,xr,yb,xb,0])
    A[yr][xr][yb][xb] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    while que:
        # print(que)
        y1, x1, y2, x2, t = que.pop(0)
        if t > 10:
            return -1
        if y1 == yh and x1 == xh:
            return t
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if nx1 >= 0 and ny1 >= 0 and nx2 >= 0 and ny2 >= 0 and nx1 <= C-1 and nx2 <= C-1 and ny1 <= R-1 and ny2 <= R-1:
                if D[ny1][nx1] == '#' and D[ny2][nx2] == '#':
                    continue
                else:
                    a, b = check(ny1, nx1, y1, x1)
                    c, d = check(ny2, nx2, y2, x2)
                    if c == yh and d == xh:
                        continue
                    if a == c and b == d:
                        continue
                    if A[a][b][c][d] == 0:
                        A[a][b][c][d] = 1
                        que.append([a,b,c,d,t+1])
    return -1

T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    D = [list(input()) for i in range(R)]
    A = [[[[0]*C for i in range(R)] for j in range(C)] for k in range(R)]
    for i in range(R):
        for j in range(C):
            if D[i][j] == 'R':
                xr, yr = j, i
            elif D[i][j] == 'B':
                xb, yb = j, i
            elif D[i][j] == 'H':
                xh, yh = j, i

    print(solution(yr,xr,yb,xb,xh,yh))



