def iswall(y, x):
    if y >= N or x >= N:
        return True
    else:
        return False

def right(ny, nx):
    global now
    if not iswall(ny, nx) and table[ny][nx] == 0:
        now = 0
        gogoring(ny, nx)

def down(ny, nx):
    global now
    if not iswall(ny, nx) and table[ny][nx] == 0:
        now = 2
        gogoring(ny, nx)

def cross(ny, nx):
    global now
    dx2 = [0, -1]
    dy2 = [-1, 0]
    if not iswall(ny, nx):
        for j in range(2):
            nx2 = nx + dx2[j]
            ny2 = ny + dy2[j]
            if table[ny2][nx2] == 1:
                break
        else:
            now = 1
            gogoring(ny, nx)

def gogoring(y, x):
    global now, count

    if y == N-1 and x == N-1:
        count += 1
        return
    dx = [1, 1, 0]
    dy = [0, 1, 1]
    # 오른쪽
    if now == 0:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if i == 0:
                right(ny, nx)
            else:
                cross(ny, nx)
    # 대각선
    elif now == 1:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if i == 0:
                right(ny, nx)
            elif i == 1:
                cross(ny, nx)
            else:
                down(ny, nx)
    # 아래
    else:
        for i in range(1, 3):
            nx = x + dx[i]
            ny = y + dy[i]
            if i == 2:
                down(ny, nx)
            else:
                cross(ny, nx)

N = int(input())
table = [list(map(int, input().split())) for i in range(N)]
# now : 현재상태 0: 오른쪽, 1: 대각선, 2: 아래
now = 0
count = 0
gogoring(0, 1)
print(count)