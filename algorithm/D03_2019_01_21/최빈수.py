import sys
sys.stdin = open("최빈수_input.txt")
T = int(input())
for tc in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    counts = [0] * 101
    for i in range(1000):
        counts[data[i]] += 1
    max = 0
    for j in range(101):
        if counts[j] >= max:
            max = counts[j]
            max_score = j

    print("#{} {}".format(tc+1, max_score))