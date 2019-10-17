import heapq

def fill_queue(a):
    for i in matrix[a]:
        n, w = i
        if not visited[n]:
            heapq.heappush(que, (w,n))

def prim():
    cnt = 0
    visited[V] = 1
    fill_queue(V)

    while que:
        w, n = heapq.heappop(que)

        if visited[n]:
            continue

        visited[n] = 1
        cnt += w
        fill_queue(n)

    return cnt

V, E = map(int, input().split())
matrix = [[] for _ in range(V+1)]

visited = [0]*(V+1)
que = []

for _ in range(E):
    a, b, c = map(int,input().split())
    matrix[a].append((b,c))
    matrix[b].append((a,c))

print(prim())