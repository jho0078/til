import sys
sys.stdin = open("글자수_input.txt")
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    alpha_str1 = list(set(list(str1)))
    dic = {}
    for i in range(len(str2)):
        if str2[i] not in dic:
            if str2[i] in alpha_str1:
                dic[str2[i]] = str2.count(str2[i])
    max = 0
    for val in dic.values():
        if val > max:
            max = val

    print("#{} {}".format(tc, max))

