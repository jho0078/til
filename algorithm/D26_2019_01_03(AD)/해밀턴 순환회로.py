def permutation(s, n, d, idx):
    global MIN, count

    if s == n:
        count += 1
        # print(*t)
        if data[idx][0] != 0:
            total = d + data[idx][0]
            if total < MIN:
                MIN = total
        return

    if s == 0:
        chk[0] = 1
        permutation(s + 1, n, d, 0)

    if s >= 1:
        for i in range(N):
            if chk[i] == 0:
                if data[idx][i] == 0:
                    continue
                # t[s] = i
                chk[i] = 1
                permutation(s + 1, n, d + data[idx][i], i)
                chk[i] = 0

N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
chk = [0]*N
MIN = 100000000
count = 0
# t = [0]*N
permutation(0, N, 0, 0)
print(MIN)
# print(count)

