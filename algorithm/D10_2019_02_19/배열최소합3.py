import sys
sys.stdin = open("배열최소합_input.txt")

def permutation(sum, n, k):
    global minnow, N

    if sum > minnow:
        return

    if k == n:
        if sum < minnow:
            minnow = sum

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                permutation(sum + data[k][i] , n, k+1)
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    minnow = 10000
    visited = [0]*N
    permutation(0, N, 0)

    print("#{} {}".format(tc, minnow))
