# arr = [1,2,3]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n+1):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()

arr = [-7,-3,-2,5,8]
n = len(arr)

def my_sum(a):
    sum_1 = 0
    for k in a:
        sum_1 += k
    return sum_1

for i in range(1, 1<<n):
    list_a = []
    for j in range(n+1):
        if i & (1<<j):
            list_a.append(arr[j])
    if my_sum(list_a) == 0:
        print(list_a)
print()


for i in range(1, 1<< len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1<<j): sum += arr[j]

    if summ == 0:
        for k in range(len(arr)):
            if i & (1<<j):
                print(arr[j], end=" ")
        print()
