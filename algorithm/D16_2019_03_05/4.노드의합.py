import sys
sys.stdin = open("4.노드의합_input.txt")

def postorder(n):
    if n <= N:
        postorder(2*n)
        postorder(2*n+1)
        if data[n] == 0:
            if 2*n + 1 <= N:
                data[n] = data[2*n] + data[2*n+1]
            else:
                data[n] = data[2*n]

# 강사님 풀이
def postorder(node):
    global N
    if node > N:
        return 0
    else:
        if tree[node] != 0:
            return tree[node]
        else:
            a = postorder(2 * node)
            b = postorder(2 * node + 1)
            tree[node] a + b
        return tree[node]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    data = [0]*(N+1)
    for i in range(M):
        leaf, value = map(int, input().split())
        data[leaf] = value

    print(data)
    postorder(1)
    # print(data)
    print("#{} {}".format(tc, data[L]))