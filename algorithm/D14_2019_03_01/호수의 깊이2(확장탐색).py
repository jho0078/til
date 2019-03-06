import sys
sys.stdin = open("호수의 깊이.txt")

N = int(input())

lake = [list(map(int, input().split())) for i in range(N)]
lake.insert(0, [0 for _ in range(N)])
lake.append([0 for _ in range(N)])
for i in range(N+2):
    lake[i].insert(0, 0)
    lake[i].append(0)

for i in range(N+2):
    print(lake[i])

for y in range(1, N+1):
    for x in range(1, N+1):
        if lake[y][x] == 1:
            dx = [1, -1, 0, 0]
            dy = [0 ,0, 1, -1]

            p = 0
            for a in range(1, N):
                for k in range(4):
                    nx = x + dx[k]*a
                    ny = y + dy[k]*a
                    if lake[ny][nx] == 0:
                        lake[y][x] = a
                        p = 1
                        break
                if p == 1:
                    break

deepsum = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        deepsum += lake[i][j]
print(deepsum)












