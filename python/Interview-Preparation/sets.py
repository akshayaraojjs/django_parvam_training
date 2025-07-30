# Set Characteristics: Unordered, No duplicates, Unchangeable
# Set is Represented by '{}'
set_of_numbers = {3, 6, 9, 12, 15, 6, 12} # ignore duplicate values even if it exist
print(set_of_numbers, type(set_of_numbers), len(set_of_numbers))
# print(set_of_numbers[2]) # unordered so we cannot access the set item using the index number

new_set = {0, 1, 2, 3, True, False} # True -> 1 & False -> 0
print(new_set)

# add method can be used to add new items to the existing set
# add method can only add 1 item at a time: 1 argument (value)
new_set.add(4)
print("New item added",new_set)

# remove method is used to remove the item by its value
# remove method expects 1 argument (value)
new_set.remove(3)
print("Item Removed",new_set)

set1 = {"Django", "Python", 3.5, 4.2, 5}
print("Set1 contains:",set1)
set2 = {"HTML", "CSS", "JS"}
print("Set2 contains:",set2)

# update method is used to combine another set to the existing set
set1.update(set2)
print("After updating Set1 contains:",set1)

set_tuple = ("Bootstrap", "MySQL") # tuple

set1.update(set_tuple) # updating the tuple to the set
print("After updating Set1 with tuple, new set contains:",set1, "it still remains as:", type(set1))

set_list = ["C", "C++"] # list

set1.update(set_list) # updating the list to the set
print("After updating Set1 with list, new set contains:",set1, "it still remains as:", type(set1))
# update method can be used to combine set, tuple & list also

# remove method is used to remove the item if it exist and throws error if it doesn't exist
set1.remove("C++")
# Error will be thrown if we try to remove the non-existing item from the set: 'KeyError'

# discard method will remove the item if it found, but doesn't throw error if it is not found
set1.discard("C#")
print("After removing CPP:", set1)

# pop method removes the random item from the set as it is not ordered
set1.pop() 
print("After popping:", set1)

# clear method will clear and remove all the items from the set
set1.clear()
print(set1)

set_of_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18}
set_of_3 = {3, 6, 9, 12, 15, 18}

# Union '|' is used to combine 2 sets by elemenating the duplicate values
union_set = set_of_2 | set_of_3 # method 1 (symbolic representation - |)
# union_set = set_of_2.union(set_of_3) # method 2 (using union method)
print("Union set:",union_set)

# Union '|' is used to combine 2 sets by elemenating the duplicate values
intersection_set = set_of_2 & set_of_3 # method 1 (symbolic representation - &)
# intersection_set = set_of_2.intersection(set_of_3) # method 2 (using intersection method)
print("Intersection set:",intersection_set)

# intersection method will only fetch the common items and doesn't affect original set
# intersection_update method will fetch the common items and modifies it with original set
common_set = set_of_2.intersection(set_of_3)
print("Intersection method:",common_set, "Original Set:", set_of_2)
set_of_2.intersection_update(set_of_3)
print("Intersection Update method:",set_of_2)

# difference set is used to list the uncommon item from left set
fruits_set = {"Apple", "Grapes", "Orange", "Pineapple", "Jackfruit", "Butterfruit", "Pomogranate"}
fruit_basket = {"Apple", "Strawberry", "Mango", "Orange"}

pick_fruits = fruits_set.difference(fruit_basket)
print("Fruits Set - Fruit Basket", pick_fruits)

pick_fruits = fruit_basket.difference(fruits_set)
print("Fruits Basket - Fruit Set", pick_fruits)

new_fruits = fruit_basket.difference(fruits_set)
print("New Fruits", new_fruits, "Original Basket:", fruit_basket)

# difference update method is used to list the uncommon item from left set and updates it with original set
fruit_basket.difference_update(fruits_set)
print("Original Basket:", fruit_basket)