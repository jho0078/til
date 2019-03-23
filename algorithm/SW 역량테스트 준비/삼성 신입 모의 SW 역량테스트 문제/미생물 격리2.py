import sys
sys.stdin = open("미생물 격리_input.txt")

def iswall(y, x):
    if y == 0 or x == 0 or y == N-1 or x == N-1:
        return True
    return False


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    table = [list(map(int, input().split())) for i in range(K)]

    coordinate = []
    status = []
    for i in range(K):
        coordinate.append(table[i][:2])
        status.append(table[i][2:4])

    for t in range(M):

        # 1시간 경과, 좌표 이동
        for i in range(len(coordinate)):
            if status[i][1] == 1:
                coordinate[i][0] -= 1
            elif status[i][1] == 2:
                coordinate[i][0] += 1
            elif status[i][1] == 3:
                coordinate[i][1] -= 1
            elif status[i][1] == 4:
                coordinate[i][1] += 1

        # 가장자리에 군집이 있을 경우
        b = [0, 2, 1, 4, 3]
        for i in range(len(coordinate)):
            if iswall(coordinate[i][0], coordinate[i][1]):
                status[i][0] = status[i][0]//2
                status[i][1] = b[status[i][1]]

        # 동일한 좌표에 군집이 있을 경우 병합
        duplicate = []
        new_coordinate = []
        new_status = []
        for i in range(len(coordinate)):
            if status[i][0] != 0:
                if coordinate.count(coordinate[i]) > 1:
                    if coordinate[i] not in duplicate:
                        duplicate.append(coordinate[i])
                    else:

                else:
                    new_coordinate.append(coordinate[i])
                    new_status.append(status[i])

        for i in range(len(duplicate)):
            sum_counts = 0
            max_counts = 0
            for j in range(len(coordinate)):
                if duplicate[i] == coordinate[j]:
                    if status[j][0] > max_counts:
                        max_counts = status[j][0]
                        direction = status[j][1]
                    sum_counts += status[j][0]

            new_coordinate.append(duplicate[i])
            new_status.append([sum_counts, direction])

        coordinate = new_coordinate
        status = new_status

    result = 0
    for i in range(len(status)):
        result += status[i][0]
    print("#{} {}".format(tc, result))
