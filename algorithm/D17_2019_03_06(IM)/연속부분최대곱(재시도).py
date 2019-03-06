N = int(input())
max_result = 0
now = 1
numlist = []
for i in range(N):
    k = float(input())
    numlist.append(k)
    if now*k > 1:
        if now*k > max_result:
            max_result = now*k
        now = now*k
    else:
        now = 1
if max_result > 1:
    print('%.3f' % max_result)
else:
    print('%.3f' % max(numlist))



