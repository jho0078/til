import sys
sys.stdin = open("벽돌 깨기_input.txt")

def sol(x):
    # 처음 부술 블럭 찾기
    for i in range(H):
        if A[i][x] != 0:
            y = i

    # 삭제할 블럭 체크
    pang = []
    pang.append([y, x])
    V = [[0] * W for i in range(H)]

    q = []
    q.append([y, x])
    V[y][x] = 1

    while q:
        nq = []
        for i in range(len(q)):
            y, x = q[i][0], q[i][1]
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            for j in range(4):
                for k in range(1, A[y][x]):
                    ny = y + dy[j] * k
                    nx = x + dx[j] * k
                    if ny > -1 and nx > -1 and ny < H and nx < W:
                        if A[ny][nx] != 0 and V[ny][nx] == 0:
                            nq.append([ny, nx])
                            pang.append([ny, nx])
        q = nq

    # 블럭 삭제
    for i in range(len(pang)):
        A[pang[i][0]][pang[i][1]] = 0

    # 떨어지기
    for x in range(W):
        blocks = []
        flag = 0
        for y in range(H):
            if A[y][x] != 0:
                blocks.append(A[y][x])
                flag = 1
            elif flag == 1 and A[y][x] == 0:
                flag = 2
            elif flag == 2 and A[y][x] != 0:
                for i in range(len(blocks)):
                    A[y-1-i][x] = blocks[i]
                break




def combination(s):

    if s == N:
        print(temp)
        sol()
        return

    for i in range(0,W):
        temp[s] = i
        combination(s+1)

T = int(input())
for tc in range(1, 2):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]

    pang = []
    V = []
    temp = [0]*N

    combination(0)
