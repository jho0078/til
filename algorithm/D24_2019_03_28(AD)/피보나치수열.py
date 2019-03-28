def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        if not a[n]:
            a[n] = fibonacci(n-1) + fibonacci(n-2)

    return a[n]

n = int(input())
a = [0]*(n+1)
print(fibonacci(n))