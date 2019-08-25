# # 순열(n!)
# def permution(s, n):
#     global count
#
#     if s == n:
#         print(*t)
#         count += 1
#         return
#
#     for i in range(4):
#         if chk[i] == 0:
#             chk[i] = 1
#             t[s] = a[i]
#             permution(s + 1, n)
#             chk[i] = 0
#
#
# a = [1,2,3,4]
# n = 4
# chk = [0]*n
# t = [0]*n
# count = 0
# permution(0, n)
# print("경우의 수 : {}".format(count))
#
# # 순열(n개 중 m개 선택)
# def permution2(s, m):
#     global count
#
#     if s == m:
#         print(*t)
#         count += 1
#         return
#
#     for i in range(4):
#         if chk[i] == 0:
#             chk[i] = 1
#             t[s] = a[i]
#             permution2(s + 1, m)
#             chk[i] = 0
#
#
# a = [1,2,3,4]
# n = 4
# m = 2
# chk = [0]*n
# t = [0]*m
# count = 0
# permution2(0, m)
# print("경우의 수 : {}".format(count))
#
# # 중복순열(n^n)
# def mpermution(s, n):
#     global count
#
#     if s == n:
#         print(*t)
#         count += 1
#         return
#
#     for i in range(4):
#         t[s] = a[i]
#         mpermution(s + 1, n)
#
#
# a = [1,2,3,4]
# n = 4
# t = [0]*n
# count = 0
# mpermution(0, n)
# print("경우의 수 : {}".format(count))

# # 승주꿀이
# def Combinations(s, cnt):
#     global n
#
#     if cnt > 2:
#         return
#
#     if s == n:
#         if cnt == m:
#             for i in range(n):
#                 if t[i] != 0:
#                     print(t[i], end=" ")
#             print()
#         return
#
#     t[s] = a[s]
#     Combinations(s+1, cnt+1)
#     t[s] = 0
#     Combinations(s+1, cnt)
#
# n = 4
# m = 2
# a = [1, 2, 3, 4]
# t = [0]*n
# Combinations(0,0)

# 조합
# def Combination(s, start):
#     global n, m
#
#     if s == m:
#         print(t)
#         return
#
#     for i in range(start, 4):
#         t[s] = i
#         Combination(s+1, i+1)
#         t[s] = 0
#
# n = 4
# m = 2
# a = [1, 2, 3, 4]
# t = [0]*m
# Combination(0,0)

# 중복조합
def Combination2(s, start):
    global n, m

    if s == m:
        print(t)
        return

    for i in range(start, 7):
        t[s] = i
        Combination2(s+1, i)
        t[s] = 0

n = 4
m = 2
a = [1, 2, 3, 4]
t = [0]*m
Combination2(0,0)

b = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i, j in b:
    print(i, j)


# # 조합
# # nCr = n-1Cr-1 + n-1Cr , nC0 = 1
# def Combination(n, r):
#     if r == 0:
#         print(*T)
#     else:
#         if n < r:
#             return
#         else:
#             T[r-1] = a[n-1]
#             Combination(n-1, r-1)
#             Combination(n-1, r)
#
#
# n = 4
# m = 3
# T = [0]*m
# a = [1, 2, 3, 4]
# Combination(n, m)


# # 중복조합
# # nHr = nHr-1 + n-1Hr , nH0 = 1
# def Hombination(n, r):
#     if r == 0:
#         print(*T)
#     else:
#         if n < r:
#             return
#         else:
#             T[r-1] = a[n-1]
#             Hombination(n, r - 1)
#             Hombination(n - 1, r)
#
# n = 4
# m = 3
# T = [0]*m
# a = [1, 2, 3, 4]
# Hombination(n, m)