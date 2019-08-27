import sys
sys.stdin = open("점심 식사시간_input.txt")

def sol():
    time = 0
    end = 0
    first = first_origin[:]
    second = second_origin[:]
    while end < len(man):
        end = 0
        if len(first):
            instair = 0
            for i in range(len(first)):
                if -stair[0][2] < first[i] < 0:
                    instair += 1

            for i in range(len(first)):
                if -stair[0][2] < first[i]:
                    if first[i] == 0:
                        if instair < 3:
                            first[i] -= 1
                            instair += 1
                    else:
                        first[i] -= 1
                if first[i] <= -stair[0][2]:
                    end += 1

        if len(second):
            instair = 0
            for i in range(len(second)):
                if -stair[1][2] < second[i] < 0:
                    instair += 1

            for i in range(len(second)):
                if -stair[1][2] < second[i]:
                    if second[i] == 0:
                        if instair < 3:
                            second[i] -= 1
                            instair += 1
                    else:
                        second[i] -= 1
                if second[i] <= -stair[1][2]:
                    end += 1

        time += 1
        if time > MIN:
            return 9999

    return time


def dfs(s):
    global MIN

    if s == len(man):
        time = sol()
        if time < MIN:
            MIN = time

        return

    for i in range(2):
        if i: second_origin.append(distance[i][s]+1)
        else: first_origin.append(distance[i][s]+1)
        dfs(s+1)
        if i: second_origin.pop()
        else: first_origin.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for i in range(N)]
    MIN = 9999

    man = []
    stair = []
    first_origin = []
    second_origin = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                man.append([i,j])
            elif A[i][j] > 1:
                stair.append([i,j,A[i][j]])

    distance = [[0] * len(man) for i in range(2)]
    for i in range(2):
        for j in range(len(man)):
            distance[i][j] = abs(stair[i][0] - man[j][0]) + abs(stair[i][1] - man[j][1])

    dfs(0)
    print("#{} {}".format(tc, MIN))
