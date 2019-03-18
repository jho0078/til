data = input()
result = ""
for i in range(len(data)):
    if data[i].islower():
        result += data[i].upper()
    else:
        result += data[i]

print(result)