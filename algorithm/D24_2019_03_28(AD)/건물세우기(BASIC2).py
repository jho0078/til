def com(s, n, sum1):
    global min_sum

    if sum1 > min_sum:
        return

    if s == n:
        if sum1 < min_sum:
            min_sum = sum1
            return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            com(s + 1, n, sum1 + table[s][i])
            visited[i] = 0


n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
visited = [0]*n
min_sum = 100000
com(0, n, 0)
print(min_sum)