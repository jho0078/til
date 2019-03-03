def find(K):
    global C, R
    number = 0
    i = 0

    # K의 번호값에서 외곽 좌석의 갯수만큼 계속해서 뺀다.
    # 뺄 때마다 내부 층수 i는 증가한다.
    # (K가 현재의 외곽 좌석 갯수보다 작아질때까지)

    while True:

        around = (C + R - 4 * i) * 2 - 4
        if K - around > 0:
            K -= around
            number += around
            i += 1

        else:
            x = i + 1
            y = i
            width = C - 2 * i
            height = R - 2 * i

            # i 층의 외곽을 돌면서 번호값에 해당하는 좌표를 찾아낸다.
            k = 0
            while True:

                plus = [height, width - 1, height - 1, width - 2]

                if K > plus[k]:
                    K -= plus[k]
                    number += plus[k]
                    k += 1

                else:
                    if k == 0:
                        y += K
                    elif k == 1:
                        y += height
                        x += K
                    elif k == 2:
                        y += height - K
                        x += width - 1
                    elif k == 3:
                        y += 1
                        x += width - 1 - K

                    return x, y

# C, R = map(int, input().split())
# K = int(input())

C, R = 7, 6
K = 11

# for i in range(1, 44):
#     print(f'{i}:{find(i)}')

print(*find(K))









