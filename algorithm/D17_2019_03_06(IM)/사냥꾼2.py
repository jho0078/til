import sys
sys.stdin = open("사냥꾼.txt")

N = int(input())
table = [[0 for _ in range(N+2)] for i in range(N+2)]
data = [list(map(int, list(input()))) for i in range(N)]
for i in range(N):
    for j in range(N):
        table[i+1][j+1] = data[i][j]

rabbit = 0
for y in range(N):
    for x in range(N):
        if table[y][x] == 1:
            dx = [0, 1, 1, 1, 0, -1, -1, -1]
            dy = [-1, -1, 0, 1, 1, 1, 0, -1]

            for i in range(8):
                for h in range(1, N):
                    ny = y + dy[i] * h
                    nx = x + dx[i] * h
                    if table[ny][nx] == 0 or table[ny][nx] == 1:
                        break
                    elif table[ny][nx] == 2:
                        rabbit += 1
                        table[ny][nx] = 3
print(rabbit)


