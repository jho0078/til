import sys
sys.stdin = open("Sum_input.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    print(arr)

    sum_max = 0
    sum_diagonal = 0
    sum_rdiagonal = 0
    for i in range(100):
        sum_diagonal += arr[i][i]
        sum_rdiagonal += arr[i][99-i]
        sum_array = 0
        sum_column = 0
        for j in range(100):
            sum_array += arr[i][j]
            sum_column += arr[j][i]
        if sum_array > sum_max:
            sum_max = sum_array
        if sum_column > sum_max:
            sum_max = sum_column
    if sum_diagonal > sum_max:
        sum_max = sum_diagonal
    if sum_rdiagonal > sum_max:
        sum_max = sum_rdiagonal

    print("#{} {}".format(tc, sum_max))







