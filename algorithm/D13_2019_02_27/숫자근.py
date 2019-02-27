import sys
sys.stdin = open("숫자근.txt")

# def digitroot(number):
#     droot = 0
#     while number >= 10:
#         droot += number%10
#         number = number//10
#     droot += number
#     return droot
#
# n = int(input())
# max = 0
# for i in range(n):
#     number = int(input())
#     a = number
#     while a >= 10:
#         a = digitroot(a)
#
#     if a > max:
#         max = a
#         min_number = number
#     elif a == max:
#         if number < min_number:
#             min_number = number
#
# print(min_number)

# a = "9 "
# print(int(a))

# a = "923 "
# print(list(a.strip()))


max = 0
n = int(input())

for i in range(n):
    number = int(input().strip())
    a = number
    while a >= 10:
        a = sum(map(int, list(str(a))))

    if a > max:
        max = a
        min_number = number
    elif a == max:
        if number < min_number:
            min_number = number

print(min_number)

