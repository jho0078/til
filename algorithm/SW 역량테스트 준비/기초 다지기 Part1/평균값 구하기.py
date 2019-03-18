T = int(input())
for tc in range(1, T+1):
    print("#{} ".format(tc) + str("%.f" % (sum(map(int, input().split()))/10)))
