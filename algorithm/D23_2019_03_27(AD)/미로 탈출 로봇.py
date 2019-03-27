def iswall(y, x):
    if y < 0 or x < 0 or y >= Y or x >= X:
        return True
    return False

def solution(x1, y1, x2, y2):

    queue = []
    queue.append([y1, x1])
    visited[y1][x1] = 1

    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx) and table[ny][nx] == 0 and visited[ny][nx] == 0:
                if ny == y2 and nx == x2:
                    return visited[y][x]

                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

    # 만약 큐가 없다면(주어진 도착지점에 도달하지 못하는 경우)
    return -1

X, Y = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

table = [list(map(int, list(input()))) for i in range(Y)]
visited = [[0]*X for i in range(Y)]

print(solution(x1-1, y1-1, x2-1, y2-1))