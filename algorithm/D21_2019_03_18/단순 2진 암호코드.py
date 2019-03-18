import sys
sys.stdin = open("단순 2진 암호코드_input.txt")

patterns = [[0,0,0,1,1,0,1],
            [0,0,1,1,0,0,1],
            [0,0,1,0,0,1,1],
            [0,1,1,1,1,0,1],
            [0,1,0,0,0,1,1],
            [0,1,1,0,0,0,1],
            [0,1,0,1,1,1,1],
            [0,1,1,1,0,1,1],
            [0,1,1,0,1,1,1],
            [0,0,0,1,0,1,1]]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, list(input()))) for i in range(N)]

    flag = 0
    for y in range(N):
        for x in range(M-1, -1, -1):
            if data[y][x] == 1:
                code = data[y][x-55:x+1]
                flag = 1
                break

        if flag == 1:
            break

    inspect = []
    for i in range(0, len(code), 7):
        inspect.append(patterns.index(code[i:i+7]))

    result = 0
    for i in range(len(inspect)):
        if (i+1)%2 == 1:
            result += inspect[i] * 3
        else:
            result += inspect[i]

    if result%10 == 0:
        print("#{} {}".format(tc, sum(inspect)))
    else:
        print("#{} ".format(tc) + "0")