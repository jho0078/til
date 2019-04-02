def powerset(s, n):

    if s == n:
        w1 = sum(t)
        w2 = abs(allchu - 2*w1)
        if w1 not in myweight:
            myweight.append(w1)
        if w2 not in myweight:
            myweight.append(w2)
        return

    t[s] = chu[s]
    powerset(s+1, n)
    t[s] = 0
    powerset(s+1, n)

N = int(input())
chu = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

allchu = sum(chu)
t = [0]*N
myweight = []
powerset(0, N)
print(myweight)
for i in range(len(weight)):
    flag = 0
    for j in range(len(myweight)):
        if weight[i] == myweight[j]:
            flag = 1
            print("Y", end=" ")
            break
    if flag == 0:
        print("N", end=" ")