new_arr = [[0 for _ in range(5)] for _ in range(5)]

arr = [[9,20,2,18,11],
       [19,1,25,3,21],
       [8,24,10,17,7],
       [15,4,16,5,6],
       [12,13,22,23,14]]

def iswall(x, y):
    if x < 0 or x >= 5: return True
    if y < 0 or y >= 5: return True
    if arr[]
    return False

dx = [1, 0, -1, 0]   #   우,하,좌,상
dy = [0, 1, 0, -1]   #i= 0, 1, 2, 3

sum = 0
for i in range(len(arr), 0, -2):

len(arr) = L
for i in range(1, L//2 + 1):
    for x in range(0+i, L-i):
        new_arr[]

    for x in range(0, len(arr[0])-1):
        new_arr[y=0][x] = arr[y=0][x]
    for y in range(0, len(arr[0])-1):
        new_arr[y][x=4] = arr[y][x=4]
    for x in range(len(arr[0])-2, 0, -1):
        new_arr[y=4][x] = arr[y=4][x]
    for y in range(len(arr[0])-2, 0, -1):
        new_arr[y][x=0] = arr[y][x=0]

    for x in range(1, len(arr[0])-2)

for i in range(6, 0, -2):
    print(i)

        #
        # for i in range(4):
        #     testX = x + dx[i]
            #
            #
            # testY = y + dy[i]
            # if iswall(testX, testY) == False:
            #     sum += calAbs(arr[y][x], arr[testY][testX])