import sys
sys.stdin = open("홈 방범 서비스_input.txt")

def soution():
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]

    for i in range(N):
        for j in range(N):
            solution(i, j)