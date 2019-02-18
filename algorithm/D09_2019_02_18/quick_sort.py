def PrintArray():
    for i in range(len(arr)):
        print("%3d" % arr[i], end=" ")
    print()

def partition(a, l, r):
    pivot = a[l]
    i = l
    j = r

    while i < j:
        # array의 왼쪽에서부터 pivot 보다 큰 값을 찾는다.
        while a[i] <= pivot:
            i += 1
            if(i == r): break

        # array의 오른쪽에서부터 pivot 보다 작은 값을 찾는다.
        while a[j] >= pivot:
            j -= 1
            if(j == l): break

        # 두 값의 위치를 바꾼다.
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quicksort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quicksort(a, low, pivot-1)
        quicksort(a, pivot+1, high)

arr = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
PrintArray()
quicksort(arr, 0, len(arr)-1)
PrintArray()