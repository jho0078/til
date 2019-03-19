import sys
sys.stdin = open("이진수2_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    result = ""
    while True:
        if N == 0:
            print("#{} {}".format(tc, result))
            break

        if len(result) >= 13:
            print("#{} {}".format(tc, "overflow"))
            break

        N *= 2
        if N >= 1:
            result += "1"
            N -= 1
        else:
            result += "0"
