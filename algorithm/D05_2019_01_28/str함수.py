def itoa(num):
    string = ""
    while num > 1:
        string += chr(num%10+48)
        num = num//10
    return string[::-1]

print(itoa(48571))

# def itoa(x):
#     str = list()
#     i, y = 0, 0
#     while True:
#         y = x%10
#         str.append(chr(y+ord("0")))
#         x //= 10
#         if x == 0: break
#         i += 1
#
#     str.reverse()
#     str = "".join(str)
#     return str

# x = 123
# print(x, type(x))
# str1 = itoa(x)
# print(str1, type(str1))