import sys
sys.stdin = open("경비원.txt")

w, h = map(int, input().split())
n = int(input())
stores = []
for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])

a, b = map(int, input().split())
if a == 1:
    my_length = b
elif a == 2:
    my_length = w + h + w - b
elif a == 3:
    my_length = 2*w + h + h - b
else:
    my_length = w + b

print(my_length)
result = 0
for i in range(len(stores)):
    if stores[i][0] == 1:
        length = stores[i][1]
    elif stores[i][0] == 2:
        length = w + h + w - stores[i][1]
    elif stores[i][0] == 3:
        length = 2*w + h + h - stores[i][1]
    else:
        length = w + stores[i][1]

    distance = abs(my_length - length)
    if distance > w + h:
        distance = 2 * (w + h) - distance
    result += distance

print(result)
