import sys
sys.stdin = open("연산_input.txt")

def solution(N, M):
    Q.append([N, 0])
    c = 0
    while Q:
        t = Q.pop(0)
        n = t[0]
        c = t[1]
        if n == M:
            return c

        if n + 1 <= 1000000:
            Q.append([n + 1, c+1])
        Q.append([n - 1, c+1])
        if n * 2 <= 1000000:
            Q.append([n * 2, c+1])
        Q.append([n - 10, c+1])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = []
    print("#{} {}".format(tc, solution(N, M)))
