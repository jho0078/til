# def fastsum(n):
#     if n == 1:
#         return 1
#     elif n%2 == 1:
#         return fastsum(n-1) + n
#     else:
#         return 2*fastsum(n//2) + n*n//4
#
# print(fastsum(100000))

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a+b)

