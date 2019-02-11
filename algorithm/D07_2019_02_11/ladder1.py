import sys
sys.stdin = open("ladder1_input.txt")

for tc in range(1, 11):
    dummy = int(input())
    data = [list(map(int, (input().split()))) for i in range(100)]

    y = 99
    x = data[99].index(2)

    while y > 0:
        y -= 1

        if x < 99 and data[y][x + 1] == 1:
            x += 1
            while data[y-1][x] != 1:
                x += 1

        elif x > 0 and data[y][x - 1] == 1:
            x -= 1
            while data[y-1][x] != 1:
                x -= 1

        elif y == 0:
            print("#{} {}".format(tc, x))











# dx = [1, -1, 0, 0] 우 좌 위 아래
# dy = [0, 0, 1, -1]
#
# def ladder(data):
#     for i in range(100):
#         if data[0][i]:
#             j = 0
#             k = i
#             while True:
#                 if data[j][k + 1] == 0 and data[j][k - 1] == 0:
#                     j += 1
#                     if j == 99:
#                         return k
#
#                 if data[j][k + 1] == 0:
#                     k = move_right(data, j, k)
#                     j += 1
#
#                 if data[j][k - 1] == 0:
#                     k = move_left(data, j, k)
#                     j += 1











