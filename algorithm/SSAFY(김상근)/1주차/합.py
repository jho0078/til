import sys
sys.stdin = open("합_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    now = 0
    maxsum = 0
    for i in range(N):
        if now + data[i] < 0:
            now = 0
        else:
            now = now + data[i]
            if now > maxsum:
                maxsum = now

    print("#{} {}".format(tc, maxsum))