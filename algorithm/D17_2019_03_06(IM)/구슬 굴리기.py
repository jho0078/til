import sys
sys.stdin = open("구슬 굴리기.txt")

w, h = map(int, input().split())
table = [[1 for _ in range(w+2)] for i in range(h+2)]
data = [list(map(int, list(input()))) for i in range(h)]
for i in range(h):
    for j in range(w):
        table[i+1][j+1] = data[i][j]
        if table[i+1][j+1] == 2:
            y = i + 1
            x = j + 1

for i in range(h+2):
    print(table[i])

N = int(input())
rotate = list(map(int, input().split()))
print(rotate, y, x)

# 위, 아래, 왼쪽, 오른쪽
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
idx = 0

count = 1
while idx < len(rotate):

    i = rotate[idx] - 1
    nx = x + dx[i]
    ny = y + dy[i]
    table[y][x] = 3
    if table[ny][nx] == 0:
        x = nx
        y = ny
        count += 1
    elif table[ny][nx] == 3:
        x = nx
        y = ny
    elif table[ny][nx] == 1:
        idx += 1

    for i in range(h + 2):
        print(table[i])
    print()

print(count)
