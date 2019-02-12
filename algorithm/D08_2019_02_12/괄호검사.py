import sys
sys.stdin = open("괄호검사_input.txt")

def bracket(data):
    stack = []
    bracket_dic = {')': '(', '}': '{'}
    for i in data:
        if i in bracket_dic.values():
            stack.append(i)

        elif i in bracket_dic:
            if stack == []:
                return 0
            elif bracket_dic[i] == stack[-1]:
                stack.pop(-1)
            else:
                return 0

    if stack == []:
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    datas = input()

    print("#{} {}".format(tc, bracket(datas)))



