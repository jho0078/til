def check(m):
    res = 0
    for i in range(N):
        if trees[i] > m:
            res += trees[i] - m
    return res


def binarysearch(s, e):
    sum1 = sum(trees)

    while s <= e:
        m = (s+e)//2
        mine = check(m)
        if mine >= M:
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol


N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(binarysearch(1, max(trees)))
