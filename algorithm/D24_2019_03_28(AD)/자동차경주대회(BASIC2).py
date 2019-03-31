import sys
sys.stdin = open("자동차경주대회.txt")

def solution(s, n, d, t):
    global min_t

    if t > min_t:
        return

    if s == n+1:
        time.append(t)
        if t < min_t:
            min_t = t
        return

    if d - D[s] >= 0:
        solution(s+1, n, d-D[s], t)
    else:
        return
    solution(s + 1, n, M, t + T[s])



    # if d - D[s] >= 0:
    #     solution(s+1, n, d-D[s], t)
    #     solution(s+1, n, M, t+T[s])
    # else:
    #     d = M
    #     t += T[s]
    #     solution(s + 1, n, d - D[s], t)
    #     solution(s + 1, n, M, t + T[s])

M = int(input())
N = int(input())
D = list(map(int, input().split()))
T = list(map(int, input().split()))
# T.insert(0, 0)
T.append(0)
print(D)
print(T)
min_t = 100000
time = []
solution(0, N, M, 0)
print(time)
print(min_t)