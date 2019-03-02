import sys
sys.stdin = open("같은 모양 찾기.txt")

M = int(input())
paper = [list(map(int, list(input()))) for i in range(M)]

P = int(input())
pattern = [list(map(int, list(input()))) for i in range(P)]

def compare(y, x):
    global P
    count0 = 0
    count90 = 0
    count180 = 0
    count270 = 0

    for i in range(P):
        for j in range(P):
            if paper[y+i][x+j] == pattern[i][j]:
                count0 += 1
            if paper[y+i][x+j] == pattern[P-1-j][i]:
                count90 += 1
            if paper[y+i][x+j] == pattern[P-1-i][P-1-j]:
                count180 += 1
            if paper[y+i][x+j] == pattern[j][P-1-i]:
                count270 += 1

    if count0 == P*P or count90 == P*P or count180 == P*P or count270 == P*P:
        return 1
    else:
        return 0


count = 0
for y in range(M-P):
    for x in range(M-P):
        count += compare(y, x)

print(count)

