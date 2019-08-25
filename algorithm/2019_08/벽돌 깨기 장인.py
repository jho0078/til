import sys
sys.stdin = open("벽돌 깨기_input.txt")

def dfs(n, org_count, org_box):
    global result
    if n == N or not org_count: result = min(result, org_count); return

    for w in range(W):

        stack = list()
        for i in range(H):
            if org_box[i][w]:
                box = [b[:] for b in org_box]
                count = org_count - 1
                stack = [(i, w, box[i][w])]
                box[i][w] = 0
                break
        if not stack: continue

        while stack:
            y, x, length = stack.pop()
            for l in range(1, length):
                for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
                    if 0 <= y + dy * l < H and 0 <= x + dx * l < W and box[y + dy * l][x + dx * l]:
                        if box[y + dy * l][x + dx * l] > 1:
                            stack.append((y + dy * l, x + dx * l, box[y + dy * l][x + dx * l]))
                        box[y + dy * l][x + dx * l] = 0
                        count -= 1

        for j in range(W):
            last = H
            for i in range(H - 1, -1, -1):
                if not box[i][j]:
                    continue
                else:
                    if i != last - 1:
                        box[i][j], box[last - 1][j] = box[last - 1][j], box[i][j]
                    last -= 1
        dfs(n + 1, count, box)


T = int(input())
for test in range(1, T + 1):
    N, W, H = map(int, input().split())
    org_box = [list(map(int, input().split())) for _ in range(H)]
    result = sum(True for r in org_box for e in r if e)
    dfs(0, result, org_box)
    print(f"#{test} {result}")