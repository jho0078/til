import sys
sys.stdin = open("탈주범 검거_input.txt")

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= M:
        return True
    return False

def inspect(i, y, x):
    global L
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    nx = x + dx[i]
    ny = y + dy[i]
    if not iswall(ny, nx) and visited[ny][nx] == 0 and table[ny][nx] != 0:

        # 각 방향 탐색할 때 이동 가능한 파이프의 종류일 때만 적용
        if i == 0:
            if table[ny][nx] == 1 or table[ny][nx] == 2 or table[ny][nx] == 5 or table[ny][nx] == 6:

                # 최종시간 이내일 때만 queue에 집어넣는다. (visited 마킹 숫자를 늘려가면서 시간을 잰다)
                if visited[y][x] < L:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
        elif i == 1:
            if table[ny][nx] == 1 or table[ny][nx] == 2 or table[ny][nx] == 4 or table[ny][nx] == 7:
                if visited[y][x] < L:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
        elif i == 2:
            if table[ny][nx] == 1 or table[ny][nx] == 3 or table[ny][nx] == 4 or table[ny][nx] == 5:
                if visited[y][x] < L:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
        elif i == 3:
            if table[ny][nx] == 1 or table[ny][nx] == 3 or table[ny][nx] == 6 or table[ny][nx] == 7:
                if visited[y][x] < L:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1


def bfs(y, x):
    count = 0
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        t = queue.pop(0)
        count += 1
        y = t[0]
        x = t[1]

        # 파이프의 종류에 따라 탐색하는 방향 설정
        if table[y][x] == 1:
            for i in range(4):
                inspect(i, y, x)
        elif table[y][x] == 2:
            for i in [0, 1]:
                inspect(i, y, x)
        elif table[y][x] == 3:
            for i in [2, 3]:
                inspect(i, y, x)
        elif table[y][x] == 4:
            for i in [0, 3]:
                inspect(i, y, x)
        elif table[y][x] == 5:
            for i in [1, 3]:
                inspect(i, y, x)
        elif table[y][x] == 6:
            for i in [1, 2]:
                inspect(i, y, x)
        elif table[y][x] == 7:
            for i in [0, 2]:
                inspect(i, y, x)

    return count


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = []

    print("#{} {}".format(tc, bfs(R, C)))
    # for i in range(N):
    #     print(visited[i])