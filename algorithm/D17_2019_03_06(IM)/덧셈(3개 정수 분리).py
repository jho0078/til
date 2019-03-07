arr = "12345"
N = len(arr)

for i in range(N-2):
    A = int(arr[:i+1])
    for j in range(i+1, N-1):
        B = int(arr[i+1:j+1])
        C = int(arr[j+1:])
        print(A, B, C)