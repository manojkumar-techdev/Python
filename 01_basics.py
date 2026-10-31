# Let's start learning Python.


# Firts Program
print("Hello World!")


# Output in Python
print("This is output")


# Input in Python
name = input("Enter your name: ")
print("Hello " + name + "! Welcome to Python programming.")


# Printing a String
my_name = "Manoj"
print(my_name)


# Printing a Number
my_age = 34
print(my_age)


# Printing a Float
my_height = 5.9
print(my_height)


# Printing a Boolean
is_student =  True
print(is_student)


# Single line Comments in Python
print("Hello") # This is a comment


# Multi-line comment
# Take two numbers
# Add them
# Print the result
num1 = 10
num2 = 20   
print(num1 + num2)


# Single Statement
print("This is a single statement")


# Multi Statement
print("Statement 1")
print("Statement 2")
print("Statement 3")


# Semicolon in Python is optional
print("Hello"); 


# Printing without a new line
message1 = "Hello"
message2 = "World"
print(message1, end=" ")
print(message2)


# Printing with separator
message1 = "Hello"
message2 = "World"  
print(message1, message2, sep="-")


# Mathematical Operations inside print() finction
print("Addition: ", 10 + 5)


# Printing Text and Number Together - method 1
my_name = "Manoj"
my_age = 34
print("My name is " + my_name + " and I am " + str(my_age) + " years old.")


# Printing Text and Number Together - method 2
my_name = "Manoj"
my_age = 34
print("My name is " + my_name,"and I am", my_age, "years old.")


# Output single variable
my_name = "Manoj"
print(my_name)


# output multiple variables in multiple lines
my_name = "Manoj"
my_age = 34
print(my_name)
print(my_age)


# output multiple variables in a single line
my_name = "Manoj"
my_age = 34 
print(my_name, my_age)


# Comma notation for multiple variables
my_name = "Manoj"
my_age = 34
my_height = 5.9
my_weight = 70
my_city = "New York"
print(my_name, my_age, my_height, my_weight, my_city)



# Python version installed on system
import sys
print("Python version")
print (sys.version)


# Coomand prompt in Python
# Open Terminal --> type "py & press Enter"
# exit() ---- To exit from Python command prompt



# Indentation to indicate a block code
if 5 > 2:
    print("Five is greater than two!")



# Number of spaces / tab depend on programmer 
if 5 > 2:
    print("Five is greater than two!")
if  5  < 2:
        print("Five is less than two!")



# Use the same number of spaces in the same block of code 
# Otherwise Python will give you an error
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")



# Python formatting 
# Arranging Text, Numbers and Output in a clean and readable way
# Using print() function
name = "Manoj"
age = 35
print("My name is :", name)
print("My age is :", age)



# Formatting using f-string
name = "Manoj"
age = 45
print(f"My name is {name}")
print(f"I am {age} years old.")



# Calculating inside f-string
num1 = 10
num2 = 20
print(f"Total = {num1 + num2}")


# Formating numbers ---- control dceimal places
price = 26.8765
print(f"Price: {price:.2f}") # keeps 2 decimals
print(f"Price: {price:.3f}") # keeps 3 decimals
print(f"Price: {price:.4f}") # keeps 4 decimals


# Formating percentages
percentage = 0.85
print(f"Succes rat: {percentage:.2%}")


# Formatting using format() function
# Placeholders replaces with values passed to .format() function
name = "Manoj"
age = 35
print("My name is {} and I am {} years old.".format(name, age))


# Formatting using format() function
# Specify the position using indexes
print("My name is {0} and I am {1} years old.".format("Manoj", 40))


