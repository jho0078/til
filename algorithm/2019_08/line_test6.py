N, M = input().split()
MAX = 0
for i in range(int(N)):
    n, style = map(int, input().split())
    if MAX < n:
        MAX = n


