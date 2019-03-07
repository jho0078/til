import sys
sys.stdin = open("원안의 마을.txt")

def giji():
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x

N = int(input())
data = [list(map(int, list(input()))) for i in range(N)]

y, x = giji()

max_distance = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            distance = ((y-i)**2 + (x-j)**2)**(1/2)
            if distance > max_distance:
                max_distance = distance

for i in range(1, 14):
    if i >= max_distance:
        print(i)
        break



