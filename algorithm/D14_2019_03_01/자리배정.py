def iswall(y, x):
    global C, R

    if y > R or y < 1 or x > C or x < 1:
        return True
    else:
        return False

def find(K):
    if K == 1:
        return 1, 1

    i = 0
    y = 1
    x = 1
    number = 1
    table = []

    while True:
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]

        ny = y + dy[i]
        nx = x + dx[i]

        if not iswall(ny, nx) and (nx,ny) not in table:
            table.append((x,y))
            # print(table)
            # print(i)
            y += dy[i]
            x += dx[i]
            number += 1

            if number == K:
                return x, y

        else:
            i = (i + 1)%4


# C, R = map(int, input().split())
# K = int(input())

C, R = 7, 6
K = 25

if K > C*R:
    print("0")
else:
    print(*find(K))



