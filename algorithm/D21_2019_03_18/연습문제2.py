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


# data = "0F97A3"
data = "68B46DDB9346F4"

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
print(len(t))

for i in range(0, len(t), 7):
    ten = 0
    print(t[i:i+7][::-1])
    for j in range(len(t[i:i+7][::-1])):

        ten += t[i:i+7][::-1][j] * (2**j)
    print(ten)

