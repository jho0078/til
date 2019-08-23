import sys
sys.stdin = open("특이한 자석_input.txt")

def sol(k, c):
    flag = [0,0,0,0,0]
    if k%2: rot = [0,c,-c,c,-c]
    else: rot = [0,-c,c,-c,c]
    flag[k] = 1
    for i in range(k-2,-1,-1):
        if M[i+1][6] != M[i][2]:
            flag[i+1] = 1
        else: break
    for i in range(k,4):
        if M[i-1][2] != M[i][6]:
            flag[i+1] = 1
        else: break
    for i in range(1,5):
        if flag[i] == 1 and rot[i] == 1:
            M[i-1].insert(0, M[i-1].pop(-1))
        elif flag[i] == 1 and rot[i] == -1:
            M[i-1].append(M[i-1].pop(0))

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    M = [list(map(int, input().split())) for i in range(4)]

    for i in range(K):
        k, c = map(int, input().split())
        sol(k,c)

    result = 0
    for i in range(4):
        result += M[i][0]*(2**i)

    print("#{} {}".format(tc, result))