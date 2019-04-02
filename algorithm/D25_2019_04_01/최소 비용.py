import sys
sys.stdin = open("최소비용_input.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

def solution(y, x):

    queue = []
    queue.append([y, x])
    visited[y][x] = 0
    while queue:
        t = queue.pop(0)
        y, x = t[0], t[1]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx):
                if table[ny][nx] > table[y][x]:
                    if visited[ny][nx] > visited[y][x] + 1 + (table[ny][nx] - table[y][x]):
                        visited[ny][nx] = visited[y][x] + 1 + (table[ny][nx] - table[y][x])
                        queue.append([ny, nx])
                else:
                    if visited[ny][nx] > visited[y][x] + 1:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append([ny, nx])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    visited = [[9999999999]*N for i in range(N)]
    solution(0, 0)
    for i in range(N):
        print(table[i])
    print()
    for i in range(N):
        print(visited[i])
    print("#{} {}".format(tc, visited[N-1][N-1]))