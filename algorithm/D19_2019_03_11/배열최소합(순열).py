import sys
sys.stdin = open("배열최소합_input.txt")

def sumgo(minsum):
    sum1 = 0
    for i in range(N):
        sum1 += table[i][tmp[i]]
    if sum1 < minsum:
        return sum1
    return minsum

def perm(n):
    global minsum
    if n == -1:
        minsum = sumgo(minsum)
        # print(''.join(map(str, tmp)))
        return

    else:
        for i in range(n, -1, -1):
            a[i], a[n] = a[n], a[i]
            tmp[n] = a[n]
            perm(n-1)
            a[i], a[n] = a[n], a[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    minsum = 100
    a = [0] * N
    for i in range(N):
        a[i] = i
    tmp = [0] * N
    perm(N-1)
    print("#{} {}".format(tc, minsum))

