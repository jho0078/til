N, M = map(int, input().split())
table = [[0]*N for i in range(N)]

data = [list(map(int, input().split())) for i in range(N)]

color = [1]
flag = 0
for i in range(1, N):
    chk = [0] * N
    a = list(range(1, N))
    for j in range(len(data[i])):
        if data[i][j] == 1:
            if color[j] in a:
                a.remove(color[j])
    # print(a)
    b = min(a)
    if b > M:
        flag = 1
        break
    color.append(min(a))

if flag == 1: print(-1)
else: print(*color)