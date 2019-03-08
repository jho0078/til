import sys
sys.stdin = open("1_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]

    chais = []
    for y in range(N-K+1):
        for x in range(N-K+1):
            cross1 = 0
            cross2 = 0
            for i in range(K):
                cross1 += table[y+i][x+i]
                cross2 += table[y+i][x+K-1-i]
            chai = abs(cross1 - cross2)
            chais.append(chai)

    print("#{} {}".format(tc, min(chais)))




