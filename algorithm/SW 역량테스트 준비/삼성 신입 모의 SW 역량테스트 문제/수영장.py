import sys
sys.stdin = open("수영장_input.txt")

T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))

    day_cost = 0
    for i in range(len(plan)):
        day_cost += plan[i] * day

    month_cost = 0
    for i in range(len(plan)):
        if plan[i] > 0:
            month_cost += month

    three_cost = 0
    for i in range(0, len(plan), 3):
        for plan[i:i+3]

    year_cost = year

