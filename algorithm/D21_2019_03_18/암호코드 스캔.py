import sys
sys.stdin = open("암호코드 스캔_input.txt")

asc = [[0,0,0,0],
       [0,0,0,1],
       [0,0,1,0],
       [0,0,1,1],
       [0,1,0,0],
       [0,1,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,0,0],
       [1,0,0,1],
       [1,0,1,0],
       [1,0,1,1],
       [1,1,0,0],
       [1,1,0,1],
       [1,1,1,0],
       [1,1,1,1]]

patterns = [[1,1,2],
            [1,2,2],
            [2,2,1],
            [1,1,4],
            [2,3,1],
            [1,3,2],
            [4,1,1],
            [2,1,3],
            [3,1,2],
            [2,1,1]]

def findratio(i, j):
    x_start = j
    while True:
        j -= 1
        if table[i][j] == 0:
            first = x_start - j
            x_start = j
            break

    while True:
        j -= 1
        if table[i][j] == 1:
            second = x_start - j
            x_start = j
            break

    while True:
        j -= 1
        if table[i][j] == 0:
            third = x_start - j
            break

    ratio = [first, second, third]
    # gonil = [third, second, first]
    # t.append(gonil)
    min_ratio = min(ratio)
    for k in range(3):
        ratio[k] //= min_ratio

    if ratio in patterns:
        save.append(patterns.index(ratio))
        return min_ratio*7

    else:
        return 0


def aToh(c):
    if c <= "9":
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    table = [[0 for _ in range(M*4)] for _ in range(N)]
    data = [list(input()) for i in range(N)]

    for i in range(N):
        for j in range(M):
            for k in range(4):
                table[i][j*4 + k] = asc[aToh(data[i][j])][k]

    t = []
    s = []
    result = 0
    flag = 0
    for i in range(N):
        save = []
        j = M*4-1
        while j > 0:
            if table[i][j] == 1 and table[i][j+1] == 0 and table[i-1][j] == 0:

                while True:
                    # print(i, j)
                    k = findratio(i, j)
                    if len(save) == 8:
                        save.reverse()
                        check = 0
                        for m in range(len(save)):
                            if (m + 1) % 2 == 1:
                                check += save[m] * 3
                            else:
                                check += save[m]
                        s.append(sum(save))
                        if check % 10 == 0:
                            flag = 1
                            t.append(sum(save))
                            result += sum(save)

                        break

                    if k > 0:
                        j -= k
                    else:
                        break
                save = []
            j -= 1

    if flag == 0:
        print("#{} {}".format(tc, "0"))
    else:
        print("#{} {}".format(tc, result))
    #
    print(s)
    print(t)