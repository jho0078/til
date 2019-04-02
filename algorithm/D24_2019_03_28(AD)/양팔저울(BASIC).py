# 부분집합
def scale(s, n, w):
    if w in weight:
        result[weight.index(w)] = 'Y'

    if s == n:
        return

    scale(s+1, n, w)
    scale(s+1, n, w+chu[s])
    scale(s+1, n, w-chu[s])


N = int(input())
chu = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

chk = [0]*N
result = ['N']*M
scale(0, N, 0)
print(*result)