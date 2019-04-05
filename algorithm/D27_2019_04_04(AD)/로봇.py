def solution(y1, x1, d1, y2, x2, d2):

    # 동서남북 : 1234
    dy = [0,0,0,1,-1]
    dx = [0,1,-1,0,0]

    # L : 0, R : 1
    turn = [[0,0],[4,3],[3,4],[1,2],[2,1]]

    que = []
    que.append([d1, y1, x1, 0])

    while que:
        d, y, x, c = que.pop(0)
<<<<<<< HEAD
        for i in range(1, 4):


        for i in range(1, 4):







=======
        if d == d2 and y == y2 and x == x2:
            return c
>>>>>>> 14b36fe28096291067bd0d6e717be8552ab33d16

        for k in range(1, 4):
            nx, ny = x + dx[d]*k, y + dy[d]*k
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                break
            if data[ny][nx] == 1:
                break

            if data[ny][nx] == 0 and V[d][ny][nx] == 0:
                V[d][ny][nx] = 1
                que.append([d,ny,nx,c+1])

        for i in range(2):
            if V[turn[d][i]][y][x] == 0:
                V[turn[d][i]][y][x] = 1
                que.append([turn[d][i],y,x,c+1])


M, N = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]
V = [[[0]*N for i in range(M)] for i in range(5)]
y1, x1, d1 = map(int, input().split())
y2, x2, d2 = map(int, input().split())
print(solution(y1-1,x1-1,d1,y2-1,x2-1,d2))