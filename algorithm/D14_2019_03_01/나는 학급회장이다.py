import sys
sys.stdin = open("나는 학급회장이다.txt")

n = int(input())
first = []
second = []
third = []
emptylist = []

for i in range(n):
    a, b, c = map(int, input().split())
    first.append(a)
    second.append(b)
    third.append(c)

max_score = max(sum(first), sum(second), sum(third))
sum_list = [sum(first), sum(second), sum(third)]

max_score = 0
for i in range(3):
    if sum_list[i] > max_score:
        max_score = sum_list[i]
        max_idx = []
        max_idx.append(i)

    elif sum_list[i] == max_score:
        max_idx.append(i)

print(max_idx, max_score)
if len(max_idx) == 1:
    print(max_idx[0] + 1, max_score)

else:
    data = [first, second, third]
    print(data)
    three_counts = -1
    for i in range(len(max_idx)):
        if data[max_idx[i]].count(3) > three_counts:
            three_counts = data[max_idx[i]].count(3)
            max_idx2 = []
            max_idx2.append(max_idx[i])

        elif data[max_idx[i]].count(3) == three_counts:
            max_idx2.append(max_idx[i])

    if len(max_idx2) == 1:
        print(max_idx2[0] + 1, max_score)

    else:
        p = 1
        two_counts = -1
        for i in range(len(max_idx2)):
            if data[max_idx2[i]].count(2) > two_counts:
                two_counts = data[max_idx2[i]].count(2)
                max_idx3 = max_idx2[i]

            elif data[max_idx2[i]].count(2) == two_counts:
                print("0", max_score)
                p = 0
                break

        if p == 1:
            print(max_idx3 + 1, max_score)






