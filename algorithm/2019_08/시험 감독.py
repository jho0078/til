N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    result += 1
    k = A[i] - B
    if k > 0:
        result += k // C
        if k%C != 0:
            result += 1

print(result)
