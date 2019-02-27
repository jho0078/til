import sys
sys.stdin = open("색종이 배치.txt")

data = [[0 for _ in range(102)] for _ in range(102)]

for i in range(2):
    y, x, n, m = map(int, input().split())

    for i in range(y+1, y+m+1):
        for j in range(x+1, x+n+1):
            data[i][j] = 1

    for i in range(y, y+m+2):
        data[i][x] = 2
        data[i][x+n+1] = 2

    for i in range(x, x+n+2):
        data[y][i] = 2
        data[y+m+1][i] = 2

for i in range(102):
    print(data[i])