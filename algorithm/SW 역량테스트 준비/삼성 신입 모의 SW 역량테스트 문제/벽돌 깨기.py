import sys
sys.stdin = open("벽돌 깨기.txt")

def fall():
    for i in range(W):
        for j in range(H):
            if A[i][j] > 0:
                a.append([])


def delete(y, x, k, copyA):

    stack1 = []
    que = []
    que.append([y,x,k])
    stack1.append([y,x,k])

    while que:
        y, x, k = que.pop()

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            for h in range(1, k):
                nx, ny = x + dx[i]*h, y + dy[i]*h
                if ny < 0 or nx < 0 or ny >= W or nx >= H:
                    break
                if copyA[ny][nx] > 0:
                    copyA[nx]
                    que.append([ny, nx, copyA[ny][nx]])
                    stack1.append([ny, nx, copyA[ny][nx]])

    return stack1


def solution(c, A):
    if c == N:
        return

    for i in range(W):
        for j in range(H-1, -1, -1):
            if A[i][j] > 0:
                copyA = [A[i][:] for i in range(W)]
                delete(i, j, A[i][j], copyA)
                fall()
                solution(c+1)

                break


T = int(input())
for tc in range(1, 2):
    N, W, H = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(H)]
    A = [[0]*H for i in range(W)]
    # for i in range(W):
    #     for j in range(H):
    #         A[i][j] =

    for i in range(W):
        for j in range(H):
            A[i][j] = table[H-j-1][i]

    solution(0, A)


