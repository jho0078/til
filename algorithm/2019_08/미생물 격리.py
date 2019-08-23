import sys
sys.stdin = open("미생물 격리_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(K)]
    A = [[0]*N for i in range(N)]
    q = []
    for i in range(len(data)):
        q.append([data[i][0], data[i][1]])
        A[data[i][0]][data[i][1]] = [data[i][2], data[i][3]]

    # (상: 1, 하: 2, 좌: 3, 우: 4)
    #  y,x and 갯수, 방향

    while M > 0:
        S = [[0]*N for i in range(N)]
        dy = [0, -1, 1, 0, 0]
        dx = [0, 0, 0, -1, 1]
        d = [0,2,1,4,3]
        nq = []
        for i in range(len(q)):
            y, x = q[i][0], q[i][1]
            y2, x2 = y + dy[A[y][x][1]], x + dx[A[y][x][1]]

            if S[y2][x2] == 0:
                S[y2][x2] = [0]*3
                S[y2][x2][0] = A[y][x][0]
                S[y2][x2][1] = A[y][x][1]
                S[y2][x2][2] = A[y][x][0]
                if y2 == 0 or x2 == 0 or y2 == N - 1 or x2 == N - 1:
                    S[y2][x2][0] //= 2
                    S[y2][x2][1] = d[S[y2][x2][1]]
                if S[y2][x2][0] > 0:
                    nq.append([y2,x2])

            else:
                if S[y2][x2][2] < A[y][x][0]:
                    S[y2][x2][2] = A[y][x][0]
                    S[y2][x2][1] = A[y][x][1]
                S[y2][x2][0] += A[y][x][0]

        A = S
        q = nq
        M -= 1

    result = 0
    for i in range(len(q)):
        result += S[q[i][0]][q[i][1]][0]
    print("#{} {}".format(tc, result))