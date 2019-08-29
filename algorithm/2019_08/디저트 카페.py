import sys
sys.stdin = open("디저트 카페_input.txt")

def sol(y, x, s):
    global MAX

    if s == 4:
        return

    if s == 3:
        # print(length)
        if length[0] > 0 and length[1] > 0:
            if length[0] == length[2] and length[1] == length[3]:
                if len(cafe) > MAX:
                    MAX = len(cafe)
                return


    d = [(1,1), (1,-1), (-1,-1), (-1,1), (1,1)]

    for i in range(2):
        ny, nx = y + d[s+i][0], x + d[s+i][1]
        if -1 < ny < N and -1 < nx < N:
            if A[ny][nx] not in cafe:
                cafe.append(A[ny][nx])
                length[s+i] += 1
                # print("카페:", cafe)
                # print("길이:", length)
                # print(s, i)
                sol(ny, nx, s+i)
                length[s + i] -= 1
                cafe.pop(-1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]
    length = [0]*5
    MAX = 0

    for i in range(N-1):
        for j in range(1, N-1):
            cafe = []
            sol(i, j, 0)

    if MAX == 0:
        print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, MAX))