import sys
sys.stdin = open("격자판_input.txt")

def findnum(x, y, num, s):
    global sum

    if s == 6:
        # print(num)
        if num not in numlist:           
            numlist.append(num)
            sum += 1
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and ny >=0 and nx < 4 and ny < 4 and num not in visited[s][ny][nx]:
            visited[s][ny][nx].append(num)
            num += table[nx][ny]
            findnum(nx, ny, num, s+1)
            num = num[:len(num)-1]


T = int(input())
for tc in range(1, T+1):
    table = [list(input().split()) for i in range(4)]
    visited = [[[[] for _ in range(4)] for _ in range(4)] for _ in range(6)]  
    
    sum = 0
    numlist = []
    num = ''
    for i in range(4):
        for j in range(4):            
            findnum(i, j, table[i][j], 0) 

    print("#{} {}".format(tc, sum))



