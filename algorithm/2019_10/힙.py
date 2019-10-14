# import heapq
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     heap = []
#     result = '#' + str(tc)
#     for i in range(N):
#         data = input()
#         if data == '2':
#             if heap:
#                 result += ' ' + str(heapq.heappop(heap)[1])
#             else:
#                 result += ' -1'
#
#         else:
#             num = int(data[2])
#             heapq.heappush(heap, (-num, num))
#
#         print(heap)
#
#     print(result)


from queue import PriorityQueue

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    que = PriorityQueue()
    result = '#' + str(tc)
    for i in range(N):
        data = input()
        if data == '2':
            if not que.empty():
                result += ' ' + str(que.get()[1])
            else:
                result += ' -1'

        else:
            num = int(data[2])
            que.put((-num, num))

    print(result)
