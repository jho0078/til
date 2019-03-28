import sys
sys.stdin = open("예산.txt")

def solution(s, e):

    while s <= e:
        m = (s+e)//2
        cost = 0
        for i in range(N):
            if data[i] <= m:
                cost += data[i]
            else:
                cost += m

        if budget >= cost:
            sol = m
            s = m + 1

        else:
            e = m - 1

    return sol

N = int(input())
data = list(map(int, input().split()))
budget = int(input())
max_budget = max(data)

print(solution(1, max_budget))


# 그리디그리디
N = int(input())
arr = list(map(int, input().split()))
budget = int(input())

arr.sort()
sol, tot = 0, 0
for i in range(N):
    if tot + arr[i]*(N-i) <= budget:
        tot += arr[i]
    else:
        sol = (budget - tot)//(N-i)
        break

if sol:
    print(sol)
else:
    print(arr[N-1])



