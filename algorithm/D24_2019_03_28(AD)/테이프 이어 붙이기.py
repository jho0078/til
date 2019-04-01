def Combination(n, r):
    if r == 0:
        print(*t)
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
t = [0]*(N//2)
Combination(N, N//2)


