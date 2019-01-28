# 숫자형식으로 이루어진 문자열을 정수의 형태로 반환하기(int함수)
def atoi(string):
    value = 0
    i = 0
    while i<len(string):
        c = string[i]
        # 아스키 코드값으로 비교(문자이기 때문에)
        if c >= "0" and c <= "9":
            # 아스키 코드로 바꿈
            digit = ord(c) - ord("0")
        else:
            break
        value = (value*10) + digit;
        i += 1
    return value

a = "123"
print(type(a))
b = atoi(a)
print(b)
print(type(b))
c = int(a)
print(type(c))