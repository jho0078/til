# t = [0]*(2**31)
# end = 0
# N = int(input())
# for i in range(N):
#     a, b = map(int, input().split())
#     end = max(end, b)
#     for j in range(a, b):
#         t[j] = 1
#
# zero = 0
# one = 0
# max_zero = 0
# max_one = 0
# change = 0
# for i in range(end):
#     if t[i]:
#         if not one:
#             max_zero = max(max_zero, zero)
#         one += 1
#         zero = 0
#     else:
#         if not zero:
#             max_one = max(max_one, one)
#         zero += 1
#         one = 0
#
# print(max_one)
# print(max_zero)

N = int(input())
one = 0
end_time = 1
max_one = 0
max_zero = 0
for i in range(N):
    a, b = map(int, input().split())
    if a <= end_time:
        one += (b - end_time)
    else:
        max_one = max(max_one, one)
        max_zero = max(max_zero, (a-end_time))
        one = 0
    end_time = b

print(max_one)
print(max_zero)