import sys
sys.stdin = open("행렬찾기_input.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     print(data[i])

    matrixall = []

    for y in range(n):
        for x in range(n):
            x_length = 1
            y_length = 1
            y1 = y
            x1 = x

            matrix = []

            if data[y1][x1] != 0:
                y_start = y1
                x_start = x1
                while data[y1][x1] != 0:
                    x1 += 1
                    x_length += 1
                x1 -= 1
                x_length -= 1

                while data[y1][x1] != 0:
                    y1 += 1
                    y_length += 1
                y1 -= 1
                y_length -= 1

                y_end = y1
                x_end = x1

                matrix.append(y_length)
                matrix.append(x_length)
                matrixall.append(matrix)

                for i in range(y_start, y_end+1):
                    for j in range(x_start, x_end+1):
                        data[i][j] = 0


    sorted_matrix = sorted(matrixall, key=lambda x: (x[0]*x[1], x[0]))
    result = []
    for i in range(len(sorted_matrix)):
        for j in range(2):
            result.append(str(sorted_matrix[i][j]))

    print("#{} {} {}".format(tc, len(matrixall), ' '.join(result)))


