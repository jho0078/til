def selectionSort(a):
    for i in range(0, len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

data = [64, 25, 10, 22, 11]
selectionSort(data)
print(data)