# Resolving the Customer Queue
# FIFO - First In First Out (Following the order)
class CustomerService:
    def __init__(self):
        self.queue = []
        
    def add_customer(self, name):
        self.queue.append(name)
        print(f"{name} joined the queue.")
        
    def resolve_issue(self):
        if self.queue:
            name = self.queue.pop(0)
            print(f"Resolved the issue for {name}")
        else:
            print("Issue Resolved! No customer found in the queue.")
          
queue1 = CustomerService()

queue1.add_customer("Akshay")
queue1.add_customer("Ajay")
queue1.add_customer("Akash")
queue1.add_customer("Adarsh")
queue1.add_customer("Avinash")
queue1.resolve_issue()
queue1.resolve_issue()
queue1.resolve_issue()
queue1.resolve_issue()
queue1.resolve_issue()
queue1.resolve_issue()