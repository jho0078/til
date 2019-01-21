import sys
sys.stdin = open("electric_bus_input.txt")
T = int(input())
for tc in range(1, T+1):
    KNM = list(map(int, input().split()))
    data2 = list(map(int, input().split()))
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]

    data = [0]*(M+2)
    for j in range(1, M+1):
        data[j] = data2[j-1]
    data[M+1] = N

    j = 0
    ans = 0
    while j < M+1:
        if N - data[j] <= K:
            break
        if data[j+1] -data[j] > K:
            ans = 0
            break
        step = K
        next_station = 0
        for i in range(j, j+K):
            step -= (data[i + 1] - data[i])
            if step == 0:
                ans += 1
                next_station += 1
                break
            elif step > 0:
                next_station += 1
            else:
                ans += 1
                break
        j += next_station

    print("#{} {}".format(tc, ans))

# 2. 다른 풀이
# def find(data, K, N, M):
#     data.insert(0,0)
#     data.append(n)
#     last = 0
#     cnt = 0
#     for i in range(1, M+2):
#         if data[i] - data[i-1] > K:
#             return 0
#         if data[i] > last + K:
#             last = data[i-1]
#             cnt += 1
#     return cnt
