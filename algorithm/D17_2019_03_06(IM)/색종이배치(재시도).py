def type():
    count = 0
    for i in range(h2):
        for j in range(w2):
            if table[y2 + 1 + i][x2 + 1 + j] == 1:
                return 3
            if table[y2 + 1 + i][x2 + 1 + j] == 2:
                count += 1

    if count == 1:
        return 1
    elif count > 1:
        return 2
    else:
        return 4

table = [[0 for _ in range(102)] for _ in range(102)]

y1, x1, w1, h1 = map(int, input().split())
y2, x2, w2, h2 = map(int, input().split())

for i in range(h1+2):
    for j in range(w1+2):
        table[y1+i][x1+j] = 2

for i in range(h1):
    for j in range(w1):
        table[y1+1+i][x1+1+j] = 1
#
# for i in range(100):
#     print(table[i])

print(type())



