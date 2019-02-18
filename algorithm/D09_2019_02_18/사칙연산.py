# inputs = "2+3*4/5"
# yeon = "+-*/"
# result = ""
# stack = []
#
# for i in range(len(inputs)):
#     if inputs[i] not in yeon:
#         result += inputs[i]
#     else:
#         stack.append(inputs[i])
# for i in range(len(stack)):
#     result += stack.pop()
#
# print(result)


token = {'+': 1, '-': 1, '*': 2, '/': 2}
result = ""
stack = []

for i in range(len(inputs)):
    if inputs[i] not in token:
        result += inputs[i]
    else:
        if

