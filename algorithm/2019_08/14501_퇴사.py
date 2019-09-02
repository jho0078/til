# import sys
# sys.stdin = open("input.txt")

def sol(s, earn):
    global MAX

    if earn > MAX:
        MAX = earn

    if s >= N:
        return

    for i in range(s, len(data)):
        if i+data[i][0] <= N:
            print("s:", i+data[i][0])
            print("earn:", earn+data[i][1])
            sol(i+data[i][0], earn+data[i][1])


N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
MAX = 0


sol(0, 0)

print(MAX)