import sys
sys.stdin = open("이진수_input.txt")

asc = [[0,0,0,0],
       [0,0,0,1],
       [0,0,1,0],
       [0,0,1,1],
       [0,1,0,0],
       [0,1,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,0,0],
       [1,0,0,1],
       [1,0,1,0],
       [1,0,1,1],
       [1,1,0,0],
       [1,1,0,1],
       [1,1,1,0],
       [1,1,1,1]]

def sixteen(c):
    if c <= "9":
        return ord(c) - ord("0")
    else:
        return ord(c) - ord("A") + 10

T = int(input())
for tc in range(1, T+1):
    N, data = input().split()

    result = ""
    for i in range(len(data)):
        for j in range(4):
            result += str(asc[sixteen(data[i])][j])

    print("#{} {}".format(tc, result))


