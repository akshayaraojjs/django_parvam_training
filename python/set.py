multiples = {3, 6, 9, 12, 15}
print(multiples)
print(type(multiples))

multiples.add(18)
print(multiples)

# multiples.update(21, 24) # It will throw error
multiples.update([21, 24]) # updating the values using list
multiples.update((27, 30)) # updating the values using tuple
print(multiples)

# remove method is used to remove the item specified
multiples.remove(24)
# multiples.remove(22) 
# trying to remove the item which is not present in the set throws error 
print(multiples)

# discard method removes the item specified, if not found no error occurs
multiples.discard(27) 
multiples.discard(28)
print(multiples) 

# pop method is used to remove the first item of the set
multiples.pop()
multiples.pop()
print(multiples)

# copy method is used to copy the items from one set to another
multiples_of_3 = multiples.copy()
print(multiples_of_3)

# union method is used to combine the elements of both the sets
multiples2 = {2, 4, 6, 8, 10}
multiples3 = {3, 6, 9, 12, 15}
print(multiples2.union(multiples3))

# intersection method is used to get the common elements from both the sets
print(multiples2.intersection(multiples3))

# difference method is used to get the unique elements from either of the sets
print(multiples2.difference(multiples3)) # shows the unique items of set1
print(multiples3.difference(multiples2)) # shows the unique items of set2

# symmetric_difference method is used to get the unique elements from both of the sets
print(multiples2.symmetric_difference(multiples3)) # shows the unique items from both sets

# issubset method is used to check if all the elements of the given set is present in another set
set1 = {2, 4, 6}
set2 = {4, 6}
set3 = {4, 6, 8}

print(set2.issubset(set1))
print(set3.issubset(set1))

# issuperset method is used to check if all the elements of another set is present in current set
set1 = {2, 4, 6}
set2 = {4, 6}
set3 = {4, 6, 8}

print(set1.issuperset(set2))
print(set3.issuperset(set1))
