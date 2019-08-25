import sys
sys.stdin = open("벽돌 깨기_input.txt")

def sol(n, COUNT, DATA):
    global MIN

    if n == N or not COUNT:
        MIN = min(MIN, COUNT)
        return

    for w in range(W):

        q = []
        # 처음 부술 블럭 찾기
        for i in range(H):
            if DATA[i][w]:
                data = [j[:] for j in DATA]
                count = COUNT - 1
                q = [(i, w, data[i][w])]
                data[i][w] = 0
                break
        if not q:
            continue

        # 블록 부수기
        while q:
            y, x, length = q.pop()
            for k in range(1, length):
                for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
                    ny, nx = y + dy * k, x + dx * k
                    if -1 < ny < H and -1 < nx < W and data[ny][nx]:
                        if data[ny][nx] > 1:
                            q.append((ny, nx, data[ny][nx]))
                        data[ny][nx] = 0
                        count -= 1

        # 떨어지기
        for x in range(W):
            idx = H - 1
            for y in range(H-1, -1, -1):
                if data[y][x]:
                    data[idx][x], data[y][x] = data[y][x], data[idx][x]
                    idx -= 1

        sol(n + 1, count, data)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(H)]
    count = sum(1 for x in origin for a in x if a)
    MIN = 9999
    sol(0, count, origin)
    print("#{} {}".format(tc, MIN))