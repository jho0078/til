SIZE = 4
Q = [0]*SIZE
front, rear = 0, 0

def isFull():
    global rear
    return (rear+1) % len(Q) == front

def isEmpty():
    global front, rear
    return front == rear

def enQueue(n):
    global rear
    if isFull():
        print("Queue is Full")
    else:
        rear = (rear+1) % len(Q)
        Q[rear] = n

def deQueue():
    global front
    if isEmpty():
        print("Queue is Empty")
    else:
        front = (front+1) % len(Q)
        return Q[front]



enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())