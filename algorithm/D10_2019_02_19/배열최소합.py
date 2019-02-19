def process_solution(a, k):
    sum = []
    for i in range(1, k+1):
        for j in range()
            sumlist.append

def make_candidates(a, k, input, c):

    # in_perm 리스트를 False로 채운다
    in_perm = [False] * NMAX

    # 이미 사용한 값을 in_perm 리스트에 True로 표시한다
    for i in range(1, k):
        in_perm[a[i]] = True

    # 사용하지 않은 값(False)의 인덱스정보를 후보(c 리스트)에 집어넣는다
    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):

    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)






import sys
sys.stdin = open("배열최소합_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    datas = [list(map(int, input().split())) for _ in range(N)]

    MAXCANDIDATES = 100
    NMAX = 100
    data = [0] * (N+1)
    for i in range(N+1):
        data[i] = i
    a = [0] * NMAX
    backtrack(a, 0, 3)



























