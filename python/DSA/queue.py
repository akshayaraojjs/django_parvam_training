# Python List is used to create a Queue
class Queue:
    def __init__(self):
        self.queue = [] # empty list for Queue
        
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item Enqueued: {item}")
        print(f"After Enqueue - Queue Contains: {self.queue}")
        
    def dequeue(self):
        if not self.is_empty():
            # list method: pop(0) is given to remove the item from first index or first item
            return self.queue.pop(0)
        else:
            return "Queue Underflow! Cannot Remove item"
        
    def front(self):
        if not self.is_empty():
            # 0th index contains firts element
            return self.queue[0]
        else:
            return "Queue is Empty!"
        
    def rear(self):
        if not self.is_empty():
            # -1 index contains last element (Negative Indexing)
            return self.queue[-1]
        else:
            return "Queue is Empty!"
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
queue1 = Queue() # "queue1 object" is an instance of "Queue class"
queue1.enqueue(7)
queue1.enqueue(14)
queue1.enqueue(21)
queue1.enqueue(28)
queue1.enqueue(35)

print("Front element/First Item: ", queue1.front())
print("Rear element/Last Item: ", queue1.rear())
print("Dequeuing: ", queue1.dequeue())
print("Dequeuing: ", queue1.dequeue())
print("Dequeuing: ", queue1.dequeue())
print("Dequeuing: ", queue1.dequeue())
print("Dequeuing: ", queue1.dequeue())
print("Dequeuing: ", queue1.dequeue())
print("Queue Size: ", queue1.size())
print("Is Queue empty?", queue1.is_empty())