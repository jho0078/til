import sys
sys.stdin = open("최소신장트리_input.txt")

def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst():
    global V
    c = 0    # 간선 갯수
    s = 0    # 가중치의 합
    i = 0    # 제어변수
    while c < V:
        p1 = findSet(edge[i][0])
        p2 = findSet(edge[i][1])
        if p1 != p2:
            s += edge[i][2]
            c += 1
            p[p2] = p1
        i += 1
    return s


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for i in range(E)]

    edge.sort(key=lambda x : x[2])
    for i in range(E):
        print(edge[i])
    p = list(range(V+1))
    print("#{} {}".format(tc, mst()))
