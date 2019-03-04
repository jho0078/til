
# a, b = map(int, input().split())
a = 3
b = 999

# 제곱했을 때 최대범위(b)가 넘어가는 순간의 값(i) 찾기
# 이 값 이하의 소수들의 배수들을 제거하면 소수만 남는다.
def square(b):
    for i in range(320):
        if i**2 > b:
            return i

# 위 함수에서 구한 값(i) 이하의 모든 소수들을 구한다
def decimal_for_division(i):
    numbers = list(range(2, i))
    result = []

    while True:
        ing = []
        num = numbers.pop(0)
        result.append(num)
        if numbers:
            for j in range(len(numbers)):
                if numbers[j]%num:
                    ing.append(numbers[j])
            numbers = ing[:]
        else:
            return result

i = square(b)
decimal_list = decimal_for_division(i)

print(i)
print(decimal_list)

# 1은 소수가 아니므로 범위에 있다면 제거
# 입력 범위의 모든 수를 가진 리스트 생성
if a == 1:
    numbers = list(range(2, b+1))
else:
    numbers = list(range(a, b+1))

# 소수리스트에서 하나씩 뽑아서 소수의 배수들을 계속해서 제거해 나간다.
while decimal_list:
    num = decimal_list.pop(0)
    ing = []
    for j in range(len(numbers)):

        if numbers[j] == num or numbers[j]%num:
            ing.append(numbers[j])
    numbers = ing[:]

print(numbers)
print(len(numbers))
print(min(numbers)+max(numbers))



