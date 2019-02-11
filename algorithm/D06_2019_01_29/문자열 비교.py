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
            i = i - j     # 서로 다른 문자가 나올 시 비교를 처음 시작했던 자리로 이동
            j = -1        # j = 0 으로 초기화(아래에서 +1 하기 때문에 -1로 해줌)
        i = i + 1  #  i와 j를 1씩 더해가면서 비교
        j = j + 1
    if j == len(p):
        return 1
    else:
        return 0


for tc in range(1, T+1):
    word1 = input()
    word2 = input()
    print("#{} {}".format(tc, BruteForce(word1, word2)))





