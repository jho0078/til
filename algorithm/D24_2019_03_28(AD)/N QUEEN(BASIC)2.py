def iswall(y, x):

    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def marking(y, x, n, t):
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    for i in range(8):
        for k in range(1, n+1):
            nx = x + dx[i]*k
            ny = y + dy[i]*k
            if iswall(ny, nx):
                break
            else:
                t.append([ny,nx])


def chess(s, n):
    global count

    if s == n:
        count += 1
        return

    for i in range(n):
        t = []
        if table[s][i] == 0:
            table[s][i] = 1
            marking(s, i, n, t)
            for j in range(len(t)):
                table[t[i][0]][t[i][1]] = 1
            chess(s+1, n)
            for j in range(len(t)):
                table[t[i][0]][t[i][1]] = 0

N = int(input())
table = [[0]*N for i in range(N)]
count = 0
chess(0, N)
print(count)

