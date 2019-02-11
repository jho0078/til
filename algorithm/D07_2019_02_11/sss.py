#
# def aus(cmds):
#     q = []
#     for i in cmds:
#         if "PUSH" in i:
#             q.append(int(i.split()[1]))
#         elif "POP" in i:
#             # if q != []:
#             del q[0]
#
#     return q
#
# cmds = ["PUSH 1","PUSH 2","PUSH 3","POP", "POP", "POP", "PUSH 7"]
# print(aus(cmds))

def solution(x1, m1, x2, m2):
    start = x1
    end = x2
    middle = (start + end)/2
    while abs(m1 / (middle - x1) ** 2 - m2 / (x2 - middle) ** 2) > 10 ** -11:

        if m1 / (middle - x1) ** 2 < m2 / (x2 - middle) ** 2:
            end = middle
        else:
            start = middle

        middle = (start + end) / 2
    return middle

print(solution(1, 1, 2, 1000))
