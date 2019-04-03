def solution():
    queue = []
    queue.append([0,0])
    V[0][0] = 0

    while queue:
        y, x = queue.pop(0)
        dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= N-1 and ny <= N-1:
                if V[ny][nx] > V[y][x] + data[ny][nx]:
                    V[ny][nx] = V[y][x] + data[ny][nx]
                    queue.append([ny,nx])


N = int(input())
data = [list(map(int, list(input()))) for i in range(N)]
V = [[100000000]*N for i in range(N)]
solution()
print(V[N-1][N-1])
# print(V)
