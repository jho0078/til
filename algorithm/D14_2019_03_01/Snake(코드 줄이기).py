import sys
sys.stdin = open("Snake2.txt")

def iswall(y, x):
    global N
    if y < 1 or x < 1 or y > N or x > N:
        return True
    else:
        return False

N = int(input())
K = int(input())
table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(K):
    r, c = map(int, input().split())
    table[r][c] = 1

L = int(input())
data = [input().split() for i in range(L)]

x = 1
y = 1
i = 0
time = 0
idx = 0
body = []
while True:

    # D(정방향), L(역방향)
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    ny = y + dy[i]
    nx = x + dx[i]

    if idx < len(data):
        if time < int(data[idx][0]):
            if not iswall(ny, nx) and table[ny][nx] != 2:
                body.insert(0, (y, x))
                table[y][x] = 2
                y = ny
                x = nx
                time += 1

                if table[ny][nx] == 0:
                    eraser = body.pop(-1)
                    table[eraser[0]][eraser[1]] = 0

            elif iswall(ny, nx) or table[ny][nx] == 2:
                print(time + 1)
                break

        elif time == int(data[idx][0]):
            if data[idx][1] == 'D':
                i = (i + 1) % 4
                idx += 1
            else:
                i = (i - 1) % 4
                idx += 1

    else:
        if not iswall(ny, nx) and table[ny][nx] != 2:
            body.insert(0, (y, x))
            table[y][x] = 2
            y = ny
            x = nx
            time += 1

            if table[ny][nx] == 0:
                eraser = body.pop(-1)
                table[eraser[0]][eraser[1]] = 0

        elif iswall(ny, nx) or table[ny][nx] == 2:
            print(time + 1)
            break