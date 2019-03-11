import sys
sys.stdin = open("뿌요뿌요_input.txt")

R, C, K = map(int, input().split())
data = [list(map(int, input().split())) for i in range(R)]

table = [[0 for _ in range(R)] for _ in range(2*R)]
result = [[0 for _ in range(R)] for _ in range(2*R)]

for i in range(R):
    for j in range(R):
        result[R+i][j] = data[i][j]

def inspect():
    for i in range(2*R):
        for j in range(R):
            if result[i][j] != table[i][j]:
                return 0
    return 1

def chain():
    for_print = []
    for i in range(2):
        if i == 0:
            for j in range(C - 1):
                for K1 in range(K):
                    for K2 in range(K):
                        fall(0, j, K1)
                        fall(0, j + 1, K2)
                        chain()

        else:
            for j in range(C):
                for K1 in range(K):
                    for K2 in range(K):
                        fall(1, j, K1)
                        fall(0, j, K2)
                        chain()
        if inspect():
            for m in range(len(for_print)):
                print(' '.join(for_print[m]))





def fall(y, x, K):
    while 1:
        if y == 0 or table[y-1][x] != 0:
            table[y][x] = K
            return
        y -= 1




for_print = []
for i in range(2):
    if i == 0:
        for j in range(C-1):
            for K1 in range(K):
                for K2 in range(K):
                    fall(0, j, K1)
                    fall(0, j+1, K2)
                    chain()

    else:
        for j in range(C):
            for K1 in range(K):
                for K2 in range(K):
                    fall(1, j, K1)
                    fall(0, j, K2)
                    chain()
    if inspect():
        for m in range(len(for_print)):
            print(' '.join(for_print[m]))





