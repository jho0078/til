def solution(sticker):
    # 1
    #     dps = [0]*len(sticker)
    #     dps[0] = sticker[0]
    #     dps[1] = sticker[1]

    #     for i in range(2, len(sticker)):
    #         dps[i] = max(dps[i-2] + sticker[i], dps[i-1])

    #     first = dps[len(sticker) - 1]

    # 2
    #     dps = [0]*100000
    #     dps[0] = sticker[0]
    #     dps[1] = 0

    #     for i in range(2, len(sticker)):
    #         dps[i] = max(dps[i-2] + sticker[i], dps[i-1])

    #     second = dps[len(sticker) - 1]

    # return max(first, second)

    dp = [[0] * 2 for _ in range(len(sticker))]
    dp[0][0] = 0
    dp[0][1] = sticker[0]
    for i in range(len(sticker) - 1):
        dp[i + 1][0] = max(dp[i])
        dp[i + 1][1] = sticker[i + 1] + dp[i][0]

    return max(dp[-1])