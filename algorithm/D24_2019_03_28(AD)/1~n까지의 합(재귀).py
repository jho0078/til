def mysum(n, sum1):
    if n == 0:
        print(sum1)
    else:
        mysum(n-1, sum1+n)

n = int(input())
mysum(n, 0)