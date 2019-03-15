import sys
sys.stdin = open("건초더미_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dummy = []
    for i in range(N):
        S = int(input())
        dummy.append(S)
    sum1 = sum(dummy)
    count = 0
    for i in range(len(dummy)):
        if dummy[i] > sum1//len(dummy):
            count += (dummy[i] - sum1//len(dummy))

    print("#{} {}".format(tc, count))
