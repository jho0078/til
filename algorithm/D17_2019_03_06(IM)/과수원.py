N = int(input())

table = [list(map(int, list(input()))) for i in range(N)]
# for i in range(N):
#     print(table[i])

count = 0
for i in range(N-1):
    for j in range(N-1):
        sum1 = 0
        for k in range(i+1):
            for l in range(j+1):
                sum1 += table[k][l]

        sum2 = 0
        for k in range(i+1, N):
            for l in range(j+1):
                sum2 += table[k][l]

        sum3 = 0
        for k in range(i+1):
            for l in range(j+1, N):
                sum3 += table[k][l]

        sum4 = 0
        for k in range(i+1, N):
            for l in range(j+1, N):
                sum4 += table[k][l]

        if sum1 == sum2 and sum2 == sum3 and sum3 == sum4:
            count += 1

if count > 0:
    print(count)
else:
    print(-1)