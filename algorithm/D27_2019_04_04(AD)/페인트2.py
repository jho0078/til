def marking(y, x):
    ys = y - N
    first = x
    a = 1
    one = 1
    two = 2
    for i in range(N*3+1):
        for j in range(a):
            if D[ys+i][first+j] 

        if first == N:
            one = -1
            two = -2
        first -= one
        a += two

N = int(input())
R = int(input())
D = [list(map(int, input().split())) for i in range(N)]

for i in range(N-1):
    for j in range(N-1):
        for k in range(i+1, N):
            for l in range(j+1, N):
                C =
                marking(i,j)