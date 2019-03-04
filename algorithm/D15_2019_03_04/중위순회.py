import sys
sys.stdin = open("중위순회_input.txt")

def inorder(node):
    if node != 0:
        inorder(first_child[node])
        result.append(alpha[node])
        inorder(second_child[node])

T = 10
for tc in range(1, T+1):
    N = int(input())
    first_child = [0]*(N + 1)
    second_child = [0]*(N + 1)
    alpha = [0]*(N + 1)
    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        ch = temp[1]
        alpha[addr] = ch
        if addr*2 <= N:
            first_child[addr] = int(temp[2])
            if addr*2 + 1 <= N:
                second_child[addr] = int(temp[3])

    result = []
    inorder(1)
    print("#{} {}".format(tc, ''.join(result)))
    print(first_child)
    print(second_child)
    print(alpha)


