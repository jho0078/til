def inorder(N):
    if N != 0:
        inorder(table[N][0])
        inorder(table[N][1])
        count[0] += 1

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    table = [[0 for _ in range(3)] for _ in range(E + 2)]

    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        if table[data[i]][0] == 0:
            table[data[i]][0] = data[i+1]
        else:
            table[data[i]][1] = data[i+1]
        table[data[i]][2] = data[i]

    count = [0]
    inorder(N)

    print("#{} {}".format(tc, count[0]))


