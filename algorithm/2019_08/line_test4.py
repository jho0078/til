N = int(input())
data = list(map(int, input().strip().split(' ')))

count = 0
start_flag = 0
max_count = 0

for i in range(len(data)):

    if not data[i]:
        count += 1
    else:
        if not start_flag:
            max_count = count
            start_flag = 1
        else:
            if (count+1)//2 > max_count:
                max_count = (count+1)//2
            count = 0

if count > max_count:
    max_count = count

print(max_count)
