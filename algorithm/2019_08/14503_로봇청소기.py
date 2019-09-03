import sys
sys.stdin = open("input.txt")

def sol(y, x, d):

    A[y][x] = 2
    result = 1

    # 상, 우, 하, 좌
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while 1:

        flag = 0
        for i in range(1, 5):
            ny, nx = y + dir[d - i][0], x + dir[d - i][1]

            if A[ny][nx] == 0:
                A[ny][nx] = result + 1
                result += 1
                flag = 1
                y, x = ny, nx
                d = (d-i)%4
                break

        if flag == 0:
            back = (d + 2)%4
            y, x = y + dir[back][0], x + dir[back][1]

            if A[y][x] == 1:
                return result

N, M = map(int, input().split())
y, x, d = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

print(sol(y, x, d))