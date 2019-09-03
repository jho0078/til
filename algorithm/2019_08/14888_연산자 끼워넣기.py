def sol(s, result):
    global MAX, MIN

    if s == len(numbers)-1:
        MAX = max(result, MAX)
        MIN = min(result, MIN)

    for i in range(len(operators)):
        if operators[i] > 0:
            if i == 0:
                operators[i] -= 1
                sol(s+1, result + numbers[s+1])
                operators[i] += 1
            elif i == 1:
                operators[i] -= 1
                sol(s+1, result - numbers[s+1])
                operators[i] += 1
            elif i == 2:
                operators[i] -= 1
                sol(s+1, result * numbers[s+1])
                operators[i] += 1
            elif i == 3 and numbers[s+1]:
                operators[i] -= 1
                if result > 0 and numbers[s+1] > 0:
                    sol(s+1, result // numbers[s+1])
                else:
                    sol(s+1, -(-result // numbers[s+1]))
                operators[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
MAX = -0x7fffffff
MIN = 0x7fffffff

sol(0, numbers[0])
print(MAX)
print(MIN)