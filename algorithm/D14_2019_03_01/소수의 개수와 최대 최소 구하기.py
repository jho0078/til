
# a, b = map(int, input().split())
a = 3
b = 999

def square(b):
    for i in range(320):
        if i**2 > b:
            return i

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

# print(decimal_for_division(100))

i = square(b)
decimal_list = decimal_for_division(i)

print(i)
print(decimal_list)
if a == 1:
    numbers = list(range(2, b+1))
else:
    numbers = list(range(a, b+1))
    
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



