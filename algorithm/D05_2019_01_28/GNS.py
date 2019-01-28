import sys
sys.stdin = open("GNS_input.txt")
T = int(input())

for tc in range(1, T+1):
    temp = input()  #dummy
    data = list(map(str, input().split()))
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for j in range(10):
        globals()[f"count_{j}"] = 0
    for i in range(len(data)):
        for k in range(len(number)):
            if data[i] == number[k]:
                globals()[f"count_{k}"] += 1

    result = []
    for l in range(len(number)):
        for i in range(globals()[f"count_{l}"]):
            result.append(number[l])

    print("#{} {}".format(tc, " ".join(result)))

    count = [for i in range(len(data)) for k in range(len(number)) if data[i] == number[k]]