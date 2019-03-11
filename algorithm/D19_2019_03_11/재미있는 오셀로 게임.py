import sys
sys.stdin = open("재미있는 오셀로 게임_input.txt")

def iswall(y ,x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [[0 for _ in range(N)] for _ in range(N)]
    table[N//2 - 1][N//2 - 1] = 2
    table[N//2][N//2 - 1] = 1
    table[N//2 - 1][N//2] = 1
    table[N//2][N//2] = 2

    for j in range(M):
        a, b, color = map(int, input().split())
        print(a, b)
        x = a - 1
        y = b - 1
        table[y][x] = color

        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, -1, 1, 1, -1, 1, -1]

        for i in range(8):
            for h in range(1, 9):
                nx1 = x + dx[i]*h
                ny1 = y + dy[i]*h
                if iswall(ny1, nx1) or table[ny1][nx1] == 0:
                    break
                else:
                    if table[ny1][nx1] == color:
                        for k in range(1, h):
                            nx1 = x + dx[i] * k
                            ny1 = y + dy[i] * k
                            table[ny1][nx1] = color
                        break


                # if not iswall(ny1, nx1) and table[ny1][nx1] == 0:
                #     break
                # else:
                #     if not iswall(ny1, nx1) and table[ny1][nx1] == color:
                #         for k in range(1, h):
                #             nx1 = x + dx[i] * k
                #             ny1 = y + dy[i] * k
                #             table[ny1][nx1] = color
                #         break


        for k in range(N):
            print(table[k])
        print()

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                black += 1
            elif table[i][j] == 2:
                white += 1

    print("#{} {} {}".format(tc, black, white))