import sys, copy
sys.stdin = open("벽돌 깨기_input.txt")

def sol():
    global count, MIN

    A = copy.deepcopy(DATA)
    c = count

    # for m in range(W):
    #     print(A[m])
    # print()

    for l in range(len(pick)):
        x = pick[l]
        # 처음 부술 블럭 찾기
        flag = 0
        for i in range(H):
            if A[i][x] != 0:
                flag = 1
                y = i
                break

        if flag == 0:
            continue

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
                            if V[ny][nx] == 0:
                                V[ny][nx] = 1
                                if A[ny][nx] != 0:
                                    nq.append([ny, nx])
                                    pang.append([ny, nx])

            q = nq

        # 블럭 삭제
        for i in range(len(pang)):
            A[pang[i][0]][pang[i][1]] = 0
        #
        # for m in range(W):
        #     print(A[m])
        # print()


        # 떨어지기
        for x in range(W):
            blocks = []
            for y in range(H):
                if A[y][x] != 0:
                    blocks.append(A[y][x])
                    A[y][x] = 0
            for y in range(len(blocks)):
                A[H-1-y][x] = blocks[len(blocks)-1-y]

        c -= len(pang)

        # for m in range(W):
        #     print(A[m])
        # print()

    if c < MIN:
        MIN = c

def combination(s):
    global ccc

    # if MIN == 0:
    #     return

    if s == N:
        # print(pick)
        ccc += 1
        sol()
        return

    for i in range(W):
        pick[s] = i
        combination(s+1)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    DATA = [list(map(int, input().split())) for i in range(H)]
    MIN = 99999
    ccc = 0

    count = 0
    for i in range(H):
        for j in range(W):
            if DATA[i][j] != 0:
                count += 1

    pick = [0]*N
    combination(0)

    print(ccc)
    print("#{} {}".format(tc, MIN))



