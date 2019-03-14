import sys
sys.stdin = open("프로세서 연결하기_input.txt")

def find(idx, end, length, count, visited):
    global max_count, min_length

    if idx == end:
        if count > max_count:
            max_count = count
            min_length = length
        elif count == max_count:
            if length < min_length:
                min_length = length
        return

    else:
        flag = 0
        y = cores[idx][0]
        x = cores[idx][1]
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            for h in range(1, N):
                nx = x + dx[i] * h
                ny = y + dy[i] * h

                if visited[ny][nx] == 0:
                    if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                        flag = 1
                        if table[ny][nx] != 1:
                            for j in range(1, h):
                                visited[y + dy[i] * j][x + dx[i] * j] = 1
                            break
                elif visited[ny][nx] != 0 or table[ny][nx] == 1:
                    break

            if flag == 1:
                find(idx+1, end, length+h+1, visited)
            else:
                find(idx+1, end, length, count, visited)


T = int(input())
for tc in range(1, 2):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    cores = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if table[i][j] == 1:
                cores.append([i, j])

    visited = [[0 for _ in range(N)] for _ in range(N)]
    max_count = 0
    min_length = 10000

    find(0, len(cores), 0, 0, visited)
    print(max_count, min_length)