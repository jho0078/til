R, C, M = map(int, input().split())
table = [[0]*C for _ in range(R)]
pos = {}

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    pos[(r-1, c-1)] = (s, d, z)
    table[r-1][c-1] = z

result = 0
for i in range(C):
    for j in range(R):
        if table[j][i]:
            result += z
