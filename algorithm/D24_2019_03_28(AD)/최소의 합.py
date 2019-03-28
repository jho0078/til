# def Rcom(s, n, sum1):
#     global min_sum1
#
#     if sum1 > min_sum1:
#         return
#
#     if s == n:
#         if sum1 < min_sum1:
#             min_sum1 = sum1
#             return
#
#     for i in range(n):
#         Rcom(s+1, n, sum1+table[s][i])

def Rcom():
    sum1 = 0
    for i in range(n):
        sum1 += min(table[i])
    return sum1

def com(s, n, sum1):
    global min_sum2

    if sum1 > min_sum2:
        return

    if s == n:
        if sum1 < min_sum2:
            min_sum2 = sum1
            return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            com(s + 1, n, sum1 + table[s][i])
            visited[i] = 0


n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
visited = [0]*n
min_sum1 = 100000
min_sum2 = 100000
# Rcom(0, n, 0)
# print(min_sum1)
print(Rcom())
com(0, n, 0)
print(min_sum2)

# 4
# 1 5 3 9
# 2 4 7 3
# 5 3 5 2
# 3 1 8 1