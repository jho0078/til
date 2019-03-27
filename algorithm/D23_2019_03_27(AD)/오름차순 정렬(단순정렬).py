N = int(input())
a = list(map(int, input().split()))

# # Bubble 정렬
# n = len(a)
#
# for i in range(n-1):
#     now = a[i]
#     for j in range(i+1, n):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
#
# print(*a)

# # Quick Sort
# def QuickSort(s, e):
#     if s >= e:
#         return
#
#     P, T = e, s
#     for L in range(s, e):
#         if a[L] < a[P]:
#             a[L], a[T] = a[T], a[L]
#             T += 1
#     a[P], a[T] = a[T], a[P]
#
#     QuickSort(s, T-1)
#     QuickSort(T+1, e)
#
# QuickSort(0, len(a)-1)
# print(*a)

# Merge Sort
def MergeSort(s, e):
    if s >= e:
        return

    m = (s+e)//2
    MergeSort(s, m)
    MergeSort(m+1, e)

    L, R, T = s, m+1, s

    temp = [0]*N
    while L <= m and R <= e:
        if a[L] < a[R]:
            temp[T] = a[L]
            T += 1
            L += 1
        else:
            temp[T] = a[R]
            T += 1
            R += 1

    # 왼쪽 부분이 다 안채워진 경우에 마저 채워준다.
    while L <= m:
        temp[T] = a[L]
        T += 1
        L += 1

    # 오른쪽 부분이 다 안채워진 경우에 마저 채워준다.
    while R <= e:
        temp[T] = a[R]
        T += 1
        R += 1

    # 임시 리스트에 정렬된 값들을 원본 리스트에 덮어쓴다.
    for i in range(s, e+1):
        a[i] = temp[i]

MergeSort(0, N-1)
print(*a)