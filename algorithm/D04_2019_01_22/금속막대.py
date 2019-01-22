import sys
sys.stdin = open("금속막대_input.txt")
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    arr = [[data[j] for j in range(i, i+2)] for i in range(0, n*2, 2)]

    for t in range(2*n):
        if data.count(data[t])%2 == 1 and t%2 == 0:
            first = data[t]

    for i in range(n):
        if arr[i][0] == first:
            arr[i], arr[0] = arr[0], arr[i]

    for i in range(n-2):
        for y in range(i, n):
            for x in range(2):
                if arr[0+i][1] == arr[y][0]:
                    arr[1+i], arr[y] = arr[y], arr[1+i]

    result = []
    for k in range(n):
        result.append(" ".join(list(map(str, arr[k]))))

    print("#{} {}".format(tc, " ".join(result)))









