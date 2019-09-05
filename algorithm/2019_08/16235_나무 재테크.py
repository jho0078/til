N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

tree = {}
data = [list(map(int, input().split())) for i in range(M)]
for i in range(M):
    if (data[i][0], data[i][1]) in tree:
        tree[(data[i][0], data[i][1])].append(data[i][2])
    else:
        tree[(data[i][0], data[i][1])] = [data[i][2]]

for val in tree.values():
    val.sort()

print(tree)
land = [[5]*N for i in range(N)]

# 봄
for key, val in tree.items():
    for i in range(len(val)):
        if land[land[key][0]][land[key][1]] >= val[i]:
            land[land[key][0]][land[key][1]] -= val[i]
        else:
            idx = i
            break
    if idx:
        tree[key] = val[:idx]

# 여름