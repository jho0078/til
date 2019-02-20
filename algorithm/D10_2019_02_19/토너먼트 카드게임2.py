import sys
sys.stdin = open("토너먼트 카드게임_input.txt")

def win(x, y):
    # 가위: 바위, 바위: 보, 보: 가위
    windic = {1: 2, 2: 3, 3: 1}
    if windic[cards[x-1]] == cards[y-1]:
        return y
    elif windic[cards[y-1]] == cards[x-1]:
        return x
    else:
        if x < y:
            return x
        else:
            return y


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int, input().split()))

    def tournament(start, end):
        if end - start == 1:
            return win(start, end)

        elif start == end:
            return start

        mid = (start + end)//2

        return win(tournament(start, mid), tournament(mid+1, end))

    print("#{} {}".format(tc, tournament(1, n)))