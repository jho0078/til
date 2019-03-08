import sys
sys.stdin = open("쇠막대기.txt")

data = input()

i = 0
count = 0
layer = 0
while i < len(data):
    if data[i] == '(':
        if data[i+1] == ')':
            i += 1
            count += layer
        else:
            layer += 1
    else:
        count += 1
        layer -= 1
    i += 1

print(count)
