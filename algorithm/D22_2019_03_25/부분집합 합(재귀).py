count = 0
N = 10
arr = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 가지치기 없이
# def printset(n):
#     sum1 = 0
#     idx = []
#     for i in range(len(arr)):
#         if arr[i] == 1:
#             sum1 += data[i]
#             idx.append(i)
#     if sum1 == 10:
#         for i in range(len(idx)):
#             print(data[idx[i]], end="")
#         print()
#
#
# def powerset(n, k):
#     if n == k:
#         printset(n)
#     else:
#         arr[k] = 1
#         powerset(n, k+1)
#         arr[k] = 0
#         powerset(n, k+1)
#
# powerset(N, 0)



def printset(n):

    count += 1
    for i in range(len(arr)):
        if arr[i] == 1:
            print(data[i], end="")
    print()


def powerset(n, k, sum1):
    global count
    if sum1 > 10:
        return

    if n == k:
        if sum1 == 10:
            printset(n)

    else:
        arr[k] = 1
        powerset(n, k+1, sum1+data[k])
        arr[k] = 0
        powerset(n, k+1, sum1)

count = 0
powerset(N, 0, 0)
print("호출횟수 : {}".format(count))