def inorder(n):
    global idx, N
    if n <= N:
        inorder(n*2)
        data[n] = idx
        idx += 1
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [0]*(N+1)
    idx = 1

    inorder(1)
    print(data)
    print("#{} {} {}".format(tc, data[1], data[N//2]))