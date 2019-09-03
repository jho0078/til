def sumhoney(s, k, gethoney, profit):
    global total

    total = max(total, profit)

    if s == M:
        return

    for i in range(k, M):
        if gethoney + honeys[i] <= C:
            sumhoney(s+1, i+1, gethoney + honeys[i], profit + honeys[i]**2)


def sol(s, y, x, result):
    global MAX, total, honeys

    if s == 2:
        MAX = max(result, MAX)
        return

    j = x
    for i in range(y, N):
        while j <= N-M:
            total = 0
            honeys = A[i][j:j+M]
            sumhoney(0, 0, 0, 0)
            sol(s+1, i, j+M, result + total)
            j += 1
        j = 0


import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    visited = [[0]*N for i in range(N)]
    honeys = []
    MAX = 0
    total = 0
    sol(0, 0, 0, 0)

    print("#{} {}".format(tc, MAX))


