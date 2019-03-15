import sys
sys.stdin = open("농작물 수확하기_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, list(input()))) for i in range(N)]
    # print(table)

    sum1 = 0
    one = 1
    two = 2
    first_idx = N // 2
    a = 1
    for i in range(N):
        for j in range(a):
            sum1 += table[i][first_idx + j]
            # print(table[i][first_idx + j])

        if first_idx == 0:
            one = -one
            two = -two
        first_idx -= one
        a += two

    print("#{} {}".format(tc, sum1))
