N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

tree = {}
data = [list(map(int, input().split())) for i in range(M)]
for i in range(M):
    if (data[i][0]-1, data[i][1]-1) in tree:
        tree[(data[i][0]-1, data[i][1]-1)].append(data[i][2])
    else:
        tree[(data[i][0]-1, data[i][1]-1)] = [data[i][2]]

for val in tree.values():
    val.sort()

land = [[5]*N for i in range(N)]

while K > 0:
    # 봄
    for key, val in tree.items():
        idx = len(val)
        for i in range(len(val)):
            if land[key[0]][key[1]] >= val[i]:
                land[key[0]][key[1]] -= val[i]
                val[i] += 1
            else:
                idx = i
                break

        # 여름
        if idx < len(val):
            for i in val[idx:]:
                land[key[0]][key[1]] += i//2
            tree[key] = val[:idx]

    # 가을
    new = {}
    for key, val in tree.items():
        if key in new:
            new[key] += val
        else:
            new[key] = val
        for i in range(len(val)):
            if not val[i]%5:
                for dy, dx in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
                    ny, nx = key[0] + dy, key[1] + dx
                    if -1 < ny < N and -1 < nx < N:
                        if (ny,nx) in new:
                            new[(ny,nx)].insert(0, 1)
                        else:
                            new[(ny,nx)] = [1]

    # for val in new.values():
    #     val.sort()

    # 겨울
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]

    tree = new
    K -= 1

result = 0
for val in tree.values():
    result += len(val)

print(result)
