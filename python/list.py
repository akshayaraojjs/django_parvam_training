vegetables = ["Carrot", "Beetroot", "Potato", "Onion"]
print(vegetables)
print(type(vegetables))

# append method is used to add the new item to the end of the list 
vegetables.append("Tomato")
print(vegetables)

# insert method can be used to add the new value to to the desired index
vegetables.insert(2, "Cucumber")
print(vegetables)

# remove method can be used to remove the item from the list
vegetables.remove("Onion")
print(vegetables)

# pop method can be used to remove the item from the list based on the index
vegetables.pop(3)
print(vegetables)

# index method is used to find the index of the current item
print(vegetables.index("Cucumber"))

# count method is used to count all the matching items
vegetables = ["Carrot", "Beetroot", "Onion", "Potato", "Onion", "Onion"]
print(vegetables.count("Onion"))

# sort method is used to sort the items from Ascending to Descending Order
vegetables.sort()
print(vegetables)

# reverse method is used to reverse the order of the list items(not sorting)
vegetables = ["Carrot", "Beetroot", "Onion", "Potato", "Onion", "Onion"]
vegetables.reverse()
print(vegetables)

# copy method is used to copy the list items to another list
basket = vegetables.copy()
print(basket)
basket.append("Cauliflower")
print("----------------------------------------------------------")
print(vegetables)
print(basket)

# clear method is used to remove all the items from the list
vegetables.clear()
print(vegetables)

# Tuples
vowels = ("A", "E", "I", "O", "U", "A", "e", "I", "o", "u")
print(vowels)
print(type(vowels))

# count method is used to count all the matching items
print(vowels.count("A"))

print(vowels.index("u"))