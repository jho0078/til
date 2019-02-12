import sys
sys.stdin = open("반복문자 지우기_input.txt")


def banbok(data):
    while True:
        count = 0
        result = []
        result.append(data[0])
        for i in range(1, len(data)):
            if len(result) == 0 or result[-1] != data[i]:
                result.append(data[i])
            else:
                result.pop(-1)
                count += 1

        if count == 0:
            return len(result)

        data = result[:]

T = int(input())
for tc in range(1, T+1):
    data = input()

    print("#{} {}".format(tc, banbok(data)))
