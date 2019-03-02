# import math
# R = int(input())
R = 5

data = [[0 for _ in range(R+1)] for _ in range(R+1)]
# for i in range(R+1):
#     print(data[i])

count = 0
for y in range(1, R+1):
    for x in range(1, R+1):
        # if (y ** 2 + x ** 2) ** (1 / 2) < R or ((y ** 2 + x ** 2) ** (1 / 2) - R) < 10 ** (-10):
        # if (y**2 + x**2)**(1/2) < R or math.isclose((y**2 + x**2)**(1/2), R):
        if (y ** 2 + x ** 2) ** (1 / 2) <= R:
            print(y, x, (y**2 + x**2)**(1/2), R)
            count += 1
            data[y][x] = 1

print(count*4)
for i in range(R+1):
    print(data[i])

