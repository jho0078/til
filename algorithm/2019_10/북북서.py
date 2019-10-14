import sys
sys.stdin = open("input.txt")

def solution(direct):
    total = 0
    n = 0
    up = 0
    for d in direct:
        if d == 'n' or d == 'w':
            total += 1

    for i in range(len(direct) - 1, -1, -1):
        if direct[i] == 'n':
            if n:
                up -= 90 * (2 ** (total - n))
            n += 1
        elif direct[i] == 'w':
            if not n:
                up += 90 * (2 ** total)
            else:
                up += 90 * (2 ** (total - n))
            n += 1

    # print(up, 2**total)
    while not up % 2:
        if not up:
            return "0"

        if not up % 2 and total:
            up //= 2
            total -= 1

        if not total:
            return str(up)

    return str(up) + "/" + str(2**total)

T = int(input())
for tc in range(1, T+1):
    direct = input()

    print("#{} {}".format(tc, solution(direct)))
