# Bubble 정렬
a = [5,3,1,4,2]
n = len(a)

for i in range(n-1):
    now = a[i]
    for j in range(i+1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)

# 2차 정렬
# a:총점, b:국어점수
a = [5,3,1,4,3,2,3]
b = [1,2,3,9,1,5,10]
n = len(a)

for i in range(n-1):
    now = a[i]
    for j in range(i+1, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]
        if a[i] == a[j] and b[i] < b[j]:
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]

print(a)
print(b)