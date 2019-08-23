import sys
sys.stdin = open("1_input.txt")

# T = int(input())
T = 1
for tc in range(1, T+1):
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    count = 0

    for l in range(2):
        if l == 1:
            A = list(zip(*A))
        for i in range(N):
            a = A[i][0]
            c = 1
            j = 1
            flag = 1
            while j < N:
                if A[i][j] == a:
                    c += 1
                elif A[i][j] == a+1:
                    if c < X:
                        flag = 0
                        break
                    else:
                        a = A[i][j]
                        c = 1
                elif A[i][j] == a-1:
                    a = A[i][j]
                    if N-j < X:
                        flag = 0
                        break
                    for k in range(X):
                        if A[i][j+k] != a:
                            flag = 0
                            break
                    if flag == 0:
                        break
                    else:
                        c = 1
                        j += X-1
                else:
                    flag = 0
                    break
                j += 1

            if flag == 1:
                print(l,i)
                count += 1

    print("#{} {}".format(tc, count))