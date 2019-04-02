import sys
sys.stdin = open("그룹 나누기_input.txt")

def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst():
    global M
    c = 0    # 간선 갯수
    i = 0    # 제어변수
    while c < M:
        p1 = findSet(data[i])
        p2 = findSet(data[i+1])
        if p1 != p2:
            p[p2] = p1
        c += 1
        i += 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    p = list(range(N + 1))
    mst()
    count = -1
    for i in range(len(p)):
        if p[i] == i:
            count += 1

    print("#{} {}".format(tc, count))
