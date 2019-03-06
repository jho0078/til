import sys
sys.stdin = open("사냥꾼.txt")

N = int(input())
table = [[0 for _ in range(N+2)] for i in range(N+2)]
data = [list(map(int, list(input()))) for i in range(N)]
for i in range(N):
    for j in range(N):
        table[i+1][j+1] = data[i][j]

# for i in range(N+2):
#     print(table[i])

rabbit = 0
for y in range(N):
    for x in range(N):
        if table[y][x] == 1:
            dx = [0, 1, 1, 1, 0, -1, -1, -1]
            dy = [-1, -1, 0, 1, 1, 1, 0, -1]

            idx = [0, 1, 2, 3, 4, 5, 6, 7]
            while idx:
                for h in range(1, N):
                    delist = []
                    for i in range(len(idx)):
                        ny = y + dy[idx[i]] * h
                        nx = x + dx[idx[i]] * h
                        if table[ny][nx] == 0 or table[ny][nx] == 1:
                            delist.append(idx[i])
                        elif table[ny][nx] == 2:
                            rabbit += 1
                            table[ny][nx] = 3

                    # for i in range(N + 2):
                    #     print(table[i])
                    # print()
                    # print(idx, delist, rabbit)
                    # print()
                    for i in range(len(delist)):
                        idx.remove(delist[i])

print(rabbit)


