import sys
sys.stdin = open("색종이 배치.txt")

def istype1():
    for y in range(102):
        for x in range(102):
            count = 0
            if data[y][x] == 1:
                dx = [1, -1, 0, 0, 1, 1, -1, -1]
                dy = [0, 0, 1, -1, 1, -1, 1, -1]
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if data[ny][nx] == 0:
                        count += 1

                if count == 4:
                    return 1

    return 4

data = [[0 for _ in range(102)] for _ in range(102)]

total_length = 0
for i in range(2):
    y, x, n, m = map(int, input().split())

    total_length += 2*(n + m)
    for i in range(y+1, y+m+1):
        for j in range(x+1, x+n+1):
            data[i][j] += 1

print(total_length)
for i in range(102):
    print(data[i])

# 면적 구하기
p = 0
for y in range(102):
    for x in range(102):
        if data[y][x] == 2:
            p += 1

print(p)
if p > 0:
    print(3)

else:
    # 둘레 길이
    length = 0
    for y in range(102):
        for x in range(102):
            if data[y][x] == 1:
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if data[ny][nx] == 0:
                        length += 1
    print(length)
    if length < total_length:
        print(2)

    else:
        print(istype1())




