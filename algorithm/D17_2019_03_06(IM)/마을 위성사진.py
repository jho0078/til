# 예외사항
# 입력값이 모두 0일 때를 생각하자 !!!

N = int(input())
table = [[0 for _ in range(N+2)] for _ in range(N+2)]
data = [list(map(int, list(input()))) for i in range(N)]

for i in range(N):
    for j in range(N):
        table[i+1][j+1] = data[i][j]

for i in range(N+2):
    print(table[i])

h = 1
countzero = 0
while True:
    p = 0
    for y in range(1, N+1):
        for x in range(1, N+1):
            if table[y][x] == 0:
                countzero += 1
            if table[y][x] == h:
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                count = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if table[ny][nx] >= h:
                        count += 1
                if count == 4:
                    table[y][x] = h + 1
                    p = 1

    if countzero == N*N:
        print(0)
        break
    if p == 0:
        print(h)
        break
    h += 1


