T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    number = str(data[0])
    MAX = 0
    for i in range(1, N):
        if data[i] >= data[i-1]:
            number += str(data[i])
        else:
            MAX = max(int(number), MAX)
            number = str(data[i])

    if MAX:
        print(MAX)
    else:
        print(-1)