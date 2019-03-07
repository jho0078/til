import sys
sys.stdin = open("경비원.txt")

def transform(a, b):
    global h, w
    x = 0
    y = 0
    if a == 1:
        x += b
    elif a == 2:
        x += b
        y += h
    elif a == 3:
        y += b
    else:
        x += w
        y += b
    return y, x

w, h = map(int, input().split())
N = int(input())

table = [[0 for i in range(w+1)] for i in range(h+1)]

stores = []
k = 3
for i in range(N):
    a, b = map(int, input().split())
    y, x = transform(a,b)
    table[y][x] = k
    k += 1
    stores.append((y, x))

a, b = map(int, input().split())
y, x = transform(a,b)
table[y][x] = 2

print(stores, [y, x])
for i in range(h+1):
    print(table[i])

length = 0
for i in range(N):
    if abs(y - stores[i][0]) == h:
        if x + stores[i][1] > w:
            length += w*2 - (x + stores[i][1]) + h
            print(i, length)
        else:
            length += x + stores[i][1] + h
            print(i, length)

    elif abs(x - stores[i][1]) == w:
        if y + stores[i][0] > h:
            length += h*2 - (y + stores[i][0]) + w
            print(i, length)
        else:
            length += y + stores[i][0] + w
            print(i, length)

    else:
        length += abs(y - stores[i][0]) + abs(x - stores[i][1])
        print(i, length, 1)

print(length)



