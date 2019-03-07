import sys
sys.stdin = open("수열.txt")

N = int(input())
data = list(map(int, input().split()))

print(data)
count = 1
max_length = 0
for i in range(1, N):
    if data[i] >= data[i-1]:
        count += 1
    else:
        if count > max_length:
            max_length = count
        count = 1
if count > max_length:
    max_length = count

count = 1
for i in range(1, N):
    if data[i] <= data[i-1]:
        count += 1
    else:
        if count > max_length:
            max_length = count
        count = 1
if count > max_length:
    max_length = count

print(max_length)