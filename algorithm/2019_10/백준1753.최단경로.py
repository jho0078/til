import heapq

def dijkstra():
    D = [0x7fffffff] * (V + 1)
    D[K] = 0

    que = []
    heapq.heappush(que, (0, K))

    while que:
        weight1, n1 = heapq.heappop(que)
        for i in graph[n1]:
            n2, weight2 = i

            if D[n2] > D[n1] + weight2:
                D[n2] = D[n1] + weight2
                heapq.heappush(que, (D[n2], n2))

    for i in range(1, V+1):
        if D[i] == 0x7fffffff:
            print("INF")
        else:
            print(D[i])

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra()



