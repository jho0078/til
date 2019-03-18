import sys
sys.stdin = open("홀수만 더하기_input.txt")

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    sum = 0
    for i in range(len(data)):
        if data[i]%2:
            sum += data[i]

    print("#{} {}".format(tc, sum))