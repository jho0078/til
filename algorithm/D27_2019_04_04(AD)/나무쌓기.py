# def solution(s, c, chk):
#     global MAX, flag
#
#     if s == N:
#         flag = 1
#         if c > MAX:
#             MAX = c
#         return
#
#     A = chk[:]
#
#     if A[data[s]] == 0:
#         A[data[s]] = 1
#         solution(s + 1, c, A)
#         A[data[s]] = 0
#
#     if A[2] == 1 or (A[1] == 1 and A[3] == 1):
#         t = [0] * 4
#         t[data[s]] = 1
#         solution(s+1, c+1, t)
#         t[data[s]] = 0
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     data = list(map(int, input().split()))
#     MAX = -0x7fffffff
#     check = [0]*4
#     flag = 0
#     solution(0, 1, check)
#     if flag == 1: print(MAX)
#     else: print(-1)


def solution(s, c, chk):
    global MAX, flag

    if s == N:
        flag = 1
        if c > MAX:
            MAX = c
        return

    if chk[data[s]] == 0:
        chk[data[s]] = 1
        solution(s + 1, c, chk)
        chk[data[s]] = 0

    if chk[2] == 1 or (chk[1] == 1 and chk[3] == 1):
        t = [0] * 4
        t[data[s]] = 1
        solution(s+1, c+1, t)
        t[data[s]] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    MAX = -0x7fffffff
    check = [0]*4
    flag = 0
    solution(0, 1, check)
    if flag == 1: print(MAX)
    else: print(-1)






