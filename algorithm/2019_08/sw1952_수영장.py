def sol(s, result):
    global MIN

    if MIN < result:
        return

    if s >= 12:
        MIN = min(MIN, result)
        return

    sol(s+1, result + price[0]*plan[s])
    sol(s+1, result + price[1])
    sol(s+3, result + price[2])
    sol(s+12, result + price[3])

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    MIN = 999999

    sol(0, 0)

    print("#{} {}".format(tc, MIN))