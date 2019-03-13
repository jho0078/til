# nPr = n * n-1Pr-1

# a = [1, 2, 3]
# t = [0]*2
#
# def Perm(n, r, q):
#     if r == 0:
#         print(' '.join(map(str, t)))
#     else:
#         for i in range(n-1, -1, -1):
#             a[n-1], a[i] = a[i], a[n-1]
#             t[r-1] = a[n-1]
#             Perm(n-1, r-1, q)
#             a[n-1], a[i] = a[i], a[n-1]
#
# Perm(3, 2, 2)

a = [1, 2, 3]
