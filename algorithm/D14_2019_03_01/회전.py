import sys
sys.stdin = open("회전.txt")




n = int(input())

data = [list(map(int, input().split())) for i in range(n)]


radius = 0
for i in range(100000):
    r = int(input())
    if r > 360:
        continue
    elif r == 0:
        break

    else:
        radius = (radius + r) % 360

        if radius == 0:
            for y in range(n):
                for x in range(n):
                    print(str(data[y][x]), end=' ')
                print()

        if radius == 90:
            for y in range(n):
                for x in range(n):
                    print(str(data[n-1-x][y]), end=' ')
                print()

        elif radius == 180:
            for y in range(n):
                for x in range(n):
                    print(str(data[n-1-y][n-1-x]), end=' ')
                print()

        elif radius == 270:
            for y in range(n):
                for x in range(n):
                    print(str(data[x][n-1-y]), end=' ')
                print()




