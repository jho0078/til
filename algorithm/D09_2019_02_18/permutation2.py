# swap을 이용한 순열
def print_arr():
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def permutation(n, r):
    if r == 0:
        print_arr()
        return

    for i in range(n-1, -1, -1):
        arr[i], arr[n-1] = arr[n-1], arr[i]
        permutation(n-1, r-1)
        arr[i], arr[n - 1] = arr[n - 1], arr[i]


# arr = [1,2,3,4,5]
# # arr에서 배열할 수의 갯수
# pick = 5
# permutation(len(arr), 5)

arr = [1,2,3]
# arr에서 배열할 수의 갯수
pick = 3
permutation(len(arr), 3)