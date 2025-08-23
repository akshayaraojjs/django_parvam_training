# Double Ended Queue (deque)
# We will use the predefined deque class

# How Normal Queue works?
# Add item from rear end and remove item from front end
# Class need not to be declared, as we already have by default
from collections import deque

dq = deque() # dq object is an instance of deque class (predefined class)

new_list = [2, 4, 6, 8]
# Appending from front end
dq.append(20)
dq.append(30)
# Appending from rear end
dq.appendleft(40)
dq.appendleft(50)

dq.pop()
dq.popleft()

dq.extend(new_list)
dq.extendleft(new_list)

# Rear End : [50, 40, 30, 20] : Front End 

print("Deque contains:", dq)