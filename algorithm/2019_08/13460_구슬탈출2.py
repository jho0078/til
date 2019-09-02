N, M = map(int, input().split())
A = [list(input().split()) for i in range(N)]
print(A)

def sol():




    return

for i in range(1, N-1):
    for j in range(1, N-1):
        if A[i][j] == "B":
            blue = [i, j]
        elif A[i][j] == "R":
            red = [i, j]
        elif A[i][j] == "O":
            goal = [i, j]

