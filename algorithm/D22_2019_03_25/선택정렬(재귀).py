# def SelectionSort(A):
#     n = len(A)
#     for i in range(0, n-1):
#         min = i
#         for j in range(i+1, n):
#             if A[j] < A[min]:
#                 min = j
#         temp = A[min]
#         A[min] = A[i]
#         A[i] = temp


def selectionsort(idx, A):
    n = len(A)
    mini = idx
    if idx == n-1:
        return

    for j in range(idx+1, n):
        if A[j] < A[mini]:
            mini = j
    A[mini], A[idx] = A[idx], A[mini]
    selectionsort(idx+1, A)

A = [5,2,7,1,3,8,9,3,5,2]
selectionsort(0, A)
print(A)