def solution(y1, x1, d1):

    # 동서남북 : 1234
    dr = [0,0,0,1,-1]
    dc = [0,1,-1,0,0]

    # L : 0, R : 1
    turn = [[0,0],[4,3],[3,4],[1,2],[2,1]]

    que = []
    que.append([d1, y1, x1, 0])

    while que:
        d, y, x, c = que.pop(0)
        for i in range(1, 4):
            

        for i in range(1, 4):












M, N = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]
V = [[[0]*N for i in range(M)] for i in range(5)]
y1, x1, d1 = map(int, input().split())
y2, x2, d2 = map(int, input().split())