import sys
sys.stdin = open("ladder1_input.txt")

def move_right(datas, a, b):
    while b != 99 and datas[a][b] != 0:
        b += 1
    if b == 99: return b
    if datas[a][b] == 0: return b - 1

def move_left(datas, a, b):
    while b != 0 and datas[a][b] != 0 :
        b -= 1
    if b == 0: return b
    if datas[a][b] == 0: return b + 1


for tc in range(1, 11):
    dummy = int(input())
    data = [list(map(int, (input().split()))) for i in range(100)]

    for j in range(100):
        for i in range(100):
            if data[j][i] == 2:
                y = j
                x = i


    while y > 0:
        y -= 1
        if x < 99 and data[y][x + 1] == 1:
            x = move_right(data, y, x)

        if x > 0 and data[y][x - 1] == 1:
            x = move_left(data, y, x)

        if y == 0:
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











