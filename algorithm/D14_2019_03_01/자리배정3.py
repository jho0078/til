def find(K):
    global C, R
    number = 0
    i = 0
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

            k = 0
            while True:

                plus = [height, width - 1, height - 1, width - 2]

                if K > plus[k]:
                    K -= plus[k]
                    number += plus[k]
                    k = k + 1

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

C, R = map(int, input().split())
K = int(input())

if K > C*R:
    print("0")
else:
    print(*find(K))