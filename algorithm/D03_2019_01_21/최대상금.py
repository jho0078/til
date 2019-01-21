
for j in range(n)

    for i in range(len(data)):
        if data[i] >= max:
            max_index = i
        if data[i] < min:
            min_index = i
    data[min_index], data[max_index] = data[max_index], data[min_index]