import sys
sys.stdin = open("원자 소멸 시뮬레이션_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 시간 4000초, 범위 벗어나면 삭제
    data = [list(map(int, input().split())) for i in range(N)]
    print(data)
    for i in range(N):
        data[i][0], data[i][1] = 2*data[i][0], 2*data[i][1]

    t = 0
    result = 0
    while t < 4002 and data:
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        xys = {}
        # print(data)
        for i in range(len(data)):
            data[i][0] = data[i][0] + dx[data[i][2]]
            data[i][1] = data[i][1] + dy[data[i][2]]
            x, y = data[i][0], data[i][1]

            if -2000 <= x <= 2000 and -2000 <= y <= 2000:
                if (x, y) not in xys:
                    xys[(x, y)] = [data[i]]
                else:
                    xys[(x, y)].append(data[i])

        # print(xys)
        data = []
        for val in xys.values():
            if len(val) > 1:
                for r in val:
                    result += r[3]
            else:
                data.append(val[0])

        t += 1

    print("#{} {}".format(tc, result))
