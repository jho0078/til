import sys
sys.stdin = open("number_card_input.txt")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # data = list(map(int, list(input())))
    data = input()
    counts = [0]*10
    max = 0
    for i in data:
        counts[int(i)] += 1
    for index, j in enumerate(counts):
        if j >= max:
            max = j
            number = index

    print("#{} {} {}".format(tc, number, max))

    # 2.enumerate 사용 x
    # for i in data:
    #     counts[int(i)] += 1
    # for j in range(1, 10):
    #     if max <= counts[j]:
    #         max = counts[j]
    #         max_index = j