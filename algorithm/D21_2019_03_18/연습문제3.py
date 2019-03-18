asc = [[0,0,0,0],
       [0,0,0,1],
       [0,0,1,0],
       [0,0,1,1],
       [0,1,0,0],
       [0,1,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,0,0],
       [1,0,0,1],
       [1,0,1,0],
       [1,0,1,1],
       [1,1,0,0],
       [1,1,0,1],
       [1,1,1,0],
       [1,1,1,1]]

patterns = [[0,0,1,1,0,1],
            [0,1,0,0,1,1],
            [1,1,1,0,1,1],
            [1,1,0,0,0,1],
            [1,0,0,0,1,1],
            [1,1,0,1,1,1],
            [0,0,1,0,1,1],
            [1,1,1,1,0,1],
            [0,1,1,0,0,1],
            [1,0,1,1,1,1]]

# data = "0DEC"
data = "0269FAC9A0"

def aToh(c):
    if c <= "9":
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


t = []
for j in range(len(data)):
    for i in range(4):
        t.append(asc[aToh(data[j])][i])
print(t)
# print(len(t))

result = []
i = len(t)-1
while i >= 5:
    if t[i] == 1:
        # print(t[i-5:i+1])
        if t[i-5:i+1] in patterns:
            result.append(patterns.index(t[i-5:i+1]))
            i -= 5
    i -= 1

result.reverse()
print(' '.join(map(str, result)))

