import sys
sys.stdin = open("회문2_input.txt")

def compared(data):
    for k in range(100, 1, -1):         # 회문길이
        for i in range(100):            # 행
            for j in range(101-k):      # 시작점
                for l in range(k//2):   # 회문검증
                    if data[i][j+l] != data[i][j+k-l-1]:
                        break
                else:
                    return k

                for m in range(k//2):
                    if data[j+m][i] != data[j+k-m-1][i]:
                        break
                else:
                    return k

for tc in range(1, 11):
    n = int(input())
    my_data = [input() for i in range(100)]

    print("#{} {}".format(n, compared(my_data)))

