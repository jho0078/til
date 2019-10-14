

def permutation(s):
    global count, result

    if count == k and result != -1:
        return

    if s == 3:
        if count == k:
            result = ''.join(list(map(str, t)))

        count += 1
        return

    for i in range(3):
        if not c[i]:
            c[i] += 1
            t[s] += numbers[i]
            permutation(s+1)
            t[s] -= numbers[i]
            c[i] -= 1


numbers = list(map(int, input().strip().split(' ')))
k = int(input())
numbers.sort()

c = [0]*3
t = [0]*len(numbers)
count = 1
result = -1
permutation(0)
print(result)