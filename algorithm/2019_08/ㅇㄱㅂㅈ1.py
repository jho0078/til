def solution(goods, boxes):
    goods.sort(reverse=True)
    boxes.sort(reverse=True)
    print(goods)
    print(boxes)
    answer = 0
    j = 0
    for i in range(len(goods)):
        if boxes[i] >= goods[i]:
            answer += 1
            j += 1

    return answer

goods = [1,2]
boxes = [2,3,1]
print(solution(goods, boxes))