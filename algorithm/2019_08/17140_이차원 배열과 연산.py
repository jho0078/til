def sol():
    global A, k, r, c

    t = 0
    while 1:

        if -1 < r-1 < len(A) and -1 < c-1 < len(A[0]) and A[r-1][c-1] == k:
            return t

        if t > 100:
            return -1

        newA = []
        length = 0
        row = len(A)
        column = len(A[0])

        flag = 0
        if row < column:
            flag = 1
            A = list(zip(*A))
            row, column = column, row

        for i in range(row):
            tmp = {}
            for j in range(column):
                if A[i][j] in tmp:
                    tmp[A[i][j]] += 1
                else:
                    if A[i][j]:
                        tmp[A[i][j]] = 1

            tmp2 = []
            for key, val in tmp.items():
                tmp2.append([val, key])

            tmp2.sort()
            newA.append(tmp2)

        newnewA = []
        for i in range(len(newA)):
            tmp2 = []
            for j in range(len(newA[i])):
                for h in range(1, -1, -1):
                    tmp2.append(newA[i][j][h])

            length = max(length, len(tmp2))
            newnewA.append(tmp2)

        for i in range(row):
            if len(newnewA[i]) < length:
                newnewA[i] += [0]*(length - len(newnewA[i]))

        if flag == 1:
            A = list(zip(*newnewA))
        else:
            A = newnewA

        t += 1


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for i in range(3)]

print(sol())
