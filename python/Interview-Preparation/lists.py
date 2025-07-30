# Characteristics of List: Mutable, Ordered and Allow duplicate values
# List are represented by Square Brackets:
# Starting Index or position of the list is 0
num_of_list = [1, 2, 3, 4, 5] # list
print("List of numbers contain these values: ", num_of_list)
print(type(num_of_list)) # To check the type of the variable in this case it is list

# Append method is used to Insert the data at the end of the list, it takes only 1 argument(i.e value)
# Syntax: list_variable.append(value)
num_of_list.append(6)
num_of_list.append(7)
print("Appended List: ", num_of_list) 

# Insert method is used to Insert the data at the desired position of the list
# Syntax: list_variable.insert(position, value) - 2 arguments (position & value)
num_of_list.insert(3, 8)
num_of_list.insert(5, 10)
print("Inserted List: ", num_of_list) 

# Remove method is used to remove the specific data from the list
# Syntax: list_variable.remove(value) - 1 argument (i.e value)
num_of_list.remove(6)
num_of_list.remove(3)
print("Removed List: ", num_of_list) 

# Pop method is used to remove the data from the end of the list
# Syntax: list_variable.pop() - No argument required
num_of_list.pop()
num_of_list.pop()
print("Popped List: ", num_of_list) 

random_list = [2, 5, 3, 9, 4, 5, 8, 3]
# sort method is used to sort the data in the list in either ascending or descending order
random_list.sort()
print("Sorted List in Ascending Order: ", random_list) 
random_list.sort(reverse=True) # For Descending Order we need to pass the argument: reverse=True
print("Sorted List in Descending Order: ", random_list) 

# Index method is used to Find the position of the Desired element in the list
# Index will be shown for the first found position of the element even though it is repeated
index = random_list.index(2) # 1 argument - (value)
print("Number 2 is present at ", index)
index = random_list.index(3) # Duplicate Value will be ignored if the first item is found
print("Number 3 is present at ", index)

# count method is used to check number of times the items have been repeated
count = random_list.count(5) # 1 argument - (value)
print("5 is repeated for ", count, " times")
count = random_list.count(4)
print("4 is repeated for ", count, " time")

# Reverse method is used to change the order of the list
random_list.reverse()
print("Reversed List: ", random_list)

# Extend method is used to combine another list to the end of current list
print("Original Random list", random_list)
print("Original Number list", num_of_list)
# Syntax: list1.extend(list2) # 1 argument - (list)
random_list.extend(num_of_list)
print("Newly Extended List: ", random_list)

# Example 2: 
even_list = [2, 4, 6, 8, 10]
odd_list = [1, 3, 5, 7, 9]
combine_list = even_list.copy() # copying the even_list to combine_list
print("Combined with even list: ", combine_list)
combine_list.extend(odd_list)
print("Combine with odd list: ", combine_list)
# combine_list.append(odd_list) # If we append the list to the existing list, it will be appended as the list itself but not as an item
# print("Appended odd list: ", combine_list)

# Copy method is used to copy the items from one list to another list
copy = random_list.copy() # No arguments
print("Copied List", copy)

# Clear method is used to remove all the items from the list
copy.clear()
print("Empty List: ", copy)

# List can contain any kind of data - int, string, float
fruits_list = ["Apple", "Banana", "Chikoo", "Jackfruit"]
print(fruits_list)
fruits_list.append("Grapes")
print("New Fruit Added:",fruits_list)
float_list = [1.23, 3.45, 5.67, 8.959]
print(float_list)

# list can contain all kind of data together
mix_list = ["Akshay Rao", 24, 82.5, "ParvaM", "B.E", 3, 'J', True] # Heterogenous Property (Combination of different data)
print(mix_list)
print(type(mix_list))
print("My name is", mix_list[0]) # we can acces the item using its index number
print("I'm working at", mix_list[3]) # we can acces the item using its index number
print("My Initial is", mix_list[6], type(mix_list[6])) # we can acces the item using its index number
# print(type(mix_list[2])) # Finding the type of item present the list
# print(type(mix_list[3]))
# print(type(mix_list[5]))
# print(type(mix_list[7]))
# print(mix_list[8]) # "IndexError: list index out of range": This error can be seen when you're trying to access the value from the unknown index number / out of limit

new_list = [1, 5, 2, "Banana", True, 5.5, "Django", 6.25]
# Negative Indexing: Reverse order starts from -1 for last item
print(new_list[-2]) # Negative Indexing can be used to get the item from the reverse order
print(new_list[-4]) # Negative Indexing can be used to get the item from the reverse order

# Slicing the list to get the required items from the list without modifying the original list
print(new_list[1:4]) # starting point is inclusive and ending point is exclusive
# Syntax: list[start : end]
# start value is included, end value is excluded
print(new_list[-4: -1])

list_of_num = [1, 3, 4, 5, 7, 8, 10, 13]
# normal index 0  1  2  3  4  5   6   7
# negative    -8 -7 -6 -5 -4 -3  -2  -1
print("Original List: ", list_of_num)
# Syntax: list[start : end] start is included, end is excluded

# Slicing
print("Slicing from 0 to 3:", list_of_num[0:3]) # 0th index to 2nd index, 3rd index has been skipped
print("Slicing from 4 to 7:", list_of_num[4:7]) # 4th index to 6th index, 7th index has been skipped
print("Slicing from 2 to 5:", list_of_num[2:5]) # 2nd index to 4th index, 5th index has been skipped

# Slicing can be done only on starting or ending index:
# If only start is given: starting from start index to last index
print("Slicing from 2 to end:", list_of_num[2:]) # 2nd index to last index
print("Slicing from 4 to end:", list_of_num[4:]) # 4th index to last index

# If only end is given: starting from start index to end but 1 index
print("Slicing from 0 to 4:", list_of_num[:5]) # 0th index to 4th index, 5th index has been skipped
print("Slicing from 0 to 4:", list_of_num[:7]) # 0th index to 6th index, 7th index has been skipped

# Negative Index Slicing
# start only
print("Slicing from -8 to end: ", list_of_num[-8:]) # Starting from 0(-8) to last index
print("Slicing from -3 to end: ", list_of_num[-3:]) # Starting from 5(-3) to last index

# end only
print("Slicing from 0 to -3: ", list_of_num[:-3]) # Starting from 0 to 5(-3) index
print("Slicing from -3 to end: ", list_of_num[:-6]) # Starting from 0 to 1(-6)

# start and end
print("Slicing from -5 to -2: ", list_of_num[-5:-2]) # Starting from 3(-5) to 5(-3) index
print("Slicing from -8 to -4: ", list_of_num[-8:-4]) # Starting from 0(-8) to 4(-4) index

# Try on your phone number - All 5 types (2 examples for each)

# Step of Slicing need to be covered (Step of 2, -1 , empty slicing (:))

some_list = [1, 3, 5, 7, 9]
print(some_list) 
# Change the element using its index number
# Syntax = list[index] =  new_value
some_list[2] = 6 # 5 is replaced by 6
print(some_list)
# some_list.remove(4) # If we try to remove the item which is not present in the list, then we will get "ValueError: list.remove(x): x not in list"

some_list.clear() # clear method is used to remove all elements which returns the empty list
print(some_list)
del some_list # del keyword is used to remove the list itself
# print(some_list) # NameError will be thrown # It throws error as the list has been deleted above

# Errors
# IndexError: when the finding index is not present in the list
# ValueError: when the finding value is not present in the list
# NameError: when the variable itself is not present (Occurred commonly when del keyword is used)

name_list = ["Akshay"]
print("What type of data is name_list:",type(name_list))


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2 # combine 2 list and assign it to new list
list3.sort(reverse=True)
print(list3)