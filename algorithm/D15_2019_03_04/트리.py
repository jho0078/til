def enq(n):
    global last
    last += 1 # 마지막 노드 번호 증가
    c = last  # 마지막 노드를 자식 노드로
    p = c//2  # 부모 노드 계산
    q[last] = n
    while c>1 and q[p] > q[c]:
        q[c], q[p] = q[p], q[c]
        c = p
        p = p//2