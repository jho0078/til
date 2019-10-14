N = int(input())
table = [0]*160

for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, b):
        table[j] += 1

print(max(table))




