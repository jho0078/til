import sys
sys.stdin = open("min_max_input.txt")
T = int(input())   #test 횟수
for tc in range(T):
    max = 0
    min = 458888888
    result = 0
    N = int(input())
    data = list(map(int, input().split()))

    for i in range(N):
        if data[i] > max:
            max = data[i]
        if data[i] < min:
            min = data[i]
    result = max - min



    print("#{} {}".format(tc+1, result))

    #2. max, min을 첫번째 값으로 잡고 시작
    #
    # N = int(input())
    # data = list(map(int, input().split()))
    # result = 0
    # max = data[0]
    # min = data[0]
    #
    # for i in range(1, N):
    #     if data[i] > max:
    #         max = data[i]
    #     if data[i] < min:
    #         min = data[i]
    # result = max - min

