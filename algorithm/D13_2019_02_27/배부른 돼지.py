import sys
sys.stdin = open("배부른 돼지_input.txt")

n = int(input())

# data = [3, 4, 5, 6, 7, 8, 9]
# for i in range(n):
#     num, yorn = map(int, input().split())
#     if yorn == "N":
#         for i in range(len(data)):
#             if data[i] > num:
#
mins = 10
maxs = 0

for i in range(n):
    inputs = input().split()
    num = int(inputs[0])
    yorn = inputs[1]

    if yorn == "Y":
        if num <= mins:
            mins = num

    if yorn == "N":
        if num >= maxs:
            maxs = num

if mins != 10 and mins > maxs:
    print(mins)

else:
    print("F")

inputs = "4 N"
a, b = inputs.split()
print(a, b)