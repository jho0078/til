import sys
sys.stdin = open("마을 위성사진.txt")

# def iswall(y, x):
#     if y < 0 or x < 0 or y > n-1 or x > n-1:
#         return True
#     else:
#         return False

def hill():
    height = 1
    while True:
        change = 0
        for y in range(1, n-1):
            for x in range(1, n-1):
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                count = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if data[ny][nx] >= height:
                        count += 1

                if count == 4:
                    data[y][x] = height + 1
                    change += 1

        print(height)
        for i in range(n):
            print(data[i])
        print()

        if change == 0:
            return height
        else:
            height += 1

n = int(input())
data = [list(map(int, list(input()))) for i in range(n)]
for i in range(n):
    print(data[i])
print()

p = 0
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            p += 1

if p == 0:
    print(0)
else:
    print(hill())


