count = 0
N = 3
arr = [0 for _ in range(N)]
data = [1, 2, 3]

def printset(n):
    global count
    count += 1
    print("%d : " % (count), end="")
    for i in range(n):
        if arr[i] == 1:
            print("%d " % data[i], end="")
    print()

def powerset(n, k):
    if n == k:
        printset(n)
    else:
        arr[k] = 1
        powerset(n, k+1)
        arr[k] = 0
        powerset(n, k+1)

powerset(N, 0)