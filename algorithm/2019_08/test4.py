def sol():
    time = 0
    message_number = 0
    while time < 20:

        count = 0
        for i in range(c):
            if not data[i][0]:
                if message_number < len(t):
                    data[i][0] += t[message_number] - 1
                    message_number += 1
                else:
                    count += 1
            else:
                data[i][0] -= 1
        if count == c:
            return time

        time += 1
        print(time)
        print(data)

m, c = map(int, input().strip().split(' '))
t = [int(input()) for i in range(m)]
print(t)

data = [[0] for _ in range(c)]
print(sol())

