T = int(input())
for tc in range(1, T+1):
    print("#{} ".format(tc) + str(max(map(int, input().split()))))