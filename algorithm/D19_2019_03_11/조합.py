# nCr = n-1Cr-1 + n-1Cr , nC0 = 1

def Combination(n, r, q):
    if r == 0:
        myprint(q)
    else:
        if n < r:
            return
        else:
            T[r-1] = A[n-1]
            Combination(n-1, r-1, q)
            Combination(n-1, r, q)

def myprint(q):
    while q != 0:
        q = q - 1
        print(" %d" % (T[q]), end="")
    print("")

T = [0]*3
A = [1, 2, 3, 4]
Combination(4, 3, 3)