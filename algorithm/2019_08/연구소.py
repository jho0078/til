import sys
sys.stdin = open("연구소_input.txt")

def check():
    count = 0
    data = [i[:] for i in A]

    for pi in pick:
        data[pi[0]][pi[1]] = 1

    for vi in virus:
        y, x = vi[0], vi[1]
        q = []
        q.append([y, x])
        while q:
            y, x = q.pop(0)
            for dy, dx in (1,0), (-1,0), (0,1), (0,-1):
                ny, nx = y + dy, x + dx
                if -1 < ny < N and -1 < nx < M and data[ny][nx] == 0:
                    q.append([ny, nx])
                    data[ny][nx] = 2
                    count += 1

    return len(empty) - count - 3


def sol(s, start):
    global MAX

    if s == 3:
        # print(pick)
        count = check()
        if count > MAX:
            MAX = count
        return

    for i in range(start, len(empty)):
        pick[s] = empty[i]
        sol(s+1, i+1)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
virus = []
empty = []
pick = [0]*3
MAX = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            virus.append([i,j])
        elif A[i][j] == 0:
            empty.append([i,j])

# print(virus)
sol(0,0)
print(MAX)