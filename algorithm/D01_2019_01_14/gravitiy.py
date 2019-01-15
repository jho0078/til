data = [7,4,2,0,0,6,0,7,0]
result = 0
maxHeight = 0
for i in range(len(data)):
    #i의 최대 낙차 값은 len(data) - (i+1)
    #i이후의 모든 행을 검사한다.
    maxHeight = len(data) - (i+1)
    for j in range(i+1, len(data), 1):
        if data[i] <= data[j]:
            maxHeight -= 1
    if result < maxHeight:
        result = maxHeight