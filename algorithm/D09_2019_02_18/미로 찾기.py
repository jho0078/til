def iswall(y, x):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    else:
        return True

def miro(y, x):
    global data, flag

    dx = [1, 0, -1, 0] # 우, 하, 좌, 상
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if iswall(ny, nx) and data[ny][nx] == 2:
            flag = 1
            return

        elif iswall(ny, nx) and data[ny][nx] == 0:
            data[y][x] = 1
            miro(ny, nx)

data = [[0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 2, 1]]

n = len(data)
flag = 0
miro(0, 0)
print(flag)