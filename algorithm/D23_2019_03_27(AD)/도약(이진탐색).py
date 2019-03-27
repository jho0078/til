import sys
sys.stdin = open("도약.txt")

# num 보다 작은 것들 중에서 가장 큰 값 탐색
def uppersearch(s, e, num):
    up = -1
    while s <= e:
        m = (s+e)//2
        if data[m] < num:  # num 보다 작으면 오른쪽 영역(더 큰값) 재탐색
            s = m + 1
            up = m
        else:
            e = m - 1
    return up

N = int(input())

data = []
for i in range(N):
    data.append(int(input()))

data.sort()
print(data)

count = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = data[j] + (data[j] - data[i])
        end = data[j] + (data[j] - data[i])*2
        up1 = uppersearch(j, N-1, start)
        up2 = uppersearch(j, N-1, end+1)
        count += up2 - up1

print(count)


