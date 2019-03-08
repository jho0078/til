import sys
sys.stdin = open("스파이 조직.txt")

T = int(input())
for tc in range(1, T+1):
    n, data = input().split()
    N = int(n)

    i = 0
    stage = 0
    tree = [[] for i in range(51)]
    while i < len(data):
        if data[i] == '<':
            if data[i+1] == '>':
                i += 1
            else:
                stage += 1
                num = ''
                j = 1
                while data[i+j] != '>' and data[i+j] != '<':
                    num += data[i+j]
                    j += 1
                tree[stage].append(num)
                i += j - 1
        elif data[i] == '>':
            stage -= 1
        else:
            tree[stage].append(data[i])
        i += 1

    print(tree)
    print(' '.join(tree[N]))

# n, data = input().split()
# N = int(n)
#
# i = 0
# stage = 0
# tree = [[] for i in range(51)]
# while i < len(data):
#     if data[i] == '<':
#         if data[i+1] == '>':
#                 i += 1
#         else:
#             stage += 1
#             num = ''
#             j = 1
#             while data[i+j] != '>' and data[i+j] != '<':
#                 num += data[i+j]
#                 j += 1
#             tree[stage].append(num)
#             i += j - 1
#     elif data[i] == '>':
#         stage -= 1
#     else:
#         tree[stage].append(data[i])
#     i += 1
#
# print(' '.join(tree[N]))