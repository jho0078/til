import sys
sys.stdin = open("같은 모양 찾기.txt")

n = int(input())

data = [list(map(int, list(input()))) for i in range(n)]
for i in range(n):
    print(data[i])

p = int(input())

pattern = [list(map(int, list(input()))) for i in range(p)]
for i in range(p):
    print(pattern[i])

result = 0
for y in range(n-p+1):
    for x in range(n-p+1):
        flag = 0
        count = 0
        for i in range(p):
            for j in range(p):
                if data[y + i][x + j] == pattern[i][j]:
                    count += 1
                else:
                    flag = 1
                    break

            if flag == 1:
                break

        if count == p*p:
            result += 1

print(result)



