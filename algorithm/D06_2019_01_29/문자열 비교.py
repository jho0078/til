import sys
sys.stdin = open("문자열 비교_input.txt")
T = int(input())

# def compare(a, b):
#     for i in range(len(b)):
#         if b[i] == a[0]:
#             for j in range(1, len(a)):
#                 if b[i+j] != a[j]:
#                     break
#             else:
#                 return 1
#     return 0

def BruteForce(p, t):
    i = 0
    j = 0
    while j<len(p) and i<len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p):
        return 1
    else:
        return 0


for tc in range(1, T+1):
    word1 = input()
    word2 = input()
    print("#{} {}".format(tc, BruteForce(word1, word2)))





