import sys
sys.stdin = open("그래프 경로_input.txt")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    for i in range(E):
        a, b = map(int, input().split())
