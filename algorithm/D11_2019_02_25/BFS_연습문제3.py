# V, E = 7, 8
# input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
# data = list(map(int, input.split()))
# items = [[0 for _ in range(V+1)] for _ in range(V+1)]
# for i in range(0, len(data), 2):
#     items[data[i]][data[i+1]] = 1
#     items[data[i+1]][data[i]] = 1
#
#
# def bfs(G, v):
#     global V
#     visited = [0] * (V + 1)
#     queue = []
#     queue.append(v)
#     while queue:
#         v = queue.pop(0)
#         if visited[v] == 0:
#             visited[v] = 1
#             print(v, end=" ")
#         for i in range(V+1):
#             if items[v][i] == 1 and visited[i] == 0:
#                 queue.append(i)
#
# bfs(items, 1)

V, E = 7, 8
input = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
data = list(map(int, input.split()))
items = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(0, len(data), 2):
    items[data[i]][data[i+1]] = 1
    items[data[i+1]][data[i]] = 1


def bfs(G, v):
    global V
    visited = [0] * (V + 1)
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        v = queue.pop(0)

        for i in range(V+1):
            if items[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1

    print(visited)


    return max(visited)-1

print(bfs(items, 1))
