import sys
sys.stdin = open("수영장_input.txt")

def solution(idx, cost):
    global min_cost

    if idx == 12:
        if cost < min_cost:
            min_cost = cost
        return
    else:
        if cost > min_cost:
            return
        else:
            solution(idx+1, cost + plan[idx]*day)
            solution(idx+1, cost + month)
            if idx + 3 < 13:
                solution(idx+3, cost + three)


T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))
    # print(plan)
    # print(day, month, three, year)

    min_cost = 1000000
    solution(0, 0)
    if min_cost < year:
        print("#{} {}".format(tc, min_cost))
    else:
        print("#{} {}".format(tc, year))