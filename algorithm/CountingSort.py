def counting_sort(A, B, C)
    for i in range(len(A)):  # counting
        C[A[i]] += 1

    for i in range(1, len(C)):  #
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1



A = [1,4,5,1,2,4,5,7,9,3]
B = [0]*len(A)
C = [0]*10                      # 숫자의 갯수를 counting해서 넣을 리스트
counting_sort(A, B, C)
print(B)
