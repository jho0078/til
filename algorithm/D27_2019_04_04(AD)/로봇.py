def solution(y1, x1, d1):
    queue = []
    queue.append([y1,x1,d1,3])
    while queue:
        y, x, d, k = queue.pop(0)
        dx, dy = [1, 0, -1, 0], [0, 1, -1, 0]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if x >= 0 and y >= 0 and x <= N-1 and y <= N-1:
                if data[ny][nx] == 0:
                    if d == i+1
                        if  k > 0:
                            p = 1
                            if visited[ny][nx] > visited[y][x] + p:
                                queue.append([ny,nx,d,k-1])
                        else:
                            
                    elif d == i
                    if visited[ny][nx] > visited[y][x] + p



M, N = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]
visited = [[0]*N for i in range(M)]
y1, x1, d1 = map(int, input().split())
y2, x2, d2 = map(int, input().split())