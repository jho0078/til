T = int(input())
for tc in range(1, T+1):
    data = list(map(int, list(input())))
    count = 0
    i = 0
    while i < len(data):
        if data[i] == 1:
            count += 1
            for j in range(len(data[i+1:])):
                if data[i+1+j] == 1:
                    data[i+1+j] = 0
                else:
                    data[i+1+j] = 1
        i += 1
    print("#{} {}".format(tc, count))