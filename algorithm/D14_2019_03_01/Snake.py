import sys
sys.stdin = open("Snake.txt")

def iswall(y, x):
    if y < 1 or x < 1 or y >= N or x >= N:
        True
    else:
        False

N = int(input())
K = int(input())
table = [[0 for _ in range(N)] for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    table[r][c] = 1

L = int(input())
# for i in range(L):
#     move = input().split()
#     time = int(move[0])
#     rotate = move[1]
move = [input().split() for i in range(L)]
for i in range(N):
    print(table[i])
print(move)

x = 1
y = 1
i = 1
while True:
    for i in range(L):
    # D(정방향), L(역방향)
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    ny = y + dy
    nx = x + dx




