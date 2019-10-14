def solution(datas):
    global FLAG

    # print(datas)

    if FLAG:
        return

    now = datas[0]
    start = 0
    idx = 0
    for i in range(1, len(datas)):
        if datas[i] == now:
            idx += 1
        else:
            if idx >= 1:
                new_data = []
                for j in range(len(datas)):
                    if j < start or j > start + idx:
                        new_data.append(datas[j])
                # print("new_data", new_data)

                if not new_data:
                    FLAG = 1
                    return

                solution(new_data)
            now = datas[i]
            idx = 0
            start = i

    if idx >= 1:
        new_data = []
        for j in range(len(datas)):
            if j < start or j > start + idx:
                new_data.append(datas[j])
        # print("new_data", new_data)

        if not new_data:
            FLAG = 1
            return

        solution(new_data)

T = int(input())
for tc in range(1, T+1):
    data = list(input())
    # print(data)
    FLAG = 0
    solution(data)
    print(FLAG)