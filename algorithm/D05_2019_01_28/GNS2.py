import sys
sys.stdin = open("GNS_input.txt")
T = int(input())
for tc in range(1, T+1):
    temp = input()  #dummy
    data = list(map(str, input().split()))
    number = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}

    for i in range(len(data)):
        for k in number:
            if data[i] == k:
                number[k] += 1
    result = [key for key, value in number.items() for j in range(value)]

    print("#{} {}".format(tc, " ".join(result)))

