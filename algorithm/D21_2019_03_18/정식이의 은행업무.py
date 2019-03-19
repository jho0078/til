import sys
sys.stdin = open("정식이의 은행업무_input.txt")

def solution():
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(3):
                copya = a[:]
                copyb = b[:]
                if copya[i] == 0:
                    copya[i] = 1
                else:
                    copya[i] = 0

                if copyb[j] != k:
                    copyb[j] = k

                c = two(copya)
                d = three(copyb)
                if c == d:
                    return c

def two(copya):
    result = 0
    copya.reverse()
    for i in range(len(copya)):
        result += (2**i) * copya[i]

    return result

def three(copyb):
    result = 0
    copyb.reverse()
    for i in range(len(copyb)):
        result += (3**i) * copyb[i]

    return result


T = int(input())
for tc in range(1, T+1):
    a = list(map(int, input()))
    b = list(map(int, input()))

    print("#{} {}".format(tc, solution()))




