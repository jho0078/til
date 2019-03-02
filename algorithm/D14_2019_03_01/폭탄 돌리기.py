import sys
sys.stdin = open("폭탄 돌리기.txt")

remain = 210
K = int(input())
N = int(input())

for i in range(N):
    time, quiz = input().split()
    remain -= int(time)
    if remain < 0:
        lastperson = K
        break
    if quiz == "T":
        if K == 8:
            K = 1
        else:
            K += 1

if remain >=0:
    lastperson = K

print(lastperson)