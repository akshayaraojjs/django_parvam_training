# Dictionary Characteristics: Ordered, Mutable, Do not allow duplicate Values
# Dictionary is Represented using Key-Value pairs
ParvaM = {
    "Founder & Managing Director" : "Dr. Naveen M",
    "Co-Founder & CTO" : "Mohith Santhosh",
    "Co-Founder & CEO" : "Mohammed Habeeb",
    "HR & BDM" : "Monica R A",
    "Technical Trainers" : ["Akshay Rao", "Murthy"],
    "Founded Year": 2018,
    "Verticals": {"ERP", "CRM", "Training & Placement", "Internships", "Technical Workshops"}
}

print(ParvaM)
print(type(ParvaM))

print("ParvaM's Business includes':",ParvaM["Verticals"], "ParvaM was found in the year: ", ParvaM["Founded Year"])

# keys method is used to get all the keys present in the dictionary
print("Keys of ParvaM Dictionary:",ParvaM.keys())

# values method is used to get all the values present in the dictionary
print("Values of ParvaM Dictionary:",ParvaM.values())

# items method is used to get all the key-value pairs in the form of tuple within the list
# [(key1,value1),(key2,value2)]
print("Values of ParvaM Dictionary:",ParvaM.items())

# check whether the key is present in the current dictionary or not
if "Location" in ParvaM:
    print("Location Found")
else:
    print("Location not found")
    
# Update the new key value pair
# dictionary["key"] = "value"
ParvaM["Location"] = "Chikkabanavara"

print(ParvaM)

# update is used for both adding the new key-value pair or update the existing key-value pair
# Update: dictionary.update({"key":"value"})
# We can add or update multiple key-value pairs together
ParvaM.update({"Location": "Chikkabanavar, Bengaluru", "No. of Branches":2})
print("ParvaM Updated Information:",ParvaM)

# pop method is used to remove the key-value pair from the dictionary
# dictionary.pop("key")
# If we try to remove the unknown key, it throws the error: 'KeyError'
ParvaM.pop("Technical Trainers")
print("ParvaM after removal:", ParvaM)

ParvaM.popitem()
print("ParvaM after Pop-item:", ParvaM)

new_dict = {
    "even": [2, 4, 6, 8], # list
    "odd": {1, 3, 5, 7}, # set
    "prime": (2, 3, 5, 7, 11, 13, 17),
    "complex": "2i + 3"
}

print(new_dict)
new_dict.update({"Sum of even":20, "Sum of odd":16})
print(new_dict)
# popitem method is used to remove the last added key-value pair - No arguments
new_dict.popitem()
print(new_dict)