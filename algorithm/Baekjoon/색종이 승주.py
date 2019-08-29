import sys
sys.stdin = open('input.txt')


def check(x,y,n):
    for i in range(n):
        for j in range(n):
            nx = x + i
            ny = y + j
            if nx < 0 or nx >= SIZE or ny < 0 or ny >= SIZE or M[nx][ny] != 1:
                return False
    return True

def paint(x,y,n,c):
    global remain

    if c == 2:
        o = -1
    else:
        o = 1

    for i in range(n):
        for j in range(n):
            nx = x+i
            ny = y+j
            M[nx][ny] = c
            remain += o

def DFS(n,count):
    global MIN

    if count > MIN:
        return

    if n <= 0:
        return

    if remain == 0:
        if count < MIN:
            MIN = count
            return

    # flag = False

    if N[n]<5:
        for i in range(SIZE):
            # if not flag:
            for j in range(SIZE):
                if M[i][j] == 1:
                    if check(i,j,n):
                        x, y = i, j
                        paint(x, y, n, 2)
                        N[n] += 1
                        DFS(n, count + 1)
                        N[n] -= 1
                        paint(x, y, n, 1)

    # if flag:
    #     x,y = flag
    #     paint(x,y,n,2)
    #     N[n]+=1
    #     DFS(n, count+1)
    #     N[n]-=1
    #     paint(x,y,n,1)

    DFS(n-1, count)

SIZE = 10

M = [list(map(int, input().split())) for _ in range(SIZE)]

remain = 0

for i in range(SIZE):
    for j in range(SIZE):
        if M[i][j]:
            remain += 1

N = [0,0,0,0,0,0]

MIN = 0xfffffff

DFS(5,0)

if MIN == 0xfffffff:
    print(-1)
else:
    print(MIN)