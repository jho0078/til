def bubblesort(data):
    for i in range(len(data)-1, 0, -1):  #i = 4 3 2 1
        for j in range(0, i):            #i = 4 3 2 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

data = [55,7,78,12,42]
# data.sort()
# data.reverse()

# call by value 와 call by reference