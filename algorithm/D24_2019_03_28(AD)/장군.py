# import sys
# sys.stdin = open("장군.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= 10 or x >= 9:
        return True
    return False

def solution(y, x):

    count = 1
    queue = []
    queue.append([y, x])
    visited[R1][C1] = 2

    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not iswall(ny, nx) and table[ny][nx] == 0:
                if i == 0 or i == 1:
                    dx1 = [dx[i], dx[i]]
                    dy1 = [-1, 1]
                else:
                    dx1 = [-1, 1]
                    dy1 = [dy[i], dy[i]]

                for j in range(2):
                    for k in range(1, 3):
                        nx1 = nx + dx1[j]*k
                        ny1 = ny + dy1[j]*k
                        if not iswall(ny1, nx1):
                            if k == 2:
                                if table[ny1][nx1] == 1:
                                    visited[ny1][nx1] = visited[y][x] + 1
                                    count = visited[ny1][nx1]
                                    return count - 2

                                elif table[ny1][nx1] == 0 and visited[ny1][nx1] == 0:
                                    visited[ny1][nx1] = visited[y][x] + 1
                                    count = visited[ny1][nx1]
                                    queue.append([ny1, nx1])

                            else:
                                if table[ny1][nx1] != 0:
                                    break
    return -1


R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
table = [[0]*9 for i in range(10)]
visited = [[0]*9 for i in range(10)]
table[R2][C2] = 1
print(solution(R1, C1))
for i in range(10):
    print(visited[i])





