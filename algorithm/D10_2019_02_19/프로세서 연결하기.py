import sys
sys.stdin = open("프로세서 연결하기_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxinos = [list(map(int, input().split())) for i in range(N)]
    for i in range(1, N-1):
        for j in range(1, N-1):
            if maxinos[i][j] == 1:

                for k in range(i):
                    if maxinos[i][j] == 1:
                        break
                else:
                    count += 1
                    total_length += i
