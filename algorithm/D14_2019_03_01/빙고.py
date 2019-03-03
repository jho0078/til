import sys
sys.stdin = open("빙고.txt")

# 빙고의 갯수가 3개인지 검사
def bingo():
    bingo_number = 0
    zero_diagonal = 0
    zero_rdiagonal = 0

    for i in range(5):
        zero_row = 0
        zero_column = 0

        if data[i][i] == 0:
            zero_diagonal += 1
        if data[4-i][i] == 0:
            zero_rdiagonal += 1

        for j in range(5):
            if data[i][j] == 0:
                zero_row += 1
            if data[j][i] == 0:
                zero_column += 1

        if zero_row == 5:
            bingo_number += 1
        if zero_column == 5:
            bingo_number += 1
        if zero_diagonal == 5:
            bingo_number += 1
        if zero_rdiagonal == 5:
            bingo_number += 1

    if bingo_number >= 3:
        return True
    else:
        return False

# 숫자를 하나씩 뽑아 0으로 만들면서 빙고여부를 체크
def inspect(count):
    while numbers:
        a = numbers.pop(0)
        p = 0
        for i in range(5):
            for j in range(5):
                if data[i][j] == a:
                    data[i][j] = 0
                    p = 1
                    count += 1
                    if bingo():
                        return count
                    else:
                        break

            if p == 1 or p == 2:
                break
    return 0

# 입력값
data = [list(map(int, input().split())) for i in range(5)]

# 첫 10개까지는 받아서 0으로 체크(빙고가 일어나지 않으므로)
for i in range(2):
    numbers = list(map(int, input().split()))
    while numbers:
        a = numbers.pop(0)
        p = 0
        for i in range(5):
            for j in range(5):
                if data[i][j] == a:
                    data[i][j] = 0
                    p = 1
                    break
            if p == 1:
                break

# 나머지 값을 받으면서 빙고여부 체크
count = 10
for i in range(3):
    numbers = list(map(int, input().split()))
    a = inspect(count)

    # for i in range(5):
    #     print(data[i])

    if a > 0:
        print(a)
        break
    else:
        count += 5



