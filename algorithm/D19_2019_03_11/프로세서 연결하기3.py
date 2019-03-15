import sys
sys.stdin = open("프로세서 연결하기_input.txt")

def find(idx, end, length, visited):
    global max_count, min_length
    visited = visited[:]

    if idx == end:
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

                if visited[ny][nx] == 0 and table[ny][nx] != 1:
                    if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                        flag = 1
                        if table[ny][nx] != 1:
                            for j in range(1, h+1):
                                visited[y + dy[i] * j][x + dx[i] * j] = 1
                            break
                else:
                    break

            if flag == 1:
                find(idx+1, end, length+h, visited)
            # else:
            #     find(idx+1, end, length, visited)


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

    find(0, len(cores), 0, visited)
    print(max_count, min_length)