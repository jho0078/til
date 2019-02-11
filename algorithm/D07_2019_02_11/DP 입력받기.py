n = 7 #정점의 갯수
inputs = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"

# n =  int(input())
# n += 1              # 한 줄씩 더 만들어줘야 한다.
hangyol = [[0 for i in range(n)] for j in range(n)]
data = list(map(int, inputs.split()))

for i in range(0, len(data), 2):
    hangyol[data[i]][data[i+1]] = 1
    hangyol[data[i+1]][data[i]] = 1

for i in range(n):
    print(i, hangyol[i])