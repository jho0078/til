# def move(y, x, s, d):
#     direction = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]
#
#     while s > 0:
#         nexty = y + direction[d][0]
#         nextx = x + direction[d][1]
#         if nexty < 0:
#             d = 2
#             nexty = y + direction[d][0]
#
#         elif nexty >= R:
#             d = 1
#             nexty = y + direction[d][0]
#
#         elif nextx < 0:
#             d = 3
#             nextx = x + direction[d][1]
#
#         elif nextx >= C:
#             d = 4
#             nextx = x + direction[d][1]
#
#         y = nexty
#         x = nextx
#         s -= 1
#
#     return y, x, d

def move(y, x, s, d):
    direction = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]

    if 1 <= d <= 2:
        nexty = y + direction[d][0]*s
        if (nexty/(R-1))%2:
            nexty = R-1 - (nexty%(R-1))
            if d == 1:
                d = 2
            else:
                d = 1
        else:
            nexty = nexty%(R-1)

        return nexty, x, d

    else:
        nextx = x + direction[d][1]*s
        if (nextx//(C-1))%2:
            nextx = C-1 - (nextx%(C-1))
            if d == 3:
                d = 4
            else:
                d = 3
        else:
            nextx = nextx%(C-1)

        return y, nextx, d


def solution(pos, miny):

    result = 0
    for i in range(C):

        # 2. 상어잡기
        if miny != 999:
            result += pos[(miny, i)][2]

            del pos[(miny, i)]

        if not pos:
            return result

        newpos = {}
        miny = 999
        for key in pos:
            s, d, z = pos[key]
            y, x, d = move(key[0], key[1], s, d)
            if (y, x) in newpos:
                if z > newpos[(y, x)][2]:
                    newpos[(y, x)] = (s, d, z)
            else:
                newpos[(y, x)] = (s, d, z)

            if x == i + 1:
                if miny > y:
                    miny = y

        print("newpos", newpos)
        pos = newpos

    return result


R, C, M = map(int, input().split())
table = [[0]*R for _ in range(C)]
pos = {}

MIN = 999

for i in range(M):
    r, c, s, d, z = map(int, input().split())

    if c-1 == 0:
        if MIN > r-1:
            MIN = r-1

    pos[(r-1, c-1)] = (s, d, z)

print("pos", pos)
print(solution(pos, MIN))

print(-4//3)
print(-4%3)