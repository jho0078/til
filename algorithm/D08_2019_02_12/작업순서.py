import sys
sys.stdin = open("작업순서_input.txt")

for tc in range(1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(0, data, 2):
        count[i]


    items = [[0 for i in range(V+1)] for j in range(V+1)]

    for i in range(0, len(data), 2):
        items[data[i]][data[i+1]] = 1

    # items = {}
    # for i in range(0, len(data), 2):
    #     if data[i] not in items:
    #         items.update({data[i]: [data[i+1]]})
    #     else:
    #         items[data[i]].append(data[i+1])
    # print(items)


def dfs(data):
    global visited, V

    visited[v] == 1

    for k in range(data):
        if data[v][k] == 1 and visited[v] == 0:
            if data[v].count(1) == 1:


            for j in range(data):
                if data[v][j] != 0:
                    break





def dfs(items, a):
    global visited, v, flag, end

    if a == end: # 현재 위치가 end위치와 같아지면 경로를 찾았다는 것이므로 return
        flag = 1
        return

    visited[a] = 1

    for i in range(v+1):
        if items[a][i] == 1 and visited[i] == 0:
            dfs(items, i)

















