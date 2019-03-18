alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = input()
for i in range(len(data)):
    print(alphabet.index(data[i]), end=" ")