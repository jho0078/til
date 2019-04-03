def iswall(y, x):

    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def marking(y, x, n, copytable):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    for i in range(8):
        for k in range(1, n+1):
            nx = x + dx[i]*k
            ny = y + dy[i]*k
            if iswall(ny, nx):
                break
            else:
                copytable[ny][nx] = 1


def chess(s, n, table):
    global count

    if s == n:
        count += 1
        return

    for i in range(n):
        copytable = [table[i][:] for i in range(N)]
        if copytable[s][i] == 0:
            copytable[s][i] = 1
            marking(s, i, n, copytable)
            chess(s+1, n, copytable)

N = int(input())
table = [[0]*N for i in range(N)]
count = 0
chess(0, N, table)
print(count)

