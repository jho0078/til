def solution(bishops):
    answer = 64
    table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    visited = [[0] * 8 for _ in range(8)]
    for bishop in bishops:
        y, x = int(bishop[1]) - 1, table[bishop[0]]
        if not visited[y][x]:
            visited[y][x] = 1
            answer -= 1

        dy, dx = [1, 1, -1, -1], [1, -1, 1, -1]
        for i in range(4):
            for h in range(1, 8):
                ny, nx = y + dy[i] * h, x + dx[i] * h
                if ny < 0 or nx < 0 or ny >= 8 or nx >= 8:
                    break

                if not visited[ny][nx]:
                    answer -= 1
                    visited[ny][nx] = 1

    for i in range(8):
        print(visited[i])
    return answer

bishops = ["D5", "E8", "G2"]
print(solution(bishops))
