def solution(s, c):
    if s == N:
        return

    if c < 3:
        if data[s] not in A:
            A[c] = data[s]
            if data[s] == 2: A
        else:

    else:
        solution(s+1)



T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    solution(0, 0)
    A = [0]*3

