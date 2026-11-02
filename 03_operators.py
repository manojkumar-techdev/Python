# Arithmetic Operators


# Addition
price1 = 100
price2 = 30
addition_cal = price1 + price2 
print(addition_cal)


# Subtraction
price1 = 100
price2 = 30
subtraction_cal = price1 - price2 
print(subtraction_cal)


# Multiplication
price1 = 100
price2 = 30
multiplication_cal = price1 * price2 
print(multiplication_cal)


# Division gives quotient as a float value
price1 = 100
price2 = 30
division_cal = price1 / price2 
print(division_cal)


# Modulus gives remainder
price1 = 100
price2 = 30
modulus_cal = price1 % price2 
print(modulus_cal)


# Floor Division
price1 = 100
price2 = 30
floor_division_cal = price1 // price2 
print(floor_division_cal)


# Exponentiation
price1 = 10
price2 = 3
exponentiation_cal = price1 ** price2 
print(exponentiation_cal)


# Assignment Operators


# Equal to Assignment Operator
Age1 = 20
print(Age1)


# Addition Assignment Operator
Age1 = 20
Age1 += 5
print(Age1)


# Subtraction Assignment Operator
Age1 = 20
Age1 -= 5
print(Age1)


# Multiplication Assignment Operator
Age1 = 20
Age1 *= 5
print(Age1)


# Division Assignment Operator
Age1 = 20
Age1 /= 5
print(Age1)


# Modulus Assignment Operator
Age1 = 20
Age1 %= 5
print(Age1)


# Floor Division Assignment Operator
Age1 = 20
Age1 //= 5
print(Age1)


# Exponentiation Assignment Operator
Age1 = 20
Age1 **= 5
print(Age1)


# Bitwise AND Assignment Operators
Age1 = 20
Age1 &= 5
print(Age1)


# Bitwise OR Assignment Operators
Age1 = 20
Age1 |= 5
print(Age1)


# Bitwise XOR Assignment Operators
Age1 = 20
Age1 ^= 5
print(Age1)


# Right Shift Assignment Operators
Age1 = 20
Age1 >>= 5
print(Age1)


# Left Shift Assignment Operators
Age1 = 20
Age1 <<= 5
print(Age1)


# Matrix Multiplication Assignment Operators
import numpy as np

x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]])

x @= y

print(x)


# Walrus Operator
# := is an assignment expression
print(x := 10)


# Walrus Operator
# := is an assignment expression
if (length := len("Python")) > 5:
    print(length)



# Comparison Operators


age1 = 20
age2 = 10

# Equal to
print(age1 == age2) 


# Not Equal to
print(age1 != age2)


# Greater than
print(age1 > age2)


# Less than
print(age1 < age2)


# Greater than or Equal to
print(age1 >= age2)


# Less than or Equal to
print(age1 <= age2)



# Logical Operators
# AND Operator
age1 = 20
age2 = 10

if age1 > 10 and age2 < 20:
    print("Both conditions are True")
else:
    print("One or both conditions are False")


# OR Operator
age1 = 20   
age2 = 10

if age1 > 10 or age2 < 5:
    print("At least one condition is True")
else:
    print("Both conditions are False")


# NOT Operator
age1 = 20   
age2 = 10

if (not age1 < 15):
    print("Condition is True")
else:
    print("Condition is False")


# Bitwise Operators
age1 = 20
age2 = 10

print(age1 & age2)  # Bitwise AND
print(age1 | age2)  # Bitwise OR    
print(age1 ^ age2)  # Bitwise XOR
print(~age1)        # Bitwise NOT
print(age1 << 2)  # Bitwise Left Shift
print(age1 >> 2)  # Bitwise Right Shift



# Membership Operators
# Checks whether a value exists inside a sequence or collcetion.



# IN operator (in)
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("orange" in fruits)


# NOT IN operator (not in)
fruits = ["apple", "banana", "mango"]

print("orange" not in fruits)
print("apple" not in fruits)


# Membership Operator in Strings
name = "Python Programming"

print("Python" in name)
print("Java" in name)


# Membership operators in Dictionaries
student = {
    "name": "Manoj",
    "age": 25
}

print("name" in student)
print("Manoj" in student)
print("Manoj" in student.values())



# Identiti Operators
# operators check whether two variables refer to the same object in memory


# IS operator (is)
a = [10, 20, 30]
b = a

print(a is b)


# IS NOT operator (is not)
a = [10, 20, 30]
b = [10, 20, 30]

print(a is not b)



# Although both lists contain the same values
# They are separate objects.
# Difference between == and is
a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)
print(a is b)



# Recommended Use
x = None

if x is None:
    print("No value")