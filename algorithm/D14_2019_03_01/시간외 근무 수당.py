import sys
sys.stdin = open("시간외 근무 수당.txt")

totaltime = 0
for i in range(5):
    a, b = input().split()
    start = float(a)
    end = float(b)
    if end - start > 1.0:
        if end -start > 5.0:
            totaltime += 4.0
        else:
            totaltime += (end - start - 1)


if totaltime >= 15.0:
    money = int(totaltime*10000*0.95)
    print(money)
elif totaltime <= 5.0:
    money = int(totaltime*10000*1.05)
    print(money)
else:
    money = int(totaltime*10000)
    print(money)



