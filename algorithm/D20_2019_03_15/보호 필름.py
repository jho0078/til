import sys
sys.stdin = open("보호 필름_input.txt")

def input_drug(idx, drug, film):
    global W, D, K, out, min_drug

    if out == 1 or drug >= min_drug:
        return

    if idx == D:
        for x in range(W):
            flag = 0
            count = 1
            now = film[0][x]
            for y in range(1, D):
                if film[y][x] == now:
                    count += 1
                    if count == K:
                        flag = 1
                        break
                else:
                    now = film[y][x]
                    count = 1

            if flag == 0:
                return

        # 약품을 넣지 않아도 조건을 만족한다면 바로 재귀를 빠져나온다.
        if drug == 0:
            min_drug = 0
            out = 1
            return

        if drug < min_drug:
            min_drug = drug

    else:
        for j in range(-1, 2):
            copyfilm = [film[k][:] for k in range(D)]
            if j == -1:
                input_drug(idx+1, drug, copyfilm)
            else:
                for i in range(W):
                    copyfilm[idx][i] = j
                input_drug(idx+1, drug+1, copyfilm)


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(D)]

    if K == 1:
        min_drug = 0
        print("#{} {}".format(tc, min_drug))
    else:
        drugs = []
        out = 0
        min_drug = 10000
        input_drug(0, 0, table)

        print("#{} {}".format(tc, min_drug))





