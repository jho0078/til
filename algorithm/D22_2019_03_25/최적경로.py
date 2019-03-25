import sys
import time
from time import strftime
sys.stdin = open("최적경로_input.txt")

start_time = time.time()

#
# def caldistance(n):
#     distance = 0
#     for i in range(2, n-1):
#         distance += abs(data[i][0] - data[i+1][0]) + abs(data[i][1] - data[i+1][1])
#     # distance += abs(data[0][0] - data[2][0]) + abs(data[0][1] - data[2][1])
#     distance += abs(data[1][0] - data[n-1][0]) + abs(data[1][1] - data[n-1][1])
#     # print(distance)
#
#     return distance

def solution(n, idx, distance):
    global mind, count


    if distance > mind:
        return

    if n-1 == idx:

        distance += abs(data[idx-1][0] - data[idx][0]) + abs(data[idx-1][1] - data[idx][1])
        if distance < mind:
            mind = distance
    else:
        for i in range(idx, n-1):
            data[i], data[idx] = data[idx], data[i]
            plus = abs(data[idx-1][0] - data[idx][0]) + abs(data[idx-1][1] - data[idx][1])
            solution(n, idx+1, distance + plus)
            data[i], data[idx] = data[idx], data[i]



T = 10
for tc in range(1, T+1):
    N = int(input())
    dummy = list(map(int, input().split()))
    data = []
    for i in range(4, len(dummy), 2):
        data.append([dummy[i], dummy[i+1]])
    data.append([dummy[2], dummy[3]])
    data.insert(0, [dummy[0], dummy[1]])

    print(data)
    count = 0
    mind = 1000000
    n = len(data)
    solution(n, 1, 0)
    print("#{} {}".format(tc, mind))

    memoization = []

print(time.time() - start_time, 'seconds')
