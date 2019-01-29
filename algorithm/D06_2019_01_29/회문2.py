import sys
sys.stdin = open("회문2_input.txt")

def compared(data):
    max = 0
    for i in range(100):                # 행
        for k in range(100, 1, -1):     # 회문길이
            for j in range(101-k):      # 시작점
                for l in range(k//2):   # 회문검증
                    if data[i][j+l] != data[i][j+k-l-1]:
                        break
                else:
                    if k > max:
                        max = k
                        break

    yogi = max
    for m in range(100):
        for n in range(100, yogi, -1):
            for o in range(101-n):
                for p in range(n//2):
                    if data[o+p][m] != data[o+n-p-1][m]:
                        break
                else:
                    if n > max:
                        max = n
                        return max
    return max

for tc in range(1, 11):
    n = int(input())
    my_data = [input() for i in range(100)]

    print("#{} {}".format(n, compared(my_data)))

