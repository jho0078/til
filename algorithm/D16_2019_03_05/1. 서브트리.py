import sys
sys.stdin = open("1.서브트리_input.txt")

def postorder(N):
    global count

    if N != 0:
        postorder(table[N][0])
        postorder(table[N][1])
        count += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    table = [[0 for _ in range(3)] for _ in range(E+2)]
    # print(table)
    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        if table[data[i]][0] == 0:
            table[data[i]][0] = data[i + 1]
        else:
            table[data[i]][1] = data[i + 1]

        table[data[i+1]][2] = data[i]
    # for i in range(E+2):
    #     print(table[i])
    # print()
    count = 0
    postorder(N)

    print("#{} {}".format(tc, count))

