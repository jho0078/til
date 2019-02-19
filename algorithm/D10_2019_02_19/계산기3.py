import sys
sys.stdin = open("계산기3_input.txt")

for tc in range(1, 11):
    n = int(input())
    string = list(input())

    # isp = {'(': 0, '+': 1, '-':1, '*':2, '/':2, ')': -1}
    # icp = {'(': 3, '+': 1, '-':1, '*':2, '/':2}

    # isp = {'(': 0, '+': 1, '*': 2, ')': -1}
    # icp = {'(': 3, '+': 1, '*': 2}
    #
    # stack = []
    # result = []

    # icp : 외부, isp : 내부
    # for i in string:
    #     if i not in isp:
    #         result.append(i)
    #
    #     elif stack == []:
    #         stack.append(i)
    #
    #     elif i == ')':
    #         while stack[-1] != '(':
    #             result.append(stack.pop())
    #
    #     elif icp[i] >  isp[stack[-1]]:
    #         stack.append(i)
    #
    #     elif icp[i] <=  isp[stack[-1]]:
    #         while icp[i] <=  isp[stack[-1]]:
    #             result.append(stack.pop())
    #         stack.append(i)

    stack = []
    result = []
    susic = "()+*"

    for i in string:
        if i not in susic:
            result.append(i)

        elif i == '(':
            stack.append(i)

        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        elif i == '+':
            if stack == [] or stack[-1] == '(':
                stack.append(i)
            else:
                result.append(i)

        elif i == '*':
            stack.append(i)

    stack = []
    for i in result:

        if i not in susic:
            stack.append(int(i))

        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            c = b + a
            stack.append(c)

        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            c = b * a
            stack.append(c)

    print("#{} {}".format(tc, stack[0]))






    # print("#{} {}".format(tc, tournament(0, n-1)+1))

