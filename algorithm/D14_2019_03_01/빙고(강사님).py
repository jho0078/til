import sys
sys.stdin = open("빙고.txt")

def isbingo():
    count = 0
    crosssum1 = 0
    crosssum2 = 0
    for i in range(5):
        rsum = 0
        csum = 0
        for j in range(5):
            rsum += data[i][j]
            csum += data[j][i]
        if rsum == 0:
            count += 1
        if csum == 0:
            count += 1
        crosssum1 += data[i][i]
        crosssum2 += data[4-i][i]
    if crosssum1 == 0:
        count += 1
    if crosssum2 == 0:
        count += 1

    if count >= 3:
        return 1
    else:
        return 0


data = [list(map(int, input().split())) for i in range(5)]

numbers = []
for i in range(5):
    numbers += list(map(int, input().split()))

for k in range(len(numbers)):
    p = 0
    for i in range(5):
        for j in range(5):
            if data[i][j] == numbers[k]:
                data[i][j] = 0
                p = 1
                break
        if p == 1:
            break
    for l in range(5):
        print(data[l])
    print()
    if isbingo():
        print(k+1)
        break