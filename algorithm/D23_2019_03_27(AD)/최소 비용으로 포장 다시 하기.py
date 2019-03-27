N = int(input())
a = list(map(int, input().split()))

# Bubble 정렬

k = 0
result = 0
for k in range(N-1):

    for i in range(k, k+2):
        for j in range(i+1, N):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    a[k+1] = a[k] + a[k+1]
    result += a[k+1]
    k += 1

print(result)

# 7
# 4 2 5 1 2 1 9
# 5
# 2 2 2 2 5

# # 삽입정렬
# for k in range(1, N):
#     a[k] += a[k-1]
#     sol += a[k]
#     temp = a[k]
#     for i in range(k+1, N):
#         if a[i] < temp:
#             a[i], a[i-1] = a[i-1], a[i]
#         else:
#             break
#
# print(sol)