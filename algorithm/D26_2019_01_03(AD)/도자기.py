def combination(s, cnt):
    global N, M

    if cnt > M:
        return

    if s == N:
        if cnt == M:
            a = []
            for i in range(N):
                if t[i] != 0:
                    a.append(t[i])
            a.sort()
            if a not in b:
                b.append(a)

            #         print(t[i], end=" ")
            # print()
        return

    t[s] = A[s]
    combination(s + 1, cnt + 1)
    t[s] = 0
    combination(s + 1, cnt)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    t = [0]*N
    b = []
    combination(0, 0)
    print(len(b))

