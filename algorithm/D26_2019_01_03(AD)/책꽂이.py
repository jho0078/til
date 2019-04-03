def subset(s, n, sum1):
    global B, min1

    if sum1 - B >= min1:
        return

    if s == n:
        if sum1 - B >= 0 and sum1 - B < min1:
            min1 = sum1 - B
        return

    subset(s+1, n, sum1)
    subset(s+1, n, sum1 + data[s])


T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    data = [int(input()) for i in range(N)]
    # print(data)
    min1 = 1000
    subset(0, N, 0)
    print(min1)