import sys
sys.stdin = open("공통조상_input.txt")

def parents(a):
    parent_list = []
    node = a
    while node != 1:
        node = table[node][3]
        parent_list.append(node)
    return parent_list

def inorder(node):
    if node != 0:
        inorder(table[node][1])
        count[0] += 1
        inorder(table[node][2])


T = int(input())
for tc in range(1, T +1):
    V, E, a, b = map(int, input().split())
    table = [[0 for _ in range(4)] for _ in range(V + 1)]
    for i in range(V+1):
        table[i][0] = i
    data = list(map(int, input().split()))
    for i in range(0, len(data), 2):
        if table[data[i]][1] == 0:
            table[data[i]][1] = data[i + 1]
        else:
            table[data[i]][2] = data[i + 1]
        table[data[i+1]][3] = data[i]
    # for i in range(V+1):
    #     print(table[i])

    node_a = parents(a)
    node_b = parents(b)

    p = 0
    for i in range(len(node_a)):
        for j in range(len(node_b)):
            if node_a[i] == node_b[j]:
                common_node = node_a[i]
                p = 1
                break
        if p == 1:
            break

    count = [0]
    inorder(common_node)

    print("#{} {} {}".format(tc, common_node, count[0]))
