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
print("{:.2%}".format(percentage))


# Formatting using format() function
# Placeholders replaces with values passed to .format() function
name = "Manoj"
age = 35
print("My name is {} and I am {} years old.".format(name, age))


# Formatting using format() function
# Specify the position using indexes
print("My name is {0} and I am {1} years old.".format("Manoj", 40))


# Formating using variable names
print("Name: {name}, Age: {age}".format(name="Manoj", age=30))


# Formatting Alignment and Spacing
print("{:<10}".format("Python"))  # Left aligned
print("{:>10}".format("Python"))  # Right aligned
print("{:^10}".format("Python"))  # Center aligned


# Built-in format() function without a string
price = 26.8765
print(format(price, ".2f"))


# Decimal integer format
num = 25
print("{:d}".format(num))


# Thousand separator
num1 = 1000000
num2 = 234876345
print("{:,}".format(num1))
print("{:,}".format(num2))


# Format percentage ---- :%
# Multiplies a decimal number by 100 and adds %
num = 0.75
print("{:%}".format(num))



# Format percentage ---- :.2% 
# Percentage with 2 decimal places
# Displays a percentage with exactly two digits after the decimal point.
num = 0.75678
print("{:.2%}".format(num))


# Formatting 0.75%
num = 0.75
print("{}%". format(num))


# Solve practical coding challenges
# First try yourself.
# Spend Maximum 5 minutes on each challenge.
# Use ChatGPT if you cannot solve it yourself.
# Understand the cproblem and solution.
# Coding is all about practice and learning.


# ======================================
# Section 1: Basic Python programs

# 1. Personal profile: Create variables for your name, age, height, weight and city. Display all details in a single sentence using an f-string.

# 2. Simple greeting: Ask the user for their first name and last name. Display a personalized welcome message.

# 3. Student information: Ask for student name, roll number, class and school name. Print a neatly formatted student information card.

# 4. Simple addition: Ask the user to enter two numbers and display their addition, subtraction, multiplication and division.

# 5. Employee details: Create variables for employee ID, name, department, salary and employment status. Display all details using print().


# ======================================
# Section 2: Input and mathematical calculations

# 6. Age calculator: Ask for the user's birth year and calculate their approximate age using 2026.

# 7. Rectangle calculator: Ask for length and width. Calculate area and perimeter.

# 8. Circle calculator: Ask for the radius. Calculate the area and circumference. Use π=3.14159

# 9. Temperature converter: Ask for temperature in Celsius and convert it to Fahrenheit.

# 10. Average calculator: Ask for five subject marks. Calculate total, average and percentage.


# ======================================
# Section 3: Real-world practical programs

# 11. Shopping bill: Ask for product name, price and quantity. Calculate the total bill and display it with two decimal places.

# 12. Salary calculator: Ask for basic salary, allowance and bonus. Calculate gross salary and display it with comma separators.

# 13. Restaurant bill: Ask for food cost, service charge percentage and tax percentage. Calculate the final bill.

# 14. Fuel expense calculator: Ask for distance travelled, fuel efficiency (km per litre) and fuel price per litre. Calculate the fuel required and total fuel cost.

# 15. Electricity bill: Ask for electricity units consumed and price per unit. Calculate the total electricity bill.


# ======================================
# Section 4: Python string and number formatting

# 16. Employee salary slip: Display employee name, ID, basic salary and total salary in a properly aligned salary slip.

# 17. Percentage formatter: Ask for marks obtained and maximum marks. Calculate and display the percentage with two decimal places.

# 18. Number formatting: Take the number 987654321.98765 and display it with:

    # Two decimal places
    # Three decimal places
    # Thousands separators

    # Thousands separators and two decimal places

# 19. Currency formatter: Ask for product price and quantity. Display the total as a currency amount with two decimal places.

# 20. Number system converter: Create a variable containing 100. Display it in decimal, binary, octal and hexadecimal formats using format().

