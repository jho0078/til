import sys
sys.stdin = open("노드의 거리_input.txt")

def bfs(S, G):

    queue = []
    visited = [0] * (V+1)
    queue.append(S)
    visited[S] = 1

    while queue:
        t = queue.pop(0)

        for i in range(V+1):
            if data[t][i] == 1 and visited[i] == 0:
                if i == G:
                    return visited[t]
                else:
                    queue.append(i)
                    visited[i] = visited[t] + 1

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        y, x = map(int, input().split())
        data[y][x] = 1
        data[x][y] = 1

    for i in range(V+1):
        print(data[i])

    S, G = map(int, input().split())

    print("#{} {}".format(tc, bfs(S, G)))



