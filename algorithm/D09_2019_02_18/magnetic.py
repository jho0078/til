import sys
sys.stdin = open("magnetic_input.txt")

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    count = 0

    # for i in range(N):
    #     mag = []
    #     for j in range(N):
    #         if data[j][i] != 0:
    #             mag.append(data[j][i])
    #
    #     for k in range(len(mag)-1):
    #         if mag[k] == 1 and mag[k+1] == 2:
    #             count += 1
    #
    # print("#{} {}".format(tc, count))



    for i in range(N):
        p = 0
        for j in range(N):
            if data[j][i] == 1:
                p = 1
            elif p == 1 and data[j][i] == 2:
                count += 1
                p = 0

    print("#{} {}".format(tc, count))





