import sys
sys.stdin = open("예산.txt")

def solution(s, e):

    while s <= e:
        m = (s+e)//2
        max1 = m
        cost = 0
        for i in range(N):
            if data[i] <= m:
                cost += data[i]
            else:
                cost += m

        if budget == cost:
            return max1
        elif budget < cost:
            e = m - 1
        else:
            s = m + 1

    return max1

N = int(input())
data = list(map(int, input().split()))
budget = int(input())
min_budget = min(data)
max_budget = max(data)

print(solution(min_budget, max_budget))
