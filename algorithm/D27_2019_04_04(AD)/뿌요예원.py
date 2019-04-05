def solution():
    def pprint():
        for i in range(h):
            print(*board[i])
        print()

    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def gravity():
        for j in range(w):
            temp = []
            for i in range(h - 1, 0, -1):
                if board[i][j] != '.':
                    temp += [board[i][j]]
                    board[i][j] = '.'
            for t in range(len(temp)):
                board[h - t - 1][j] = temp[t]
        # pprint()

    def pang(i, j, color):
        nonlocal Flag
        queue = [(i, j)]
        candi = []
        while queue:
            i, j = queue.pop(0)
            for d in range(4):
                x = i + direction[d][0]
                y = j + direction[d][1]
                if 0 <= x < h and 0 <= y < w and (x, y) not in candi and board[x][y] == color:
                    queue += [(x, y)]
                    candi += [(x, y)]
        if len(candi) >= 4:
            Flag = True
            for x, y in candi:
                board[x][y] = '.'
            pprint()
            print(cnt)

    def finder():
        nonlocal Flag, cnt
        Flag = False
        for i in range(h):
            for j in range(w):
                if board[i][j] != '.':
                    pang(i, j, board[i][j])

        # gravity() #1
        # if Flag:
        #     cnt += 1
        #     return finder()

    Flag = True
    cnt = 0
    while Flag:
        finder()
        gravity()  # 1
        cnt += 1

    print(cnt)




T = int(input())
h, w = 12, 6
for tc in range(T):
    board = [list(input()) for _ in range(h)]
    solution()