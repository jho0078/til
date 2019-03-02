import sys
# from math import prod
from functools import reduce
sys.stdin = open("연속부분최대곱.txt")

n = int(input())
data = [float(input()) for i in range(n)]

print(data)

max_product = 1
now = 1
count = 0
for i in range(n):

    if now*data[i] < 1:
        now = 1
    else:
        if now*data[i] > max_product:
            max_product = now*data[i]
        now = now*data[i]

if max_product > 1:
    print('%.3f' % max_product)
else:
    print('%.3f' % max(data))
# if max_product > 1:
#     print(round(max_product, 3))
# else:
#     print(round(max(data), 3))

print(f'{3.4567:.3f}')
print(f'{3.4:.3f}')
print('%.3f' % 3.4567)
print('%.3f' % 3.4)
print('{0:.3f}'.format(3.4567))
print('{0:.3f}'.format(3.4))







# maxm = 0
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         multiply = 1
#         for k in range(j, j+i):
#             multiply *= data[k]
#
#         if multiply > maxm:
#             maxm = multiply
#
# print(round(maxm, 4))

# maxm = 0
# for i in range(1, n+1):
#     for j in range(n-i+1):
#         # multiply = prod(data[j:j+i])
#         multiply = reduce(lambda x, y: x*y, data[j:j+i])
#
#         if multiply > maxm:
#             maxm = multiply
#
# print(round(maxm, 4))

