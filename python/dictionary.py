car = {
    "brand": "Tata",
    "model": "Curvv",
    "launch_year": 2024,
    "variants": ["Petrol", "Diesel", "EV"],
    "features": ("A/C", "360deg Camera", "ABS", "4 Airbags"),
    "price": "10L + GST"
}
print(car)
print(type(car))

# get(key) method is used to get the value using key
print(car.get("brand"))
print(car.get("model"))

# keys method is used to list out all the keys used in dictionary
print(car.keys()) # default method will print all the keys within dict_keys()
print(list(car.keys())) # specified to print the keys as a list
print(tuple(car.keys())) # specified to print the keys as a tuple

# values method is used to list out all the values used in dictionary
print(car.values()) # default method will print all the values within dict_values()
print(list(car.values())) # specified to print the values as a list
print(tuple(car.values())) # specified to print the values as a tuple

# items method is used to get the key value pairs
print(car.items()) 

car.update({
    "colors": ["red", "blue", "black"],
    "country_of_origin": "India"
})
print(car)

# pop(key) method is used to remove the item using key
car.pop("launch_year")
print(car)

# popitem method is used to remove the last key value pair of the dict
car.popitem()
print(car)

# copy method is used to copy all the key value pairs to another dict
new_car = car.copy()
print(new_car)
print("------------------------------------------------------")
new_car.popitem()
print(new_car)
print(car)

# clear method is used to remove all the key value pairs of the dict
car.clear()
print(car)