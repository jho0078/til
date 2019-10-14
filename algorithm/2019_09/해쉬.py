def sol():

    visited[N] = 1
    q = [N]
    k = 0
    while True:
        num = q[k]

        hello = [num + 1, num - 1, num * 2, num - 10]
        for i in range(4):
            if hello[i] == M:
                return visited[num]

            if hello[i] > 0 and hello[i] <= 1000000:
                if visited[hello[i]] == 0:
                    visited[hello[i]] = visited[num] + 1
                    q.append(hello[i])

        k += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0 for _ in range(1000000 + 1)]
    print("#{} {}".format(tc, sol()))