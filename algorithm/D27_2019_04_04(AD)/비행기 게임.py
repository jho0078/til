def solution(x1, y1, b):

    queue.append([x1,y1])
    visited[x1][y1] = 0
    dx, dy = [-1, -1, -1], [-1, 0, 1]
    while queue:
        # print(queue)
        x, y = queue.pop(0)
        # print(x, y)
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and ny <= 4:
                if data[nx][ny] == '*':
                    s = 10
                elif data[nx][ny] == 'X':
                    if nx <= b and nx > b-5:
                        s = 0
                    else:
                        s = -7
                else:
                    s = 0

                if visited[nx][ny] < visited[x][y] + s:
                    visited[nx][ny] = visited[x][y] + s
                    queue.append([nx,ny])

    return max(visited[0])

T = int(input())
data = [list(input()) for i in range(13)]
# print(data)
queue = []
# print(solution(12, 0))
# for i in range(13):
#     print(visited[i])

MAX = -0x7fffffff
for i in range(11, 3, -1):
    visited = [[-0x7fffffff] * 5 for i in range(13)]
    a = solution(12, 2, i)
    for j in range(13):
        print(visited[j])
    print()
    if a > MAX:
        MAX = a
print(MAX)


