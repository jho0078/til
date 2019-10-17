
while 1:
    w, h = map(int, input().split())
    if not w and not h:
        break

    data = [list(input()) for _ in range(h)]

    k = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] == '*':
                k += 1
                data[i][j] = k

            elif data[i][j] == 'O':
                data[i][j] = 0

    graph = [[0]*k for _ in range(k)]
