import sys
sys.stdin = open("반나누기.txt")

T = int(input())
for i in range(T):
    N, Kmin, Kmax = map(int, input().split())
    scores = list(map(int, input().split()))
    # print(N, Kmin, Kmax)
    # print(scores)
    max_score = max(scores)
    min_score = min(scores)

    chais = []
    for T1 in range(min_score+1, max_score):
        for T2 in range(T1+1, max_score+1):

            A = []
            B = []
            C = []

            for i in range(len(scores)):
                if scores[i] >= T2:
                    A.append(scores[i])
                elif scores[i] >= T1:
                    B.append(scores[i])
                else:
                    C.append(scores[i])

            if len(A) >= Kmin and len(A) <= Kmax:
                if len(B) >= Kmin and len(B) <= Kmax:
                    if len(C) >= Kmin and len(C) <= Kmax:

                        ban = [len(A), len(B), len(C)]
                        ban = sorted(ban)
                        # ban = sorted(list(set(ban)))
                        chai = ban[-1] - ban[0]
                        chais.append(chai)
    if chais:
        print(min(chais))
    else:
        print(-1)