T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    table = [0] * (N + 1)

    for i in range(len(data)):
        table[i + 1] = data[i]
        idx = i + 1
        parent = idx // 2
        while table[parent] > table[idx]:
            table[parent], table[idx] = table[idx], table[parent]
            idx = parent
            parent = idx // 2

    result = 0
    node = len(data) // 2
    while node > 0:
        result += table[node]
        node = node // 2

    print("#{} {}".format(tc, result))