import sys
sys.stdin = open("사칙연산_input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    fc = [0]*(N+1)
    sc = [0]*(N+1)
    symbols = [0]*(N+1)
    numbers = [0]*(N+1)

    for i in range(N):
        data = input().split()
        if len(data) > 2:
            symbols[int(data[0])] = data[1]
            fc[int(data[0])] = int(data[2])
            sc[int(data[0])] = int(data[3])
        else:
            numbers[int(data[0])] = int(data[1])

    print(fc)
    print(sc)
    print(symbols)
    print(numbers)

    for i in range(N, 0, -1):
        if symbols[i] != 0:
            if symbols[i] == '+':
                numbers[i] = numbers[fc[i]] + numbers[sc[i]]
            elif symbols[i] == '-':
                numbers[i] = numbers[fc[i]] - numbers[sc[i]]
            elif symbols[i] == '*':
                numbers[i] = numbers[fc[i]] * numbers[sc[i]]
            elif symbols[i] == '/':
                numbers[i] = numbers[fc[i]] // numbers[sc[i]]

    print("#{} {}".format(tc, numbers[1]))







