import sys
sys.stdin = open("점심 식사시간.txt")



def powerset(s, n):
    if s == n:
        A = []
        B = []
        for i in range(len(t)):
            if t[i] == 1:
                A.append(S[i])
            else:
                B.append(S[i])
        # print(t)
        return

    t[s] = 1
    powerset(s+1, n)
    t[s] = 0
    powerset(s+1, n)


T = int(input())
for tc in range(1, 2):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    S = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                S.append([i,j])
    print(S)
    t = [0]*len(S)
    powerset(0, len(S))

