n, data = input().split()
N = int(n)

table = [[] for _ in range(51)]

i = 0
stage = 0
zerocount = 0
while i < len(data):

    if data[i] == '<':
        if data[i+1] == '>':
            i += 1
        else:
            i += 1
            stage += 1
            num = data[i]

            j = 1
            while True:
                if data[i + j] != '>' and data[i + j] != '<':
                    num += data[i + j]
                    j += 1
                else:
                    break

            table[stage].append(num)
            i += j - 1

            # table[stage].append(data[i+1])
            # i += 1

    elif data[i] == '>':
        stage -= 1
    else:
        table[stage].append(data[i])

    i += 1

print(table)
print(' '.join(table[N]))


