import sys
sys.stdin = open("무선 충전_input.txt")

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    D = [list(map(int, input().split())) for i in range(2)]
    AP = [list(map(int, input().split())) for i in range(A)]
    D[0].insert(0, 0)
    D[1].insert(0, 0)
    result = 0
    # 0 : 이동x, 1 : 상, 2 : 우, 3 : 하, 4 : 좌

    y1, x1 = 1, 1
    y2, x2 = 10, 10
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]
    for i in range(M+1):
        y1, x1 = y1 + dy[D[0][i]], x1 + dx[D[0][i]]
        y2, x2 = y2 + dy[D[1][i]], x2 + dx[D[1][i]]

        pos = [[[0,0,0,0]], [[0,0,0,0]]]
        for j in range(A):
            if abs(y1 - AP[j][1]) + abs(x1 - AP[j][0]) <= AP[j][2]:
                pos[0].append(AP[j])
            if abs(y2 - AP[j][1]) + abs(x2 - AP[j][0]) <= AP[j][2]:
                pos[1].append(AP[j])

        pos[0] = sorted(pos[0], key=lambda x: x[3])
        pos[1] = sorted(pos[1], key=lambda x: x[3])

        if pos[0][-1][3] == pos[1][-1][3] and pos[0][-1][3] != 0:
            if pos[0][-1][0] == pos[1][-1][0] and pos[0][-1][1] == pos[1][-1][1]:
                result += pos[0][-1][3] + max(pos[0][-2][3], pos[1][-2][3])
            else:
                result += pos[0][-1][3]*2

        elif pos[0][-1][3] != pos[1][-1][3]:
            result += pos[0][-1][3] + pos[1][-1][3]

    print("#{} {}".format(tc, result))
