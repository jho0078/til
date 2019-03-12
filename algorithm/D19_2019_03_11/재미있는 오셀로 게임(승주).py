import sys
sys.stdin = open('재미있는 오셀로 게임_input.txt')

T = int(input())


def isWall(x,y):
    if x < 0 or x > N-1 or y < 0 or y > N-1:
        return True
    return False


def check(i, j, color):
    global N, M, flag
        # 좌 우 상 하 좌상, 좌하, 우상, 우하
    di = [0, 0, -1, 1, -1, 1, -1, 1]
    dj = [-1, 1, 0, 0, -1, -1, 1, 1]

    visited = [[0 for _ in range(N)]for _ in range(N)]

    M[i][j] = color
    visited[i][j] = 1
    stack = []
    stack.append([i, j, 0])
    tmp = []

    while len(stack) > 0:
        if not flag:
            s = stack.pop()
            for m in range(8):
                if not isWall(s[0] + di[m], s[1] + dj[m]) and M[s[0] + di[m]][s[1] + dj[m]] != 0:
                    a = 1
                    while 1:
                        if isWall(s[0] + di[m]*a, s[1] + dj[m]*a) or M[s[0] + di[m]*a][s[1] + dj[m]*a] != 0:
                            break
                        elif M[s[0] + di[m]*a][s[1] + dj[m]*a] != s[2]:
                            a += 1
                        else:
                            for i in range(1, a):
                                M[s[0] + di[m] * a][s[1] + dj[m] * a] = s[2]
                            break


                    # stack.append([s[0] + di[m], s[1] + dj[m], m])
                    # flag = 1
                    #
                    # if flag:
                    #     s = stack.pop()
                    #     tmp.append(s)
                    #     print(s)
                    #     i = s[0]
                    #     j = s[1]
                    #     find = 0
                    #     while not isWall(i + di[s[2]], j + dj[s[2]]) and M[i + di[s[2]]][j + dj[s[2]]] != 0:
                    #         i += di[s[2]]
                    #         j += dj[s[2]]
                    #         if M[i][j] == color:
                    #             find = 1
                    #             break
                    #         else:
                    #             tmp.append([i,j])
                    #
                    #
                    #     print(tmp)
                    #
                    #     if find:
                    #         while len(tmp) > 0:
                    #                 t = tmp.pop()
                    #                 M[t[0]][t[1]] = color
                    #     else:
                    #         tmp = []

        for x in M:
            print(x)
        print()

for tc in range(T):
    N, C = map(int, input().split())
    M = [[0 for _ in range(N)] for _ in range(N)]

    M[N//2-1][N//2-1] = 2
    M[N // 2-1][N // 2] = 1
    M[N // 2][N // 2-1] = 1
    M[N // 2][N // 2] = 2

    for _ in range(C):
        i, j, color = map(int, input().split())
        flag = 0
        check(i-1, j-1, color)

    black = 0
    white = 0
    for x in range(N):
        for y in range(N):
            if M[x][y] == 1:
                white +=1
            else:
                black += 1

    print('#{} {} {}'.format(tc+1 , white, black))