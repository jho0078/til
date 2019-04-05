def AllPairsShortest():
    global N

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                table[i][j] = min(table[i][k] + table[k][j], table[i][j])

def solution(s, d):
    global count

    if d <= 1:
        return

    for i in range(1, N+1):
        if table[s][i] != 0 and table[s][i] < d and visited[i] == 0:
            visited[i] = 1
            count += 1
            solution(i, d-table[s][i])


N, M, D = map(int, input().split())
table = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    table[a][b], table[b][a] = c, c

# 와샬-플로이드
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j and table[i][j] == 0:
            table[i][j] = 0x7fffffff
AllPairsShortest()

for i in range(N+1):
    print(table[i])

MAX = -0x7fffffff
for i in range(1, N+1):
    count = 1
    visited = [0] * (N + 1)
    visited[i] = 1
    solution(i, D)
    if count > MAX:
        MAX = count

print(MAX)

# 5 7 15
# 1 2 5
# 3 2 1
# 2 4 5
# 1 3 10
# 4 3 15
# 5 4 15
# 3 5 8