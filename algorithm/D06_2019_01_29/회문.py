import sys
sys.stdin = open("회문_input.txt")
T = int(input())

def compares(n, m):
    result = ""
    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2):
                if words[i][j + k] != words[i][j + m - k - 1]:
                    break
            else:
                return words[i][j:j+m]

    for i in range(n):
        for j in range(n - m + 1):
            for k in range(m // 2):
                if words[j + k][i] != words[j + m - k - 1][i]:
                    break
            else:
                for l in range(j, j + m):
                    result += words[l][i]
                return result

for tc in range(1, T+1):
    dummy = list(map(int, input().split()))
    N = dummy[0]
    M = dummy[1]
    words = [input() for i in range(N)]

    print("#{} {}".format(tc, compares(N, M)))