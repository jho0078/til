import sys
sys.stdin = open("그래프 경로_input.txt")

def dfs(items, a):
    global visited, v, flag, end

    if a == end: # 현재 위치가 end위치와 같아지면 경로를 찾았다는 것이므로 return
        flag = 1
        return

    visited[a] = 1

    for i in range(v+1):
        if items[a][i] == 1 and visited[i] == 0:
            dfs(items, i)

T = int(input())
for tc in range(1, T+1):
    flag = 0               # flag 초기 설정 경로를 못찾을 경우 0이 그대로 출력
    v, e = map(int, input().split())
    data = [[0 for _ in range(v+1)] for _ in range(v+1)]

    for i in range(e):
        y, x = map(int, input().split())
        data[y][x] = 1

    start, end = map(int, input().split())
    visited = [0] * (v+1)
    dfs(data, start)

    print("#{} {}".format(tc, flag))