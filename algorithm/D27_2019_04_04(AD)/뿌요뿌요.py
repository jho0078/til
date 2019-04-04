def fall():
    for i in range(6):
        t = []
        for j in range(11, -1, -1):
            if D[j][i] != '.':
                t.append(D[j][i])
                D[j][i] = '.'
        for j in range(len(t)):
            D[11-j][i] = t[j]

def delete(x, y, c):
    global flag

    queue = []
    count = 1
    queue.append([x,y])
    if flag == 1:
        D[x][y] = '.'
        V2[x][y] = 1
    else:
        V[x][y] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= 11 and ny <= 5 and D[nx][ny] == c:
                if flag == 0 and V[nx][ny] == 0:
                    count += 1
                    if count == 4:
                        flag = 1
                        return
                    V[nx][ny] = 1
                    queue.append([nx,ny])

                if flag == 1 and V2[nx][ny] == 0:
                    D[nx][ny] = '.'
                    V2[nx][ny] = 1
                    queue.append([nx,ny])


T = int(input())
for tc in range(T):
    D = [list(input()) for i in range(12)]

    t = 0
    go = 1
    while go == 1:
        go = 0
        V = [[0] * 6 for i in range(12)]
        for i in range(12):
            for j in range(6):
                if D[i][j] != '.' and V[i][j] == 0:
                    flag = 0
                    delete(i, j, D[i][j])
                    if flag == 1:
                        go = 1
                        V2 = [[0] * 6 for i in range(12)]
                        delete(i, j, D[i][j])

        fall()
        if go == 1:
            t += 1

    print(t)
