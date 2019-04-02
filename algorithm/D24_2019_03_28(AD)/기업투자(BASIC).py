# def solution(s, m, M, cost):
#     global maxcost
#
#     if M < 0:
#         return
#
#     if s == m:
#         # if sum(chk) == N:
#         print(t)
#         if cost > maxcost:
#             maxcost = cost
#         return
#
#     for i in range(1, N+1):
#         if chk[i-1] == 0:
#             chk[i-1] = 1
#             t[i-1] = data[s][i]
#             solution(s+1, m, M-data[s][0], cost + data[s][i])
#             t[i-1] = 0
#             chk[i - 1] = 0
#     solution(s+1, m, M, cost)


# M, N = map(int, input().split())
# data = [list(map(int, input().split())) for i in range(M)]
# # print(data)
# chk = [0]*N
# maxcost = 0
# t = [0]*N
# solution(0, M, M, 0)
# print(maxcost)

def solution(s, m, M, cost):
    global maxcost

    if M < 0:
        return

    if s == m:
        # if sum(chk) == N:
        print(t)
        if cost > maxcost:
            maxcost = cost
        return

    for i in range(1, M):
        if chk[i-1] == 0:
            chk[i-1] = 1
            t[i-1] = data[s][i]
            solution(s+1, m, M-data[s][0], cost + data[s][i])
            t[i-1] = 0
            chk[i - 1] = 0
    solution(s+1, m, M, cost)

M, N = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]
# print(data)
chk = [0]*N
maxcost = 0
t = [0]*N
solution(0, M, M, 0)
print(maxcost)