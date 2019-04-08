def check(y, x, k):
    for i in range(k):
        for j in range(k):
            if y+i > 9 or x+j > 9 or table[y+i][x+j] == 0:
                return 0

    for i in range(k):
        for j in range(k):
            table[y+i][x+j] = 0
    return 1

def back(y, x, k):
    for i in range(k):
        for j in range(k):
            table[y+i][x+j] = 1


def nemonemo(c):
    global MIN

    if c > MIN:
        return

    count = 0
    for i in range(10):
        for j in range(10):
            count += 1
            if table[i][j] == 1:
                for k in range(5, 0, -1):
                    if chk[k] > 0 and check(i, j, k):
                        chk[k] -= 1
                        t.append(k)
                        nemonemo(c+1)
                        back(i, j, k)
                        chk[k] += 1
                        t.pop()
                return
    print(t)
    if c < MIN:
        MIN = c
    return


table = [list(map(int, input().split())) for i in range(10)]
chk = [5]*6
MIN = 0x7fffffff
t = []
nemonemo(0)
if MIN == 0x7fffffff:
    print(-1)
else:
    print(MIN)
