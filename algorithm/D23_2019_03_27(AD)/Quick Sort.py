a = [5,3,1,6,4,2]
# Quick Sort
# pivot : 기준
# left : 비교대상
# target : 교환대상
# 비교 : pivot <-> left
# 교환 : left <-> target
# 처음 target은 처음 index로 설정, pivot은 마지막 놈
# left가 pivot보다 작으면
# start >= end 일 때 재귀를 멈춤

def QuickSort(s, e):
    if s >= e:
        return

    P, T = e, s
    for L in range(s, e):
        if a[L] < a[P]:
            a[L], a[T] = a[T], a[L]
            T += 1
    a[P], a[T] = a[T], a[P]

    QuickSort(s, T-1)
    QuickSort(T+1, e)

QuickSort(0, len(a)-1)
print(a)