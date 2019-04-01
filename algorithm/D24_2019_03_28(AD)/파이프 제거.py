def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def right(y, x):
    if not iswall(y, x):
        if table[y][x] == '1' or table[y][x] == '4' or table[y][x] == '5' or table[y][x] == '8' or table[y][x] == '9' or table[y][x] == 'A' or table[y][x] == 'B':
            queue.append([y, x])

def left(y, x):
    if not iswall(y, x):
        if table[y][x] == '1' or table[y][x] == '3' or table[y][x] == '6' or table[y][x] == '7' or table[y][x] == '8' or table[y][x] == 'A' or table[y][x] == 'B':
            queue.append([y, x])

def up(y, x):
    if not iswall(y, x):
        if table[y][x] == '2' or table[y][x] == '3' or table[y][x] == '4' or table[y][x] == '7' or table[y][x] == '8' or table[y][x] == '9' or table[y][x] == 'B':
            queue.append([y, x])

def down(y, x):
    if not iswall(y, x):
        if table[y][x] == '2' or table[y][x] == '5' or table[y][x] == '6' or table[y][x] == '7' or table[y][x] == '9' or table[y][x] == 'A' or table[y][x] == 'B':
            queue.append([y, x])

def solution(y, x):


    queue.append([y, x])

    while queue:
        t = queue.pop(0)
        y, x = t[0], t[1]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        if table[y][x] == '1':
            table[y][x] = 0
            right(y + dy[0], x + dx[0])
            left(y + dy[1], x + dx[1])
        elif table[y][x] == '2':
            table[y][x] = 0
            up(y + dy[3], x + dx[3])
            down(y + dy[2], x + dx[2])
        elif table[y][x] == '3':
            table[y][x] = 0
            right(y + dy[0], x + dx[0])
            down(y + dy[2], x + dx[2])
        elif table[y][x] == '4':
            table[y][x] = 0
            left(y + dy[1], x + dx[1])
            down(y + dy[2], x + dx[2])
        elif table[y][x] == '5':
            table[y][x] = 0
            left(y + dy[1], x + dx[1])
            up(y + dy[3], x + dx[3])
        elif table[y][x] == '6':
            table[y][x] = 0
            up(y + dy[3], x + dx[3])
            right(y + dy[0], x + dx[0])
        elif table[y][x] == '7':
            table[y][x] = 0
            up(y + dy[3], x + dx[3])
            right(y + dy[0], x + dx[0])
            down(y + dy[2], x + dx[2])
        elif table[y][x] == '8':
            table[y][x] = 0
            right(y + dy[0], x + dx[0])
            down(y + dy[2], x + dx[2])
            left(y + dy[1], x + dx[1])
        elif table[y][x] == '9':
            table[y][x] = 0
            left(y + dy[1], x + dx[1])
            down(y + dy[2], x + dx[2])
            up(y + dy[3], x + dx[3])
        elif table[y][x] == 'A':
            table[y][x] = 0
            right(y + dy[0], x + dx[0])
            up(y + dy[3], x + dx[3])
            left(y + dy[1], x + dx[1])
        elif table[y][x] == 'B':
            table[y][x] = 0
            right(y + dy[0], x + dx[0])
            up(y + dy[3], x + dx[3])
            left(y + dy[1], x + dx[1])
            down(y + dy[2], x + dx[2])

N = int(input())
X, Y = map(int, input().split())
table = [list(input()) for i in range(N)]
print(table)
print(X, Y)
queue = []
solution(Y, X)
count = 0
for i in range(N):
    for j in range(N):
        if table[i][j] != 0 and table[i][j] != '0':
            count += 1

for i in range(N):
    print(table[i])
print(count)