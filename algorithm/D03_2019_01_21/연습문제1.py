arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))


def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    return False

def calAbs(y, x):
    if y - x > 0: return y - x
    else: return x - y

# i : 행
# j : 열

dx = [0, 0, -1, 1]   #   상,하,좌,우
dy = [-1, 1, 0, 0]   #i= 0, 1, 2, 3

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if iswall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[testY][testX])

print("sum = {}".format(sum))


# arr = [[1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 1],
#        [1, 0, 0, 0, 1],
#        [1, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1]]

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1