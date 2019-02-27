# data = input()
data = "()()()(((())()"
# print(spl)

# data = input()
result = 10
for i in range(1, len(data)):
    if data[i-1] != data[i]:
        result += 10
    else:
        result += 5
print(result)

