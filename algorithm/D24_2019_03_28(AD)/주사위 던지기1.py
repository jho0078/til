# 중복순열
def RedundantPermutation(s, n):
    global count

    if s == n:
        print(*t)
        count += 1
        return

    for i in range(6):
        t[s] = A[i]
        RedundantPermutation(s+1, n)
        t[s] = 0

# 중복순열(중복제외)
def RedundantPermutation2(s, n):
    global count

    if s == n:
        T = sorted(t)
        if T not in total:
            total.append(T)
            print(*t)
            count += 1
        return

    for i in range(6):
        t[s] = A[i]
        RedundantPermutation2(s+1, n)
        t[s] = 0

# 순열(모두 다른 수)
def RedundantPermutation3(s, n):
    global count

    if s == n:
        print(*t)
        count += 1
        return

    for i in range(6):
        if chk[i] == 0:
            t[s] = A[i]
            chk[i] = 1
            RedundantPermutation3(s + 1, n)
            t[s] = 0
            chk[i] = 0


N, M = map(int, input().split())
A = list(range(1,7))
t = [0]*N
count = 0

if M == 1:
    RedundantPermutation(0, N)
    # print(count)

elif M == 2:
    total = []
    RedundantPermutation2(0, N)
    # print(count)

else:
    chk = [0]*6
    RedundantPermutation3(0, N)
    # print(count)