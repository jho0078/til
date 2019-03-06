N, K = map(int, input().split())

table = [list(map(int, input().split())) for i in range(N)]

maxsum = 0
for y in range(N-K+1):
    for x in range(N-K+1):
        i = 0
        sum1 = 0
        while i < 4:
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            for k in range(K-1):
                x = x + dx[i]
                y = y + dy[i]
                sum1 += table[y][x]
            i += 1
        if sum1 > maxsum:
            maxsum = sum1
print(maxsum)


