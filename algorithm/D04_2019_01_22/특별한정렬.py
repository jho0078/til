import sys
sys.stdin = open("특별한정렬_input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    L = len(data)

    for i in range(0, L-1):
        for j in range(L-2, i-1, -1):
            if data[j] <= data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    result = []
    for k in range(5):
        result.append(data[k])
        result.append(data[L - k - 1])

    # 일반적인 경우
    # result = []
    # for k in range(N//2):
    #     result.append(data[k])
    #     result.append(data[L - k - 1])
    # if N%2 == 1:
    #     result.append(data[L // 2 + 1])

    print("#{} {}".format(tc, " ".join(list(map(str, result)))))

