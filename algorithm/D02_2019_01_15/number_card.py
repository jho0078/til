import sys
sys.stdin = open("number_card_input.txt")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # data = list(map(int, list(input())))

    data = input()
    print(data)
    counts = [0]*10
    max = 0
    for i in data:
        counts[i] += 1
    for index, j in enumerate(counts):
        if j >= max:
            max = j
            number = index

    print("#{} {} {}".format(tc, number, max))