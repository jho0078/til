V,  E = 13, 12
inputs = "1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13"

data = list(map(int, inputs.split()))
# print(data)

table = [[0 for _ in range(4)] for _ in range(V)]

for i in range(V):
    table[i][0] = i + 1
#
# for i in range(V):
#     print(table[i])

for i in range(0, len(data), 2):
    if table[data[i]-1][1] == 0:
        table[data[i]-1][1] = data[i+1]
    else:
        table[data[i]-1][2] = data[i+1]

    table[data[i+1]-1][3] = data[i]

for i in range(V):
    print(' '.join(map(str, table[i])))