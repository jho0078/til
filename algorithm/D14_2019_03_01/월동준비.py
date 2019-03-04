import sys
sys.stdin = open("월동준비.txt")

def smart():
    max_value = 0
    for i in range(N):
        if acorns[i] > 0:
            max_value += acorns[i]

    if max_value > 0:
        return max_value
    else:
        return max(acorns)

def stupid():
    max_value = 0
    now = 0
    for i in range(N):
        if now + acorns[i] < 0:
            now = 0

        else:
            if now + acorns[i] > max_value:
                max_value = now + acorns[i]
            now = now + acorns[i]

    if max_value > 0:
        return max_value
    else:
        return max(acorns)


N = int(input())
acorns = list(map(int, input().split()))

print(stupid(), smart())


# def smart():
#     result = 0
#     max_of_minus = -10**(4)
#     for i in range(N):
#         if acorns[i] > 0:
#             result += acorns[i]
#
#         elif acorns[i] > max_of_minus:
#             max_of_minus = acorns[i]
#
#     if result > 0:
#         return result
#     else:
#         return max_of_minus