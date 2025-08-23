# Assigning the Task for CPU (Round Robin CPU Scheduling)
class CPU:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1
        
    def list_task(self, task):
        if (self.rear + 1) % self.size == self.front:
            print("Memory is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = task
        
    def assign_task(self):
        if self.front == -1:
            return None
        task = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return task
    
cpu = CPU(5)
cpu.list_task("Run Xampp Server")
cpu.list_task("Activate Virtual Environment")
cpu.list_task("Navigate to Django Project")
cpu.list_task("Run Django Server")
cpu.list_task("Open the Django App in the Browser")
print(cpu.assign_task())
print(cpu.assign_task())
print(cpu.assign_task())
print(cpu.assign_task())
print(cpu.assign_task())