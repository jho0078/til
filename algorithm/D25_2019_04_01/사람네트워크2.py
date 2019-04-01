import sys
sys.stdin = open("사람네트워크2_input.txt")

T = int(input())
for i in range(1, T+1):
    data = list(map(int, input().split()))
    d