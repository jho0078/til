import sys
sys.stdin = open("나는 학급회장이다.txt")

N = int(input())

data = [list(map(int, input().split())) for i in range(N)]
score = list(zip(*data))

sandc = [[sum(score[i]), score[i].count(3), score[i].count(2)] for i in range(3)]
print(sandc)

max_sandc = max(sandc)
if sandc.count(max_sandc) == 1:
    print(sandc.index(max_sandc)+1, max_sandc[0])
else:
    print("0", max_sandc[0])