# To work on Priority Queue, we use heap

# Check the priority and then remove the item from the queue
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    # Task Creation
    def enqueue(self, priority, item):
        # heappush is a method of heapq class/library
        # heappush expects 2 parameters, object and its priority and the item
        heapq.heappush(self.queue, (priority, item))
        print(f"{item} task has been added to the Priority Queue with priority no: {priority}")
        
    # Task Assignment
    def dequeue(self):
        if self.queue:
            # [1] why it has been used
            return heapq.heappop(self.queue)[1]
        return "Queue is Empty!"
    
    def display(self):
        print("Priority Queue contains: ", self.queue)
        
prique = PriorityQueue() # prique is an object of PriorityQueue class
prique.enqueue(3, "Low Priority")
prique.enqueue(2, "Medium Priority")
prique.enqueue(1, "High Priority")

prique.display()

prique.dequeue()
prique.dequeue()

prique.display()