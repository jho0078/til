def check(s):
    t = 0
    if so[s][0] < so[s-1][0] or so[s][1] < so[s-1][1]:
        t += 1
    return t

def perm(s, n, t):
    global min1

    if t > min1:
        return

    if s == n:
        if t < min1:
            min1 = t
            print(so, min1)
        return

    for i in range(s, n):
        so[i], so[s], = so[s], so[i]
        if s >= 1:
            perm(s+1, n, t + check(s))
        else:
            perm(s + 1, n, t)
        so[i], so[s], = so[s], so[i]

n = int(input())
data = list(map(int, input().split()))

so = []
for i in range(0, len(data), 2):
    so.append([data[i], data[i+1]])
# print(so)

min1 = 100
perm(0, n, 0)
print(min1)
