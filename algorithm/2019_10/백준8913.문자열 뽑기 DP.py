def solution():
    dp = [set() for _ in range(13)]
    data = input() + 'c'
    dp[0].add(data)
    for n in range(1, 13):
        for one in dp[n - 1]:
            now = one[0]
            start = 0
            idx = 0
            for i in range(1, len(one)):
                if one[i] == now:
                    idx += 1
                else:
                    if idx >= 1:
                        new_data = ''
                        for j in range(len(one)):
                            if j < start or j > start + idx:
                                new_data += one[j]

                        if len(new_data) == 1:
                            # for i in range(13):
                            #     print(dp[i])
                            return 1

                        dp[n].add(new_data)
                    now = one[i]
                    idx = 0
                    start = i

    # for i in range(13):
    #     print(dp[i])
    return 0

T = int(input())
for tc in range(1, T+1):
    print(solution())
