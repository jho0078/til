import sys
sys.stdin = open("이진탐색_input.txt")
T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    P = data[0]
    Pa = data[1]
    Pb = data[2]
    end_a = end_b = P
    start_a = 1
    count_a = 0
    while start_a < end_a:
        middle_a = (start_a + end_a)//2
        count_a += 1
        if Pa == middle_a:
            break
        elif middle_a > Pa:
            end_a = middle_a
        else:
            start_a = middle_a

    count_b = 0
    start_b = 1
    while start_b < end_b:
        middle_b = (start_b + end_b)//2
        count_b += 1
        if Pb == middle_b:
            break
        elif middle_b > Pb:
            end_b = middle_b
        else:
            start_b = middle_b

    if count_a > count_b:
        result = "B"
    elif count_a < count_b:
        result = "A"
    else:
        result = 0

    print("#{} {}".format(tc, result))

