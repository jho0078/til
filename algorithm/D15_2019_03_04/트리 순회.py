import sys
sys.stdin = open("트리 순회.txt")

def preorder(node):
    if node != 0:
        print("{}".format(node), end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        preorder(tree[node][0])
        print("{}".format(node), end=" ")
        preorder(tree[node][1])

def postorder(node):
    if node != 0:
        preorder(tree[node][0])
        preorder(tree[node][1])
        print("{}".format(node), end=" ")

V, E = map(int, input().split())
tree = [[0 for _ in range(3)] for _ in range(V+1)]
print(tree)
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i*2]
    n2 = temp[i*2+1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n2][2] = n1

print("전위순회 : ", end="")
preorder(1)
print()

print("중위순회 : ", end="")
inorder(1)
print()

print("후위순회 : ", end="")
postorder(1)
print()