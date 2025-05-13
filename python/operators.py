# Arithmetic Operators
num1 = 5
num2 = 10
print("Sum: ", num1 + num2)
print("Difference: ",num1 - num2)
print("Product: ",num1 * num2)
print("Quotient: ",num1 / num2)
print("Remainder/Modulus: ",num1 % num2)
print("Exponent: ",num1 ** 3)
print("Normal Division: ",num2 / 3)
print("Floor Division: ",num2 // 3)

# Relational Operators
print(num1 > num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2)

num3 = "10"
print(num2 == num3)

# Assignment Operators
num1+=5     # num1 = num1 + 5
print(num1)
num1-=5
print(num1)
num1*=5
print(num1)
num1/=5
print(num1)
num1%=5
print(num1)
num1**=5
print(num1)
num1//=5
print(num1)

# Logical Operators
num1 = 5
print(num1)
print(num1 > 2 and num1 < 6)
print(num1 > 2 or num1 < 6)
print(not(num1 > 2 or num1 < 6))

# Identity Operators
list1 = [2, 4, 6, 8, 10]
list2 = [2, 4, 6, 8, 10]
list3 = list1
print("-------")
print(list1 is list2)
print(list1 is list3)
print(list1 is not list2)
print(list1 == list2)

# Membership Operators
print("-------")
print(6 in list1)
print(5 in list2)
print(5 not in list2)