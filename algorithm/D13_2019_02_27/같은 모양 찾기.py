n = int(input())

data = [list(map(int, list(input()))) for i in range(n)]

p = int(input())

pattern = [list(map(int, list(input()))) for i in range(p)]

for i in range(n-p+1):
    for j in range(n-p+1):
        if data[i][j] == pattern[0][0]:


