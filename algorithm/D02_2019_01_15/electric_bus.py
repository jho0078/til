import sys
sys.stdin = open("electric_bus_input.txt")
T = int(input())
for tc in range(1, T + 1):
    result = 0
    knm = list(map(int, input().split()))
    bono = list(map(int, input().split()))

    K = knm[0]
    N = knm[1]
    M = knm[2]
    chungjeon = 0
    k = 0
    # if bono[0] < K:
    #     chungjeon += 1

    for i in range(M):
        if k != 0:
            k -= 1
            continue
        if bono[i] < K:
            chungjeon += 1
            continue
        if bono[i] - bono[i - 1] > K:
            chungjeon = 0
            break
        if bono[i] + K > N:
            break

        for j in range(K, 1, -1):
            if bono[i] + j in bono:
                k += 1
        for j in range(K, 1, -1):
            if bono[i] + j in bono:
                chungjeon += 1
                break






    print("#{} {}".format(tc , chungjeon))


