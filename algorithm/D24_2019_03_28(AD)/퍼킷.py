def subset(s, n, sour, bitter):
    global min1

    if s == n:
        if sour == 1 and bitter == 0:
            return
        else:
            print(sour, bitter)
            chai = abs(sour - bitter)
            if chai < min1:
                min1 = chai
            return

    subset(s+1, n, sour, bitter)
    subset(s+1, n, sour*data[s][0], bitter + data[s][1])

N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
min1 = 10000000000000000000000000
subset(0, N, 1, 0)
print(min1)

# 2
# 1 7
# 2 6
