def iswall(y, x):

    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def check(y, x):
    dx = [1, -1]
    dy = [-1, -1]
    for i in range(2):
        for k in range(1, N+1):
            nx = x + dx[i]*k
            ny = y + dy[i]*k
            if iswall(ny, nx):
                break
            elif table[ny][nx] == 1:
                return 0
    return 1


def chess(s, n):
    global count

    if s == n:
        count += 1
        return

    for i in range(N):
        if chk[i] == 0 and check(s, i):
            chk[i] = 1
            table[s][i] = 1
            chess(s+1, n)
            chk[i] = 0
            table[s][i] = 0


N = int(input())
table = [[0]*N for i in range(N)]
count = 0
chk = [0]*N
chk2 = [0]*2*N
chk3 = [0]*2*N
chess(0, N)
print(count)

(N-1) - (r-c)

