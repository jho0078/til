def solution(data):
    result = []
    time = data[0][1]
    idx = 0
    q = [data[0]]
    print("data:", data)
    while q:

        print("idx:", idx)

        n, t, p = q.pop(0)
        time += p
        result.append(n)
        for i in range(idx+1, len(data)):
            if data[i][1] <= time:
              idx += 1
              q.append(data[i])
            else:
                break
        print("q:", q)
        print("time:", time)
        q = sorted(q, key=lambda x:x[2])
        print("정렬 q:", q)

        if not q and idx+1 < len(data):
            q.append(data[idx+1])
            idx += 1

        print("result:", result)

    return result

data = [[1, 99999406, 100000], [2, 99999407, 100000], [3, 99999408, 100000], [4, 99999409, 100000], [5, 99999410, 100000], [6, 99999411, 100000], [7, 99999412, 100000], [8, 99999413, 100000], [9, 99999414, 100000], [10, 99999415, 100000], [11, 99999416, 100000], [12, 99999417, 100000]]
print(solution(data))

