import sys
sys.stdin = open("guganhab_input.txt")
T = int(input())
for tc in range(1, T + 1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    data = list(map(int, input().split()))
    min = 134841351413153
    max = 0
    for i in range(M-1, N):
        sum = 0
        for j in range(M):
            sum += data[i-j]
        if sum > max:
            max = sum
        if sum < min:
            min = sum

    chai = max -min

    print("#{} {}".format(tc, chai))



