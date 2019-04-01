import sys
sys.stdin = open("최소이동거리_input.txt")

def Prim(N, s):
    D = [999999]*(N+1)  # 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
    P = [-1]*(N+1)      # 최단 경로 트리 저장
    visited = [0]*(N+1)
    D[s] = 0        # 시작 정점의 가중치를 0으로 설정

    # 정점의 개수만큼 반복
    for k in range(N+1):
        minindex = -1
        min = 999999999

        # 방문 안한 정점 중 최소 가중치 정점 찾기
        for i in range(N+1):
            if not visited[i] and D[i] < min:
                min = D[i]
                minindex = i
        visited[minindex] = 1

        for i in range(N+1):
            if not visited[i] and data[minindex][i] != 0 and D[minindex] + data[minindex][i] < D[i]:
                D[i] = D[minindex] + data[minindex][i]
                print(D)
                P[i] = minindex

    return D[N]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    data = [[0]*(N+1) for i in range(N+1)]

    edge = [list(map(int, input().split())) for i in range(E)]
    for i in range(E):
        data[edge[i][0]][edge[i][1]] = edge[i][2]

    print("#{} {}".format(tc, Prim(N, 0)))


