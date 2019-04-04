def check(no, color):
    for i in range(no):
        if arr[no][i] and rec[i] == color:
            return 0
    return 1

def DFS(no):
    global flag
    if no >= N:
        flat = 1
        return

    for i in range(1, M+1):
        if check(no, i):
            rec[no] = i
            DFS(no+1)
            if flag:
                return


# main-------------------------------------------
N, M = map(int, input().split())
rec = [0]*N  # 색상기록
arr = []     # 인접행렬
for i in range(N): # 0행 0열부터 시작
    arr.append(list(map(int, input().split())))

flag = 0
DFS(0)  # 첫번째 노드부터 시작
if flag:
    for i in range(N):
        print(rec[i], end=' ')
else: print(-1)