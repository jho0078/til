import sys
sys.stdin = open("배열정리_input.txt")

Y, X =  map(int, input().split())

data = [list(map(int, input().split())) for i in range(Y)]

for i in range(Y):
    p = 0
    for j in range(X):
        if data[i][j] == 1:
            p += 1
            data[i][j] = p
        else:
            p = 0

for i in range(Y):
    print(' '.join(list(map(str, data[i]))))