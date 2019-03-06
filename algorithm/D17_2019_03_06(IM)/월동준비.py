N = int(input())
dotori = list(map(int, input().split()))

smart_sum = 0
for i in range(N):
    if dotori[i] > 0:
        smart_sum += dotori[i]


now = 0
idiot_sum = 0
for i in range(N):
    if now + dotori[i] > 0:
        if now + dotori[i] > idiot_sum:
            idiot_sum = now + dotori[i]
        now += dotori[i]
    else:
        now = 0

if smart_sum > 0:
    print(idiot_sum, smart_sum)
else:
    print(max(dotori), max(dotori))
