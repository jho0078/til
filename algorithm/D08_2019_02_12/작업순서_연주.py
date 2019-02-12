for t in range(10):
    V, E = map(int, input().split())  # V : 정점의 수/E:간선의 수
    data = list(map(int, input().split()))
    V += 1
    graph = [[0 for _ in range(V)] for _ in range(V)]

    for i in range(E):
        graph[data[i * 2]][data[i * 2 + 1]] = 1
    # 시작점 후보 찾기 (indegree 수:해당 정점에서 일하기 전에 미리 작업해야 하는 정점 수)
    indegree = [0] * V
    for j in range(E):
        indegree[data[j * 2 + 1]] += 1  # 예 : 1 4 2 3 4 2 에서 index 4, 3, 2에 +1

    instack = []
    print('#{}'.format(t + 1), end=' ')
    for id in range(1, V):
        if indegree[id] == 0:
            instack.append(id)  # 오는 간선 없는애들 모으자! 무조건 여기 안 정점에서 출발해야함
    while len(instack) > 0:
        s = instack.pop()  # 들어온 애들부터 (바로 직전에 작업한 정점때문에 append->뒤에서부터 차례대로 마저 작업 (Stack pop)
        print(s, end=" ")
        for j in range(1, V):
            if graph[s][j] == 1:
                indegree[j] -= 1  # i는 작업을 마쳤으니 i와 연결된 j 정점을 작업하기 전 미리 작업해야 하는 수-1
                if indegree[j] == 0:
                    instack.append(j)
    print()