def solution(s, C):
    global min_c

    if s == C:
        # print(damage)
        count = 0
        for i in range(N):
            if damage[i] > 0:
                count += 1
        if count < min_c:
            min_c = count
        return

    for i in range(N):
        if damage[i] > 0:
            for j in range(N):
                D = Dmemo[j][i]
                if D <= R:
                    damage[j] -= F
            solution(s+1, C)
            for j in range(N):
                D = Dmemo[j][i]
                if D <= R:
                    damage[j] += F


N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
S = []
damage = [0]*N
for i in range(N):
    S.append([data[i][0], data[i][1]])
    damage[i] = data[i][2]

Dmemo = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        Dmemo[i][j] = abs(S[i][0] - S[j][0]) + abs(S[i][1] - S[j][1])
# print(Dmemo)
# print(damage)
C, F, R = map(int, input().split())
min_c = 1000000
solution(0, C)
print(min_c)

# 3
# 100 100 40
# 100 200 80
# 300 500 40
# 2 40 100