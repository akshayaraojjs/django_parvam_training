import heapq
# heapq follows ascending order for heappush

tasks = []

# heappush(list, (priority, anything))
heapq.heappush(tasks, (3, "Learn Dance"))
heapq.heappush(tasks, (4, "Learn Singing"))
heapq.heappush(tasks, (1, "Learn Python"))
heapq.heappush(tasks, (2, "Learn Django"))

print("List of tasks:",tasks)

# task = 0
# while task != len(tasks):
#     print(tasks[task])
#     task += 1

while tasks:
    # heappop(list)
    print("Choosing the task: ", heapq.heappop(tasks))