def Combination(n, r):
    global A, min_chai

    if r == 0:
        chai = abs((A - sum(t)) - sum(t))
        if chai < min_chai:
            min_chai = chai
    else:
        if n < r:
            return
        else:
            t[r-1] = tapes[n-1]
            Combination(n-1, r-1)
            Combination(n-1, r)

# 조합
N = int(input())
tapes = list(map(int, input().split()))
A = sum(tapes)
t = [0]*(N//2)
min_chai = 99999
Combination(N, N//2)
print(min_chai)


