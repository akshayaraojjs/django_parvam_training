from collections import deque

dq = deque()
# dq is an object of deque predefined class

dq.appendleft(5)
dq.append(10)
dq.appendleft(15)
dq.append(20)

print(dq)

dq.popleft()
dq.pop()

print(dq)
# rotate will take the element from last index and bring it first index and append the remaining items
# Rotate with positive number: Clockwise
# Rotate with negative number: Anti-Clockwise
dq.rotate(1)
print("After Rotate 1:", dq)

dq.rotate(2)
print("After Rotate 2:",dq)

dq.rotate(3)
print("After Rotate 3:",dq)

dq.rotate(-1)
print("Rotate 1 in negative index:", dq)

dq.rotate(-2)
print("Rotate 2 in negative index:", dq)

dq.rotate(-3)
print("Rotate 3 in negative index:", dq)

# Initializing the object along with the initial value using constructor
word = "Python"
# Passing the value usin constructor will modify the word to group of split letters
deq = deque(word)

print(deq)

# value passed via append method is taken as string or word itself
deq.append("django")
print("After appending:",deq)

deq.extend("Django")
print("After extending:",deq)