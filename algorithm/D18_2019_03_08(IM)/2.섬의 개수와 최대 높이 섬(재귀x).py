import sys
sys.stdin = open("2_input(100).txt")
sys.setrecursionlimit(10**6)

def iswall(y, x):
    global N
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    else:
        return False

def island(y, x):
    global height

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while True:
        table[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx) and table[ny][nx] >= 1:
                if table[ny][nx] > height:
                    height = table[ny][nx]
                x = nx
                y = ny
                break
        else:
            return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    count = 0
    height = 0
    for y in range(N):
        for x in range(N):
            if table[y][x] >= 1:
                print(y, x)
                if table[y][x] > height:
                    height = table[y][x]
                island(y, x)
                count += 1

    print("#{} {} {}".format(tc, count, height))


