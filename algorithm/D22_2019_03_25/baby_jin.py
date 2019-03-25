def babygin():
    global flag

    check = 0
    if a[0] == a[1] and a[1] == a[2]:
        check += 1
    if a[3] == a[4] and a[4] == a[5]:
        check += 1
    if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
        check += 1
    if a[3] + 1 == a[4] and a[4] + 1 == a[5]:
        check += 1

    if check == 2:
        flag = 1
        print(a)
        return

def perm(n, k):
    if n == k:
        babygin()
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

a = [6,6,7,7,6,7]
flag = 0
perm(6, 0)