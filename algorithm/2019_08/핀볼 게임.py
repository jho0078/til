import sys
sys.stdin = open("핀볼 게임_input.txt")

def sol(y, x, d):
    global count
    # 우, 좌, 상, 하
    y_start, x_start = y, x
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    wall = [1,0,3,2]
    dir = [[],[1,2,3,0],[1,3,0,2],[3,0,1,2],[2,0,3,1],[1,0,3,2]]

    while True:
        y, x = y + dy[d], x + dx[d]
        if y == -1 or x == -1 or y == N or x == N:
            d = wall[d]
            count += 1
        elif A[y][x] > 0 and A[y][x] < 6:
            d = dir[A[y][x]][d]
            count += 1
        elif A[y][x] > 5 and A[y][x] < 16:
            y, x = hole[A[y][x]][0], hole[A[y][x]][1]
        elif A[y][x] == -1 or (y == y_start and x == x_start):
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]
    hole = [0]*16
    MAX = 0

    for y in range(N):
        for x in range(N):
            if A[y][x] > 5 and A[y][x] < 11:
                if hole[A[y][x]+5] == 0:
                    hole[A[y][x]+5] = [y,x]
                else:
                    hole[A[y][x]] = [y,x]
                    A[y][x] += 5

    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                for k in range(4):
                    count = 0
                    sol(i, j, k)
                    if count > MAX:
                        MAX = count

    print("#{} {}".format(tc, MAX))
