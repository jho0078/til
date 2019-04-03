def distance(pick):
    dis = 0
    for i in range(len(home)):
        MIN = 10000
        for j in range(len(pick)):
            d = abs(home[i][0] - pick[j][0]) + abs(home[i][1] - pick[j][1])
            if d < MIN:
                MIN = d
        dis += MIN
    return dis

def combination(s, n, c):
    global min_d

    if c > M:
        return

    if s == n:
        if c == M:
            pick = []
            for i in range(len(chi)):
                if chk[i] == 1:
                    pick.append(chi[i])
            d = distance(pick)
            if d < min_d:
                min_d = d
        return

    chk[s] = 1
    combination(s+1, n, c+1)
    chk[s] = 0
    combination(s+1, n, c)


N, M = map(int, input().split())
table = [list(map(int, input().split())) for i in range(N)]


home = []
chi = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            home.append([i,j])
        if table[i][j] == 2:
            chi.append([i,j])

chk = [0]*len(chi)
min_d = 10000
combination(0, len(chi), 0)
print(min_d)
# print(h)
# print(c)


