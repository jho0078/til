

def dessert(high, low):

    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]

    nx = x + dx[idx]
    ny = y + dy[idx]

    dessert(high, low)


import sys
sys.stdin = open("디저트 카페_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]




