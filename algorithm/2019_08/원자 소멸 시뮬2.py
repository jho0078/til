import sys
sys.stdin = open("원자 소멸 시뮬2_input.txt")

def sol(data):

    result = 0
    for k in range(4002):
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        xys = {}
        for i in range(len(data)):
            data[i][0] = data[i][0] + dx[data[i][2]]
            data[i][1] = data[i][1] + dy[data[i][2]]
            x, y = data[i][0], data[i][1]

            if -2000 <= x <= 2000 and -2000 <= y <= 2000:
                if (x,y) not in xys:
                    xys[(x, y)] = [data[i]]
                else:
                    xys[(x, y)].append(data[i])

        data = []
        for val in xys.values():
            if len(val) > 1:
                for row in val:
                    result += row[3]
            else:
                data.append(val[0])

        if len(data) <= 1:
            return result

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]

    for i in range(N):
        data[i][0], data[i][1] = 2*data[i][0], 2*data[i][1]

    print("#{} {}".format(tc, sol(data)))
