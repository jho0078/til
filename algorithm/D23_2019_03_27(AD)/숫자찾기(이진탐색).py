def BinarySearch(num, s, e):

    while s <= e:
        m = (s+e)//2
        if num == data[m]:
            return m + 1

        elif num > data[m]:
            s = m+1
        else:
            e = m-1

    return 0

N = int(input())
data = list(map(int, input().split()))
a = int(input())
numbers = list(map(int, input().split()))

for i in range(a):
    print(BinarySearch(numbers[i], 0, N-1))

