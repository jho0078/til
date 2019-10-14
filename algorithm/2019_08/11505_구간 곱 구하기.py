N, M, K = map(int, input().split())
numbers = [int(input()) for i in range(N)]
for i in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        numbers[b-1] = c
    elif a == 2:
        result = 1
        for num in numbers[b-1:c]:
            result *= num
        print(result%1000000007)
