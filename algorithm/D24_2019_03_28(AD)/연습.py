# def solution(s, start):
#     global n, m
#
#     if s == m:
#         print(*t)
#         return
#
#     for i in range(start, n):
#         t[s] = a[i]
#         solution(s+1, i+1)
#         t[s] = 0
#
# n = 5
# m = 3
# t = [0]*m
# a = [1,2,3,4,5]
# solution(0, 0)

# def solution2(s, start):
#     global n, m
#
#     if s == m:
#         print(*t)
#         return
#
#     for i in range(start, n):
#         t[s] = a[i]
#         solution2(s+1, i)
#         t[s] = 0
#
# n = 5
# m = 3
# t = [0]*m
# a = [1,2,3,4,5]
# solution2(0, 0)

def permutation(s):
    global n, m

    if s == m:
        print(t)
        return

    for i in range(n):
        if chk[i] == 0:
            chk[i] = 1
            t[s] = a[i]
            permutation(s+1)
            chk[i] = 0

n = 5
m = 3
t = [0]*m
a = [1,2,3,4,5]
chk = [0]*n
print(chk)
permutation(0)
