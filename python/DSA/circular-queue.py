class CircularQueue:
    def __init__(self, cqSize):
        self.size = cqSize
        self.queue = [None]*cqSize
        self.front = self.rear = -1
        
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full!")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            
    def dequeue(self):
        