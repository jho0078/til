def solution(land):
    length = len(land)
    dp = [[0] * 4 for _ in range(100000)]
    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, length):
        for j in range(4):
            print(dp[i - 1])
            max_before = max(dp[i - 1].pop(j))
            dp[i][j] = land[i][j] + max_before

    return max(dp[i])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))