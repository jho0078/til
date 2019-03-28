def solution(s, e, b):
    if s == e:
        print(*b)
        return
    else:
        for i in range(3):
            if chk[i] == 0:
                b[s] = a[i]
                chk[i] = 1
                solution(s+1, e, b)
                chk[i] = 0

a = [1,2,3]
b = [0]*3
chk = [0]*3
solution(0, 3, b)

# def solution2(s, n):
#     if s == n:
#         print(*a)
#         return
#
#     for i in range(s, n):
#         a[i], a[s] = a[s], a[i]
#         solution2(s+1, n)
#         a[i], a[s] = a[s], a[i]
#
# a = [1,2,3]
# solution2(0, 3)