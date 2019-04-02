def solution(s, N, d):
    global maxd

    if s == N:
        # print(A)
        # print(B)
        if d > maxd:
            maxd = d
        return

    if data[s] < A[-1]:
        A.append(data[s])
        solution(s+1, N, d+data[s])
        A.pop(-1)
    if data[s] > B[-1]:
        B.append(data[s])
        solution(s+1, N, d+data[s])
        B.pop(-1)
    solution(s+1, N, d)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    A = [10000]
    B = [0]
    maxd = 0
    solution(0, N, 0)
    print(maxd)
