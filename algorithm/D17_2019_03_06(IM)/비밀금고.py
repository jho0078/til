import sys
sys.stdin = open("비밀금고.txt")

N = int(input())
data = list(map(int, input().split()))

table = [[0 for _ in range(2*N-1)] for _ in range(2*N-1)]

a = 1
one = 1
for y in range(2*N-1):
    first_idx = N - a
    for i in range(a):
        table[y][first_idx + 2*i] = data.pop(0)
    if a == N:
        one = -one
    a += one

for i in range(2*N-1):
    print(table[i])

maxsum = 0
for i in range(2*N-1):
    if sum(list(zip(*table))[i]) > maxsum:
        maxsum = sum(list(zip(*table))[i])
print(maxsum)

for i in range(2*N-1):
    print(list(zip(*table))[i])

# maxsum = 0
# for i in range(2*N-1):
#     sum1 = 0
#     for j in range(2*N-1):
#         sum1 += table[j][i]
#     if sum1 > maxsum:
#         maxsum = sum1
# print(maxsum)