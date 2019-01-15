import sys
sys.stdin = open("flatten_input.txt")

for tc in range(10):
    N = int(input())
    data = list(map(int, input().split()))

    for l in range(N):
        max = 0                        #반복할 때마다 max, min 값 환기
        min = 458888888
        for i in range(len(data)):
            if data[i] > max:
                max = data[i]
            if data[i] < min:
                min = data[i]

        for j in range(len(data)):
            if data[j] == max:
                data[j] -= 1
                break

        for k in range(len(data)):
            if data[k] == min:
                data[k] += 1
                break
    max = 0
    min = 458888888
    for m in range(len(data)):
        if data[m] > max:
            max = data[m]
        if data[m] < min:
            min = data[m]
    result = max - min

    print("#{} {}".format(tc, result))
