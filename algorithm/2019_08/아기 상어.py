import sys
sys.stdin = open("아기 상어_input.txt")

def bfs(y, x):
    size = 2
    q = []
    q.append((y, x))
    V[y][x] = 1
    V = [[0]*N for _ in range(N)]
    while q:
        y, x = q.pop()
        for dy, dx  in (1,0), (-1,0), (0,1), (0,-1):
            ny, nx = y + dy, x + dx
            if -1 < dy < N and -1 < dx < N and not V[ny][nx]:
                if A[ny][nx]
                q.append((ny, nx))
                V[ny][nx] = V[y][x] + 1

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

fish = []
for i in range(N):
    for j in range(N):
        if 0 < A[i][j] < 7:
            fish.append((i, j, A[i][j]))
        elif A[i][j] == 9:
            shark = (i, j)

sol(shark[0], shark[1])