import sys
sys.stdin = open("홈 방범 서비스_input.txt")

def iswall(y, x):
    global N

    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def solution(y, x, max_count):


    for K in range(1, N+2):
        count = 0
        y_start = y - (K - 1)
        x_start = x - (K - 1)

        one = 1
        two = 2
        first_idx = K - 1
        b = 1

        for i in range(2*K - 1):
            for j in range(b):
                if not iswall(y_start + i, x_start + first_idx + j) and table[y_start + i][x_start + first_idx + j] == 1:
                    count += 1

            if first_idx == 0:
                one = -one
                two = -two
            first_idx -= one
            b += two

        if count * M - (K * K + (K - 1) * (K - 1)) >= 0 and count > max_count:
            max_count = count

    return max_count


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]
    max_count = 0

    for i in range(N):
        for j in range(N):
            max_count = solution(i, j, max_count)

    print("#{} {}".format(tc, max_count))