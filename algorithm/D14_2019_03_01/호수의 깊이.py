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


while True:
    deep = 1
    p = 0
    for y in range(1, N+1):
        for x in range(1, N+1):
            if lake[y][x] == deep:
                dx = [1, -1, 0, 0]
                dy = [0 ,0, 1, -1]

                count = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if lake[ny][nx] >= deep:
                        count += 1

                if count == 4:
                    lake[y][x] = deep + 1
                    p = 1

    for k in range(len(lake)):
        print(lake[k])

    if p == 0:
        deepsum = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                deepsum += lake[i][j]
        print(deepsum)
        break

    deep += 1




