# import sys
# sys.stdin = open("input.txt")

def sol():

    baaam = []
    baaam.append([0, 0, 0])
    t = 0
    k = 0

    # 오른쪽 : 인덱스 증가, 왼쪽 : 인덱스 감소
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while 1:

        y, x, idx = baaam[0]

        if k < len(data) and t == int(data[k][0]):
            if data[k][1] == "D":
                idx = (idx + 1) % 4
            else:
                idx = (idx - 1) % 4

            k += 1

        y, x = y + dy[idx], x + dx[idx]

        if y < 0 or x < 0 or y > N-1 or x > N-1 or A[y][x] == 1:
            return t + 1

        baaam.insert(0, [y, x, idx])

        if A[y][x] == 0:
            tail_y, tail_x, tmp = baaam.pop(-1)
            A[tail_y][tail_x] = 0

        A[y][x] = 1
        t += 1

        print("t:", t)
        print("idx:", idx)
        for i in range(N):
            print(A[i])
        print()

N = int(input())
K = int(input())
A = [[0]*N for i in range(N)]
A[0][0] = 1

for i in range(K):
    y, x = map(int, input().split())
    A[y-1][x-1] = 2

L = int(input())
data = [input().split() for i in range(L)]

print(sol())


