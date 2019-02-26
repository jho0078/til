import sys
sys.stdin = open("피자 굽기_input.txt")

# 치즈양이 0이 될 때까지 나누기
def division():
    while True:
        for i in range(len(queue)):
            if queue[i][1] == 0:
                return

        for i in range(len(queue)):
            queue[i][1] = queue[i][1] // 2

def pizza():

    while True:
        # 나누기
        division()

        # 데이터에 값이 있으면 items의 첫번째 값을 뽑아서 queue에 추가
        if items:
            for i in range(N):
                if items and queue[i][1] == 0:
                    queue[i] = items.pop(0)

        # 데이터 값이 없다면
        else:
            # queue의 요소가 하나가 될 때까지 division과 pop을(0이 된 요소) 반복
            while len(queue) > 1:
                for i in range(len(queue)):
                    if queue[i][1] == 0:
                        queue.pop(i)
                        break

                division()

            return queue[0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    items = []

    # 피자의 번호와 치즈양을 요소로 가진 리스트를 items에 append
    for i in range(M):
        items.append([i+1, data[i]])

    # queue : 화덕, 화덕에 먼저 피자를 채워넣는다
    queue = []
    for i in range(N):
        queue.append(items.pop(0))

    print("#{} {}".format(tc, pizza()[0]))



