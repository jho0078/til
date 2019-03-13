import time


def iswall(y, x):
    if y >= N or x >= N:
        return True
    else:
        return False

def right(ny, nx):
    if not iswall(ny, nx) and table[ny][nx] == 0:
        gogoring(ny, nx, 0)

def down(ny, nx):
    if not iswall(ny, nx) and table[ny][nx] == 0:
        gogoring(ny, nx, 2)

def cross(ny, nx):
    if not iswall(ny, nx) and table[ny][nx] == 0:
        if table[ny-1][nx] == 0 and table[ny][nx-1] == 0:
            gogoring(ny, nx, 1)

def gogoring(y, x, status):
    global now, count

    if y == N-1 and x == N-1:
        count += 1
        return
    dx = [1, 1, 0]
    dy = [0, 1, 1]


    # 오른쪽
    if status == 0:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if i == 0:
                right(ny, nx)
            else:
                cross(ny, nx)
    # 대각선
    elif status == 1:
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
start_time = time.time()
table = [list(map(int, input().split())) for i in range(N)]
# now : 현재상태 0: 오른쪽, 1: 대각선, 2: 아래
now = 0
count = 0
gogoring(0, 1, 0)
print(count)
print("--- %s seconds ---" %(time.time() - start_time))