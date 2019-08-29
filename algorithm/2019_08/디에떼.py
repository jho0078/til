import sys
sys.stdin = open("디에떼_input.txt")

def sol(s, main_cards):
    global flag, MIN

    cards = main_cards[:]
    sort_cards = sorted(cards)
    reverse_cards = sorted(cards, reverse=True)

    # print(s, main_cards)

    if cards == sort_cards or cards == reverse_cards:
        # print(cards)
        if s < MIN:
            MIN = s
        return

    if s == 5:
        return

    k = 1
    start = N//2 - 1
    for i in range(N-1):
        for j in range(k):
            cards[start + 2*j], cards[start + 2*j + 1] = cards[start + 2*j + 1], cards[start + 2*j]

        sol(s+1, cards)
        if i >= N//2 - 1:
            start += 1
            k -= 1
        else:
            start -= 1
            k += 1

    # # 1
    # cards[2], cards[3] = cards[3], cards[2]
    # sol(s + 1, cards)
    #
    # # 2
    # cards[1], cards[2] = cards[2], cards[1]
    # cards[3], cards[4] = cards[4], cards[3]
    # sol(s + 1, cards)
    #
    # # 3
    # cards[0], cards[1] = cards[1], cards[0]
    # cards[2], cards[3] = cards[3], cards[2]
    # cards[4], cards[5] = cards[5], cards[4]
    # sol(s + 1, cards)
    #
    # # 4
    # cards[1], cards[2] = cards[2], cards[1]
    # cards[3], cards[4] = cards[4], cards[3]
    # sol(s + 1, cards)
    #
    # # 5
    # cards[2], cards[3] = cards[3], cards[2]
    # sol(s + 1, cards)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    MIN = 999
    sol(0, cards)

    if MIN == 999:
        print("#{} {}".format(tc, -1))
    else:
        print("#{} {}".format(tc, MIN))