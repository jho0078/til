def solution(s):
    global c

    chk[s] = 1
    c += 1
    for i in range(N+1):
        if table[s][i] == 1 and chk[i] == 0:
            solution(i)

N = int(input())
M = int(input())
table = [[0]*(N+1) for i in range(N+1)]
chk = [0]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    table[a][b] = table[b][a] = 1

c = 0
solution(1)
print(c-1)