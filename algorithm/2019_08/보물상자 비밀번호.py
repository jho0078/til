import sys
sys.stdin = open("보물상자 비밀번호_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = list(input())

    numbers = []
    length = N//4
    numset = {"0": 0, "1": 1, "2":2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
              "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for k in range(length):
        for i in range(0, len(data)-length+1, length):
            hexa = data[i:i+length]
            decimal = 0
            for j in range(length):
                decimal += numset[hexa[length-1-j]]*(16**j)
            if decimal not in numbers:
                numbers.append(decimal)
        data.insert(0, data.pop(-1))
    numbers.sort()

    print("#{} {}".format(tc, numbers[len(numbers)-K]))

