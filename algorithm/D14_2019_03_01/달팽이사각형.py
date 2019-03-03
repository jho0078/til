def iswall(y, x):
    global n

    if y >= n or y < 0 or x >= n or x < 0:
        return True
    else:
        return False

def snail(n):

    i = 0
    y = 0
    x = 0
    data[y][x] = 1
    number = 1

    while True:
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        ny = y + dy[i]
        nx = x + dx[i]

        if not iswall(ny, nx) and data[ny][nx] == 0:
            y = ny
            x = nx
            number += 1
            data[y][x] = number

            if number == n*n:
                return

        else:
            i = (i + 1)%4

n = 4

data = [[0 for _ in range(n)] for _ in range(n)]
print(data)

if n == 1:
    print("1")
else:
    snail(n)
    for i in range(n):
        print(' '.join(map(str, data[i])))

