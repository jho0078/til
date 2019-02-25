SIZE = 100
Q = [0]*SIZE
front, rear = -1, -1

def isFull():
    global rear
    return rear == SIZE - 1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(n):
    global rear
    if isFull():
        print("Queue is Full")
    else:
        rear += 1
        Q[rear] = n

def deQueue():
    global front
    if isEmpty():
        print("Queue is Empty")
    else:
        front += 1
        return Q[front]

def Qpeek():
    global front
    if isEmpty():
        print("Queue is Empty")
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())