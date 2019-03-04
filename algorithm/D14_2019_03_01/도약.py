import sys
sys.stdin = open("도약.txt")

def secondrange(i):
    global N
    for j in range(i, N):
        if data[j] > (data[i] + data[N-1])//2:
            return j-1

N = int(input())

data = []
for i in range(N):
    data.append(int(input()))

data.sort()
print(data)

count = 0
for i in range(N-2):
    # print(secondrange(i))
    for j in range(i+1, secondrange(i)+1):
        for k in range(j+1, N):
            # print(i, j, k)
            if data[k] - data[j] >= data[j] - data[i]:
                if data[k] - data[j] <= (data[j] - data[i])*2:
                    print(data[i], data[j], data[k])
                    count += 1

                elif data[k] - data[j] > (data[j] - data[i])*2:
                    break

print(count)