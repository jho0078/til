import sys
sys.stdin = open("사람네트워크2_input.txt")

# 플로이드
def AllPairsShortest():
    global N

    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][k] + D[k][j], D[i][j])

T = int(input())
for tc in range(1, 2):
    data = list(map(int, input().split()))
    N = data[0]
    D = [data[i:i+N] for i in range(1, len(data), N)]
    for i in range(N):
        for j in range(N):
            if i != j and D[i][j] == 0:
                D[i][j] = 999999999

    for i in range(N):
        print(D[i])

    AllPairsShortest()

    min_sum = 9999999
    for i in range(N):
        sum1 = sum(D[i])
        if sum1 < min_sum:
            min_sum = sum1

    print("#{} {}".format(tc, min_sum))

