# input
# 10
# 5 10
# 0000000000
# 0123456789
# 0000000000
# 0000000000
# 0000000000
#
# T = int(input())
# print(T)
# N, M = map(int, input().split())
# print(N, M, sep=" ")
# for i in range(N):
#     data = list(map(int, list(input())))
#     for j in range(len(data)):
#         print(data[j], end="")
#     print()

# input
# 0000000111100000011000000111100110000110000111100111100111111001100111

# data = list(map(int, list(input())))
# # print(data)
# for i in range(0, len(data), 7):
#     ten = 0
#     # print(data[i+6:i-1:-1])
#     for j in range(len(data[i+6:i-1:-1])):
#         ten += data[i+6:i-1:-1][j] * (2**j)
#     print(ten)

data = list(map(int, list(input())))

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += "1"
        else:
            output += "0"
    print(output)

a = 0x86
key = 0xAA

print("a  ==>", end="")
Bbit_print(a)


