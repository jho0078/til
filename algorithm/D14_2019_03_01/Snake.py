import sys
sys.stdin = open("Snake2.txt")

def iswall(y, x):
    global N
    if y < 1 or x < 1 or y > N or x > N:
        return True
    else:
        return False

N = int(input())
print(N)
K = int(input())
table = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(K):
    r, c = map(int, input().split())
    table[r][c] = 1

L = int(input())
data = [input().split() for i in range(L)]
for i in range(N):
    print(table[i])
print(data)

x = 1
y = 1
i = 0
move = 0
idx = 0
# length = 1
<<<<<<< HEAD
body = []
=======
body = [(0, 0)]
>>>>>>> 39c518effd5c185f1dea453ce9806cd8d4341149
while True:

    # D(정방향), L(역방향)
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    ny = y + dy[i]
    nx = x + dx[i]

    if idx < len(data):
        if move < int(data[idx][0]):
            if not iswall(ny, nx) and table[ny][nx] != 2:
                if table[ny][nx] == 0:
                    body.insert(0, (y, x))
                    table[y][x] = 2

<<<<<<< HEAD
                    print(f'move: {move}')
                    for j in range(N + 1):
                        print(table[j])

=======
>>>>>>> 39c518effd5c185f1dea453ce9806cd8d4341149
                    y = ny
                    x = nx
                    eraser = body.pop(-1)
                    table[eraser[0]][eraser[1]] = 0
<<<<<<< HEAD
=======

>>>>>>> 39c518effd5c185f1dea453ce9806cd8d4341149
                    move += 1
                elif table[ny][nx] == 1:
                    body.insert(0, (y, x))
                    table[y][x] = 2
                    y = ny
                    x = nx
<<<<<<< HEAD

                    print(f'move: {move}')
                    for j in range(N + 1):
                        print(table[j])

                    move += 1

                print()
            elif iswall(ny, nx) or table[ny][nx] == 2:
                print(move+1)
                break

        elif move == int(data[idx][0]):
            if data[idx][1] == 'D':
                i = (i + 1)%4
                idx += 1
            else:
                i = (i - 1)%4
                idx += 1

    else:
        if not iswall(ny, nx) and table[ny][nx] != 2:
            body.insert(0, (y, x))
            table[y][x] = 2
            y = ny
            x = nx
            move += 1

            if table[ny][nx] == 0:
                eraser = body.pop(-1)
                table[eraser[0]][eraser[1]] = 0

        elif iswall(ny, nx) or table[ny][nx] == 2:
            print(move + 1)
            break




=======
>>>>>>> 39c518effd5c185f1dea453ce9806cd8d4341149

                    move += 1

                print()
            elif iswall(ny, nx) or table[ny][nx] == 2:
                print(move+1)
                break

        elif move == int(data[idx][0]):
            if data[idx][1] == 'D':
                i = (i + 1)%4
                idx += 1
            else:
                i = (i - 1)%4
                idx += 1

    else:
        if not iswall(ny, nx) and table[ny][nx] != 2:
            body.insert(0, (y, x))
            table[y][x] = 2
            y = ny
            x = nx
            move += 1

            if table[ny][nx] == 0:
                eraser = body.pop(-1)
                table[eraser[0]][eraser[1]] = 0

        elif iswall(ny, nx) or table[ny][nx] == 2:
            print(move + 1)
            break