def sol():
    global dust, T

    while T > 0:
        spread = {}

        for key, val in dust.items():
            count = 0
            y, x = key[0], key[1]
            for dy, dx in (1,0), (-1,0), (0,1), (0,-1):
                ny, nx = y + dy, x + dx
                if -1 < ny < R and -1 < nx < C and A[ny][nx] != -1:
                    count += 1
                    save[ny][nx] = A[y][x]//5
                    if (ny,nx) in spread:
                        spread[(ny,nx)] += A[y][x]//5
                    else:
                        spread[(ny,nx)] = A[y][x]//5

            save[y][x] += A[y][x] - (A[y][x]//5)*count
            spread[(y,x)] = A[y][x] - (A[y][x]//5)*count

        for i in range(R):
            print(save[i])
        print
        print(spread)
        move = {}
        for i in range(2):
            if i == 0:
                y, x = conditioner[0]
                d = [(0,1), (-1,0), (0,-1), (1,0)]
            else:
                y, x = conditioner[1]
                d = [(0,1), (1,0), (0,-1), (-1,0)]

            for j in range(4):
                while 1:
                    print(y, x)
                    ny, nx = y + d[j][0], x + d[j][1]
                    if ny < 0 or nx < 0 or ny > R - 1 or nx > C - 1:
                        break
                    else:
                        if (y, x) in spread:
                            move[(ny, nx)] = spread[(y, x)]
                        y, x = ny, nx



        dust = move
        T -= 1

    result = 0
    for val in dust.values():
        result += val

    return result

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for i in range(R)]
save = [[0]*C for i in range(R)]
dust = {}
conditioner = []

for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            dust[(i, j)] = A[i][j]
        elif A[i][j] == -1:
            conditioner.append([i,j])

print(dust)
print(conditioner)
print(sol())

