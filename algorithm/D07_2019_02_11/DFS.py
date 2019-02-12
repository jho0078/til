n = 7 #정점의 갯수
inputs = "1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7"
n += 1
# n =  int(input())
# n += 1              # 한 줄씩 더 만들어줘야 한다.
hangyol = [[0 for i in range(n)] for j in range(n)]
data = list(map(int, inputs.split()))

for i in range(0, len(data), 2):
    hangyol[data[i]][data[i+1]] = 1
    hangyol[data[i+1]][data[i]] = 1

# for i in range(n):
#     print(i, hangyol[i])

visited = [0]*n

# 재귀
def dfs(items, v):
    global visited
    visited[v] = 1     # visited(list)는 참조형이기 때문에 값이 변경되면 그대로 반영된다.(=하나의 리스트를 참조)
    print(v, end=" ")

    for i in range(n):
        if items[i][v] == 1:
            if visited[i] == 0:
                dfs(items, i)

dfs(hangyol, 1)
