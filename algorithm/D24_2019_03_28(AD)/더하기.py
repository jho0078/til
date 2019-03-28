def solution(s, e, sum1):
    global flag, K

    if flag == 1:
        return
    if sum1 > K:
        return
    if sum1 == K:
        flag = 1
        return
    if s == e:
        return

    solution(s+1, e, sum1)
    solution(s+1, e, sum1+data[s])


T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    flag = 0
    solution(0, N, 0)
    if flag == 1:
        print("YES")
    else:
        print("NO")


