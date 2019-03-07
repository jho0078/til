import sys
sys.stdin = open("도약.txt")

N = int(input())

data = [int(input()) for i in range(N)]

data.sort()
print(data)

for i in range(N-2):
    for j in range(i+1, N-1):
        # for k in range(j+1, N):
        firstjummp = data[j] = data[i]
        low = j+1
        high = N



