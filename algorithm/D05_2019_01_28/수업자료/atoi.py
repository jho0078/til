def atoi(string):
    value=0
    i = 0
    while (i < len(string)) :
        c = string[i]
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit;
        i += 1
    return value

a = "123"
print(type(a))
b = atoi(a)
print(type(b))
c = int(a)
print(type(c))