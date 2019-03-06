import sys
sys.stdin = open("초콜릿 공장.txt")

N = int(input())
count = 0
for i in range(N):
    L, H = input().split()
    for i in range(len(L)):
        if L.count(L[i]) >= 2:
            count += 1
            break
    for i in range(len(H)):
        if H.count(H[i]) >= 2:
            count += 1
            break

    overlap = 0
    for i in range(len(L)):
        if L[i] in H:
            overlap += 1
    if overlap > 2:
        count += 1

print(count)
