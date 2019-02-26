import sys
sys.stdin = open("contact_input.txt")

def contact(v):
    queue = []
    queue.append(v)
    visited = [0] * 101
    visited[v] = 1
    result = []

    while queue:
        t = queue.pop(0)
        # print(connects[t])

        if t in connects:
            for i in connects[t]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = visited[t] + 1
                    # print(queue)
                    result.append([visited[i], i])

    return result

for tc in range(1, 11):
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    connects = {}
    for i in range(0, len(data), 2):
        if data[i] in connects:
            connects[data[i]] += [data[i+1]]
        else:
            connects[data[i]] = [data[i+1]]
            
    print("#{} {}".format(tc, sorted(contact(b))[-1][1]))

# print(f'#{tc + 1} {len(visited) - 1 - visited[::-1].index(max(visited))}')




