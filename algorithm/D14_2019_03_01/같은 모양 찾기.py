import sys
sys.stdin = open("같은 모양 찾기.txt")

M = int(input())
paper = [list(map(int, list(input()))) for i in range(M)]

P = int(input())
pattern = [list(map(int, list(input()))) for i in range(P)]

def compare(y, x):
    global P

    for i in range(P):
        for j in range(P):
            if paper[y+i][x+j] != pattern[i][j]:
                return 0
    return 1


def compare90(y, x):
    global P

    for i in range(P):
        for j in range(P):
            if paper[y+i][x+j] != pattern[P-1-j][i]:
                return 0
    return 1

def compare180(y, x):
    global P

    for i in range(P):
        for j in range(P):
            if paper[y+i][x+j] != pattern[P-1-i][P-1-j]:
                return 0
    return 1

def compare270(y, x):
    global P

    for i in range(P):
        for j in range(P):
            if paper[y+i][x+j] != pattern[j][P-1-i]:
                return 0
    return 1

count = 0
for y in range(M-P+1):
    for x in range(M-P+1):
        count += (compare(y, x) + compare90(y, x) + compare180(y, x) + compare270(y, x))

print(count)

