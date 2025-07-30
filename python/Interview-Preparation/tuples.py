# Tuple characteristics: ordered, immutable (cannot modify) and allows duplicate values
# Represented using '()'
number_tuple = (1, 4, 6, 8, 10, 6, 9) # ordered
print(number_tuple)
print("Size of Tuple:",len(number_tuple))
print("Type of Data:", type(number_tuple))

# Starting index of tuple: 0
# Access the values using the index number
print(number_tuple[2])

name_tuple = ("Akshay") # string
another_tuple = ("Akshay",) # intializing tuple with a single value is succeeded by ','
print(name_tuple)
print(type(name_tuple))
print(another_tuple)
print(type(another_tuple))

# Tuple can be used to store different kind of data
mix_tuple = ("Akshay", "Rao", 24, "ParvaM", "Technical Trainer", ["Django", "Python", "PHP"])
print(mix_tuple)
print(type(mix_tuple))
print(mix_tuple[-6]) # We can alos use negative indexing

update_tuple = list(mix_tuple) # Casting or Converting the tuple to list
# list() method can be used to convert the data into list
print(update_tuple)
print(type(update_tuple))

update_tuple.append("Bengaluru")
print(update_tuple)

mix_tuple = tuple(update_tuple)
print(mix_tuple)

new_tuple = (2, 4, 8, 10) # cannot modify as a tuple
indexOf8 = new_tuple.index(8)
print("8 is present at ", indexOf8, "position")

# So we need to convert the tuple to list and update data and again convert back to tuple
new_list = list(new_tuple) # tuple -> list
print(new_list, type(new_list))
new_list.insert(2, 6) # modified / updated the list
new_list.remove(8)
print(new_list) # check whether the changes are done
new_tuple = tuple(new_list) # converting back from list to tuple
print(new_tuple, type(new_tuple)) 


myDetails = ("Akshay", "Rao", 24, "ParvaM", "Technical Trainer", ["Django", "Python", "PHP"])

additionalDetails = ("Bengaluru", "Male", "RRIT", "B.E")

completeDetails = myDetails + additionalDetails # combining 2 tuples and making new tuple

print("My Complete Details:", completeDetails)
print("Printing my details using for in loop:")
for item in myDetails:
    print(item)
    
print("Printing my details using for in range:")
for i in range(len(myDetails)):
    print(myDetails[i])
    
print("Printing my details using while loop:")
j = 0
while j < len(myDetails):
    print(mix_tuple[j])
    j+=1 # incrementing
    
tuple1 = (2, 4, 6, 8, 10)
tuple2 = tuple1 * 3 # repeat all items for number of times given
print(tuple2)