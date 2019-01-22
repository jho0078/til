import sys
sys.stdin = open("색칠하기_input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(10)] for _ in range(10)]
    count = 0

    for i in range(N):
        d = list(map(int, input().split()))
        r1 = d[0]
        c1 = d[1]
        r2 = d[2]
        c2 = d[3]
        color = d[4]

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                arr[j][k] += color
                if arr[j][k] == 3:
                    count += 1

    print("#{} {}".format(tc, count))

