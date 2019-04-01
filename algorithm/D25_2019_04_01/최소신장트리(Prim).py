import sys
sys.stdin = open("최소신장트리_input.txt")

def Prim(V, s):
    key = [999999]*(V+1)  # 가중치 무한대로 설정
    pi = [-1]*(V+1)       # 트리에서 연결될 부모 정점 초기화
    visited = [0]*(V+1)
    key[s] = 0        # 시작 정점의 가중치를 0으로 설정

    # 정점의 개수만큼 반복
    result = 0
    for k in range(V+1):
        minindex = -1
        min = 999999

        # 방문 안한 정점 중 최소 가중치 정점 찾기
        for i in range(V+1):
            if not visited[i] and key[i] < min:
                min = key[i]
                minindex = i
        visited[minindex] = 1
        result += key[minindex]

        for i in range(V+1):
            if not visited[i] and data[minindex][i] != 0 and data[minindex][i] < key[i]:
                key[i] = data[minindex][i]
                pi[i] = minindex

    return result


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0]*(V+1) for i in range(V+1)]

    edge = [list(map(int, input().split())) for i in range(E)]
    for i in range(E):
        data[edge[i][0]][edge[i][1]] = edge[i][2]
        data[edge[i][1]][edge[i][0]] = edge[i][2]

    print("#{} {}".format(tc, Prim(V, 0)))
