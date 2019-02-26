V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))
items = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(0, len(data), 2):
    items[data[i]][data[i+1]] = 1
    items[data[i+1]][data[i]] = 1


def bfs(v):
    global V
    visited = [0] * (V+1)
    queue = []
    queue.append(v)

    while queue:
        t = queue.pop(0)
        if visited[t] == 0:
            visited[t] = 1
            print(t, end=" ")
        for i in range(len(items)):
            if items[t][i] == 1 and visited[i] == 0:
                queue.append(i)

bfs(1)