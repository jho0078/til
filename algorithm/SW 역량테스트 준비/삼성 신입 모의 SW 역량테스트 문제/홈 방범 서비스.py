import sys
sys.stdin = open("홈 방범 서비스_input2.txt")

def iswall(y, x):
    global N

    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def solution(y, x, max_count):
    global K, N

    # 아래, 위, 우, 좌
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 대각선
    dx2 = [1, 1, -1, -1]
    dy2 = [-1, 1, -1, 1]

    K = 1
    while True:
        if K > N:
            return max_count

        count = 0
        if table[y][x] == 1:
            count += 1

        for i in range(4):
            for j in range(1, K):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if not iswall(ny, nx):
                    if table[ny][nx] == 1:
                        if y == 4 and x == 5:
                            print(ny, nx)
                        count += 1

        for i in range(4):
            for j in range(1, K-1):
                nx = x + dx2[i] * j
                ny = y + dy2[i] * j
                if not iswall(ny, nx):
                    if table[ny][nx] == 1:
                        if y == 4 and x == 5:
                            print(ny, nx)
                        count += 1

        print(K, y, x, count)
        if count*M - (K*K + (K-1)*(K-1)) >= 0 and count > max_count:
            print(M, y, x, count, K, (K*K + (K-1)*(K-1)))
            max_count = count

        K += 1


T = int(input())
for tc in range(1, 2):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]
    max_count = 0

    for i in range(N):
        for j in range(N):
            max_count = solution(i, j, max_count)
            # max_count = c

    print(max_count)