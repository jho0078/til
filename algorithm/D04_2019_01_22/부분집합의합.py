import sys
sys.stdin = open("부분집합의합_input.txt")
T = int(input())
arr = []
for k in range(1, 13):
    arr.append(int(k))

for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    K = data[1]
    result = 0
    for i in range(1<<12):
        count = 0
        sum = 0
        for j in range(13):
            if i & (1<<j):
                count += 1
                sum += arr[j]
        if count == N and sum == K:
            result += 1

    print("#{} {}".format(tc, result))
