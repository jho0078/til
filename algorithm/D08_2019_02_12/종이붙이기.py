import sys
sys.stdin = open("종이붙이기_input.txt")

memo = [1]
def fac(m):
    global memo
    if m >= 1 and len(memo) <= m:
        memo.append(m*fac(m-1))
    return memo[m]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = int(N/10)

    result = 0
    for i in range(int(n//2) + 1):
        result += (fac(n-i)/(fac(i)*fac(n-2*i)))*2**i

    print("#{} {}".format(tc, int(result)))

# 점화식 : f(n) = f(n-1) + 2*f(n-2)