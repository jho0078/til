N = int(input())
data = list(map(int, input().split()))
data.sort()
print(str(data[N//2]))