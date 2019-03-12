# nHr = nHr-1 + n-1Hr , nH0 = 1

def Hombination(n, r, q):
    if r == 0:
        myprint(q)
    else:
        if n == 0:
            return
        else:
            T[r-1] = A[n-1]
            Hombination(n, r-1, q)
            Hombination(n-1, r, q)

def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d" % (T[q]), end="")
    print("")

T = [0]*3
A = [1, 2, 3, 4]
Hombination(4, 3, 3)