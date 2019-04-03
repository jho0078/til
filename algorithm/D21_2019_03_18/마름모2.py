def transform(c):
    if c <= "9":
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


N, K = map(int, input().split())
data = list(input())
k = N//4
print(k)
# print(data)

data.insert(0, data[-1])
data.insert(0, data[-2])
# print(data)
A = []
for i in range(0, N, k):
    A.append(transform(data[i])*(16**2) + transform(data[i+1])*16 + transform(data[i+2]))

for i in range(1, N, k):
    A.append(transform(data[i])*(16**2) + transform(data[i+1])*16 + transform(data[i+2]))

for i in range(2, N, k):
    A.append(transform(data[i])*(16**2) + transform(data[i+1])*16 + transform(data[i+2]))

A.sort(reverse=True)
print(A)
print(A[K-1])