def lowerSearch(s, e, data):
    lo = -1
    while s <= e:
        m = (s+e)//2
        if data == arr[m]:
            e = m - 1
            lo = m
        elif data > arr[m]:
            s = m + 1
        else:
            e = m - 1

    return lo

    # return -1 # 못찾으면 -1 리턴

def upperSearch(s, e, data):
    up = -1
    while s <= e:
        m = (s+e)//2
        if data == arr[m]:
            s = m + 1
            up = m
        elif data > arr[m]:
            s = m + 1
        else:
            e = m - 1

    return up

N = int(input())
arr = list(map(int, input().split()))
a = int(input())
numbers = list(map(int, input().split()))

for i in range(a):
    lo = lowerSearch(0, N-1, numbers[i])
    if lo == -1:
        print(0, end=" ")
        continue
    else:
        up = upperSearch(0, N-1, numbers[i])
        print(up-lo+1, end=" ")


# 함수 하나만 써서 찾기
def upperSearch2(s, e, data):
    up = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] < data:
            s = m + 1
            up = m
        else:
            e = m - 1
    return up

N = int(input())
arr = list(map(int, input().split()))
a = int(input())
numbers = list(map(int, input().split()))

for i in range(a):
    print(upperSearch2(0, N-1, numbers[i]+1) - upperSearch2(0, N-1, numbers[i]))