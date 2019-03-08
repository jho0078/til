import sys
sys.stdin = open("참외밭.txt")

K = int(input())
data = []
for i in range(6):
    a, b = map(int, input().split())
    data.append([a, b])

print(data)

max_length = 0
for i in range(6):
    if data[i][1] > max_length:
        max_length = data[i][1]
        idx = i

if data[(idx - 1)%6][1] > data[(idx + 1)%6][1]:
    bigarea = max_length * data[(idx - 1)%6][1]
    smallarea = data[(idx + 2)%6][1] * data[(idx + 3)%6][1]
else:
    bigarea = max_length * data[(idx + 1) % 6][1]
    smallarea = data[(idx - 2)%6][1] * data[(idx - 3)%6][1]

area = (bigarea - smallarea)*K
print(area)
