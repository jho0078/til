n = int(input())
data = []
direction = []

for i in range(6):
    a, b = map(int, input().split())
    data.append([a,b])
    direction.append(a)

data.append(data[0])

for i in range(len(data)-1):
    if data[i][0] == 1 and data[i+1][0] == 3:
        smallsquare = data[i][1] * data[i+1][1]
    elif data[i][0] == 4 and data[i+1][0] == 1:
        smallsquare = data[i][1] * data[i+1][1]
    elif data[i][0] == 2 and data[i+1][0] == 4:
        smallsquare = data[i][1] * data[i+1][1]
    elif data[i][0] == 3 and data[i+1][0] == 2:
        smallsquare = data[i][1] * data[i+1][1]

bigsquare = 1
for i in range(len(direction)):
    if direction.count(direction[i]) == 1:
        bigsquare *= data[i][1]

area = (bigsquare - smallsquare)*n
print(area)