import sys
sys.stdin = open("forth_input.txt")

T = int(input())
for tc in range(1, T+1):
    operator = "+-*/."
    stack = []
    string = input().split()

    for i in string:
        if i == '.':
            if len(stack) > 1:
                print("#{} {}".format(tc, "error"))
                break
            else:
                print("#{} {}".format(tc, stack[0]))

        elif i not in operator:
            stack.append(i)

        else:
            if len(stack) < 2:
                print("#{} {}".format(tc, "error"))
                break

            a = stack.pop()
            b = stack.pop()
            if i == '+':
                c = int(b) + int(a)
                stack.append(c)
            elif i == '-':
                c = int(b) - int(a)
                stack.append(c)
            elif i == '*':
                c = int(b) * int(a)
                stack.append(c)
            elif i == '/':
                c = int(b) / int(a)
                stack.append(int(c))



