import sys
sys.stdin = open("view_input.txt")
T = 10   #test 횟수
for tc in range(10):
    ans = 0
    result = 0
    N =int(input())
    data = list(map(int, input().split()))

    for i in range(2, len(data)-2):
        # 처음 풀이
        # if data[i] >= data[i-2] + 1 and data[i] >= data[i-1] + 1 and data[i] >= data[i+1] + 1 and data[i] >= data[i+2] + 1:
        #     print(i+2)
        #     ans = data[i] - max(data[i-2], data[i-1], data[i+1], data[i+2])
        #     result += ans
        max_data = max(data[i-2], data[i-1], data[i+1], data[i+2])  #좌우 빌딩들 중 가장 높은 빌딩하고만 비교
        if data[i] > max_data:
            ans = data[i] - max_data
            result += ans


    print("#{} {}".format(tc+1, result))

    #강사님 풀이
    # for i in range(2, N-2):
    #     min = 4648431316843
    #     for j in range(5):
    #         if j != 2:
    #             if data[i] - data[i-2+j] < min:
    #                 min = data[i] data[i-2+j]
    #     if min > 0:
    #         ans += min
