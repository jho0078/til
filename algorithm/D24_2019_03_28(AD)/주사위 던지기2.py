def solution(s, e, sum):
    global M
    if s == e:
        if sum == M:
            print(*a)
        return

    if sum > M:
        return

    else:
        for i in range(1, 7):
            a[s] = i
            solution(s+1, e, sum+i)

N, M = map(int, input().split())
a = [0]*N
solution(0, N, 0)