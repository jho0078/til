def move(M):
    dx = [0, 0, 0, 1, -1]
    dy = [0, -1, 1, 0, 0]
    for i in range(M):



R, C, M = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]
table = [[0]*C for i in range(R)]

for i in range(M):
    table[data[i][1]][data[i][0]] = 1


king = 1
SUM = 0
while True:
    y = 0
    for i in range(M):
        if data[i][1] == king:
            if data[i][0] > y:
                y = data[i][0]
                idx = i

    if y == 0:
        move(M)
    else:
        SUM += data[idx][4]
        data.pop(idx)
        M -= 1
        move(M)

    king += 1




