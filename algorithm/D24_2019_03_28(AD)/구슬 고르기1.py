# def myset(s, e):
#     if s == e:
#         print(*b)
#         return
#
#     for i in range(2):
#         if i == 0:
#             b[s] = a[s]
#             myset(s + 1, e)
#             b[s] = 0
#
#         else:
#             myset(s + 1, e)

def myset(s, e):
    if s == e:
        print(*b)
        return

    b[s] = a[s]
    myset(s + 1, e)
    b[s] = 0
    myset(s + 1, e)

a = [1,2,3]
b = [0]*3
myset(0, 3)