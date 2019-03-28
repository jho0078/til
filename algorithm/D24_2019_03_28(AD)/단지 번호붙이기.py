def iswall(y, x):
    if y < 0 or x < 0 or y >= n or x >= n:
        return True
    return False

def check(y, x):
    global count

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not iswall(ny, nx) and table[ny][nx] == 1:
            count += 1
            table[ny][nx] = 0
            check(ny, nx)


n = int(input())
table = [list(map(int, list(input()))) for i in range(n)]

a = []
for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            count = 1
            table[i][j] = 0
            check(i, j)
            a.append(count)


a.sort()
print(len(a))
for i in range(len(a)):
    print(a[i])
#
# for i in range(n):
#     print(table[i])