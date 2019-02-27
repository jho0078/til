
# N = int(input())
N = 10
count = 0
while N > 1:
    if not N%3:
        N = N//3
        count += 1
    elif not N%2:
        N = N//2
        count += 1
    else:
        N -= 1
        count += 1

print(count)