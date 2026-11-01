# Variables



# Declare a variable
my_name = "Manoj"
print(my_name)



# Updated variable
val = "John"
val = 45
print(val)



# Data type of variable with type() function
my_name = "Manoj"
my_age = 45
print(type(my_name))



# Variables are case-sensitive
my_name = "Manoj"
My_name = "Manoj"
print(my_name)
print(My_name)



# Updating data type in variable
myAge = 100
print(myAge)
myAge = 400
print(myAge)



# Variable naming
# Use a-z, A-Z, 0-9, _
# Keywords cannot be variable name
# Cannot start with a number
# Variables are case sensitive
n = 10
N = 100
N9 = 9
n9 = 9



# Variable techniques for variables with multiple names
# camel case
myFirstName = "Manoj"


# Variable techniques for variables with multiple names
# pascal case
MyMiddleName = "Kumar"


# Variable techniques for variables with multiple names
# snake case
my_last_name = "Gupta"



# Many values to multiple variables
x, y, z = 10, 20, 30
print(x, y, x)
print("------------")
print(x)
print(y)
print(z)


# One value to multiple variables
x = y = z = 100
print(x, y, x)
print("------------")
print(x)
print(y)
print(z)



# Assigning same value to variable
color1 = color2 = color3 = "Red"
print(color1, color2,color3)



# Assigning different values
task1, task2, task3 = 10, 20, 30
print(task1, task2, task3)



# Variable assignment and reassignment
x  = 5
print(x)
print(type(x))

y = x
print(y)
print(x is y)  # True
print(id(x))
print(id(y))

x = "Python"
print(x)
print(y)

y = "Java"
print(y)
print(x)




# Variable reassignment
x = 1
y = x
y = y + 1

print(x)
print(y)



# Deleting a variable
students_count = 10
del students_count
print(students_count)



# Swapping two variables using multiple assignment
a, b = 5, 10
a, b = b, a
print(a, b)



# Swapping two variables using temp variable
# +++++++++++++++++++++++++++++++++++
a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)



# Globa variable -- can be used anywhere
fName = "Manoj"

def myFunc():
    print("My name is " + fName)

myFunc()
print(fName)



# Local variable -- used inside function only
fName = "Manoj"

def myFunc():
    fName = "Kumar"
    print("My name is " + fName)

myFunc()
print(fName)



# Function scope creates local variable
def myFunc():
    fLang = "Java"
    print(fLang)

myFunc()
print(fLang) # error




# Making local variable to global variable
def myFunc():
    global fLang
    fLang = "Java"
    print(fLang)

myFunc()
print(fLang)



# Overriding global variable with local
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()
print("Python is " + x)



# Unpacking collections
fruits = ["apple", "mango", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)



# Camel case
myFirstName = "Manoj"
print(myFirstName)



# Pascal Case
MyVariableName = "Manoj"
print(MyVariableName)

