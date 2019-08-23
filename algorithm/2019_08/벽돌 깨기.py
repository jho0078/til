import sys
sys.stdin = open("벽돌 깨기_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for i in range()]