import sys
sys.stdin = open("그래프 경로_input.txt")

def dfs(items, a):
    global visited, v, end

    visited[a] = 1

    for i in range(v+1):
        if items[a][i] == 1 and visited[i] == 0:
            dfs(items, i)

T = int(input())
for tc in range(1, T+1):
    flag = 0
    v, e = map(int, input().split())
    data = [[0 for _ in range(v+1)] for _ in range(v+1)]

    for i in range(e):
        y, x = map(int, input().split())
        data[y][x] = 1


    start, end = map(int, input().split())
    visited = [0] * (v+1)
    dfs(data, start)

    print("#{} {}".format(tc, visited[end]))








