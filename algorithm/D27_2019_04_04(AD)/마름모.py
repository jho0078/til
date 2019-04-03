def transform(c):
    if c <= "9":
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def decimal(a, N, k):
    for i in range(a, N, k):
        s = 0
        for j in range(k):
            s += transform(data[i + j]) * (16 ** (k - j - 1))
        A.append(s)

N, K = map(int, input().split())
data = list(input())
k = N//4

for i in range(1, k):
    data.insert(0, data[-i])

A = []
for i in range(k):
    decimal(i, N, k)

A = list(set(A))
A.sort(reverse=True)
print(A)
print(A[K-1])

c = 0x7fffffff