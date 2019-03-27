# Merge Sort
# 양쪽 비교대상이 하나가 될 때까지 (start와 end가 같아질 때까지) 반씩 쪼갠다.
# 왼쪽 구역과 오른쪽 구역의 값을 하나씩 비교해가면서 임시 리스트에 저장
# T : 임시리스트 인덱스
# L : 왼쪽 구역 인덱스
# R : 오른쪽 구역 인덱스

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

a = [5,3,1,6,4,2]
print(a)
N = len(a)
MergeSort(0, N-1)
print(a)