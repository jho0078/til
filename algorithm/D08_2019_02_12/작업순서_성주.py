def workhard(G, V):
    while len(result) < V:
        for j in SP:
            result.append(j)
            for i in G[j]:
                NS.pop(NS.index(i))
                if i not in NS:
                    SP.append(i)
            SP.pop(SP.index(j))

    return ' '.join(map(str, result))


for N in range(10):
    V, E = map(int, input().split())
    L = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    NS = [L[_] for _ in range(1, len(L), 2)]
    SP = [i for i in range(1, V + 1) if i not in NS]
    result = []
    # print(G)
    for i in range(0, len(L), 2):
        G[L[i]].append(L[i + 1])
    print(f'#{N + 1} {workhard(G, V)}')