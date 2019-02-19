import sys
sys.stdin = open("토너먼트 카드게임_input.txt")

# 가위 바위 보
def win(x, y):
    # 가위: 바위, 바위: 보, 보: 가위
    windic = {1: 2, 2: 3, 3: 1}
    if windic[cards[x]] == cards[y]:
        return y
    elif windic[cards[y]] == cards[x]:
        return x
    else:
        if x < y:
            return x
        else:
            return y

# 분할정복
def tournament(start, end):
    if start - end == 1:
        return win(start, end)

    elif start == end:
        return start

    else:
        mid = (start + end)//2
        return win(tournament(start, mid), tournament(mid+1, end))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int, input().split()))
    print("#{} {}".format(tc, tournament(0, n-1)+1))











