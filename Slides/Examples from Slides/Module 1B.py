##############################
# Module 1B - Error Handling #
##############################

'''
Errors are the problems in a program due to which the program will stop the execution. 
Two types of Error occur in Python:
1) Syntax errors
2) Logical errors - runtime errors (Exceptions)
'''

# slide 5: Syntax errors
'''
age = int(input("Enter your age:"))
if age < 18  # produces syntax error as colon (:) is missing at the end of the line
    print("You are a minor")
'''

# slide 6: Exceptions
marksAchieved = 237
marksAvailable = 0
# the following statement produces ZeroDivisionError exception due to division by 0
#percentageAchieved = marksAchieved / marksAvailable * 100

'''
If you have some code that may raise an exception, you can defend your program
by placing the runtime error-prone code in a try-except-else-finally block. 
Syntax:
try:
    # some code prone to runtime errors
except:
    # executed if error in the try block
else:
    # executed if no exception
finally:
    # some code ... (always executed)

The try block tests a code for errors.
The except block handles the error.
The else block executes if code in the try block does not raise an exception
The finally block executes regardless of the result of the try and except blocks.
'''

# slide 12: try-except statement 
def divide(x, y):
    try:
        result = x / y
        print(x, "divided by", y, "is :", result)
    except ZeroDivisionError:
        print("Error! You are dividing by zero")
        
divide(3, 2)  # prints "3 divided by 2 is : 1.5"
divide(3, 0)  # prints "Error! You are dividing by zero"

# slide 13: try-except-else statement
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error! You are dividing by zero")
    else:
        print(x, "divided by", y, "is :", result)
        
divide(3, 2)  # prints "3 divided by 2 is : 1.5"
divide(3, 0)  # prints "Error! You are dividing by zero"

# slide 14: try-except-else-finally statement 
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error! You are dividing by zero")
    else:
        print(x, "divided by", y, "is :", result)
    finally:
        print("The function execution terminated")
        
divide(3, 2)  # prints "3 divided by 2 is : 1.5" followed by "The function execution terminated"
divide(3, 0)  # prints "Error! You are dividing by zero" followed by "The function execution terminated"     

# slide 15: try-finally statement 
def divide(lst1, lst2):
    lst3 = []
    try:
        for index in range(len(lst1)):
            result = lst1[index] / lst2[index]
            lst3.append(result)
    finally:
        # if the finally clause executes a return, break or continue
        # statement, the saved exception is discarded
        return lst3

print(divide([10, 20, 30, 40], [2, 4, 0, 5]))  # prints [5.0, 5.0]

# slide 16: try-except-finally statement 
def divide(lst1, lst2):
    lst3 = []
    try:
        for index in range(len(lst1)):
            result = lst1[index] / lst2[index]
            lst3.append(result)
    except IndexError:
        print("Error: index", index, "does not exist in the list", lst2)
    finally:
        # if the finally clause executes a return, break or continue
        # statement, the saved exception is discarded
        return lst3

print(divide([10, 20, 30, 40], [2, 4, 0, 5]))  # prints [5.0, 5.0]
print(divide([10, 20, 30, 40], [2, 4, 5]))  # prints "Error: index 3 does not exist in the list [2, 4, 5]" followed by [5.0, 5.0, 6.0]

# slide 17: displaying the original exception that is thrown in the except clause
age = input("Please enter your age: ")
try:
    age = int(age)   
except Exception as e:
    print("Exception:", e)
    print("Please enter the correct input.")
else:
    print(age)
    
# slide 18: Raising Exceptions
'''
There are three ways of raising an exception:
1. Without specifying an exception class
2. With specifying an exception class
3. With an argument passed to the exception class
'''
# slide 20:
# 1. raise statement without specifying an exception class
num1 = int(input("Enter 1st whole number: "))
num2 = int(input("Enter 2nd whole number: "))
try:
    print(num1 / num2)
except ZeroDivisionError:
    raise
# num2 = 0 raises ZeroDivisionError

# slides 21-22:
# 2. raise statement with specifying an exception class
num1 = int(input("Enter 1st whole number: "))
num2 = int(input("Enter 2nd whole number: "))
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Please enter positive integer values") 
# num2 = 0 raises ZeroDivisionError, printing "Please enter positive integer values"

# slide 22: additional validation can be directed to an existing exception
num1 = int(input("Enter 1st whole number: "))
num2 = int(input("Enter 2nd whole number: "))
try:
    # condition for checking for negative values
    if num1 < 0 or num2 < 0:
        # raising exception using raise keyword
        raise ZeroDivisionError
    print(num1 / num2)
except ZeroDivisionError:
    print("Please enter positive integer values")
# any invalid (here negative) input value will be dealt within the
# ZeroDivisionError exception
# if num1 or num2 is negative, "Please enter positive integer values." is printed

# slides 23-25:
# 3. raise statement with an argument passed to the exception class
value = input("Enter a whole number: ")
if not(value.isdigit() or value[0] == '-' and value[1:].isdigit()):
    raise TypeError("Only integers are allowed")
# If the entered value is not an integer, TypeError exception is raised and shown

# slide 24
value = int(input("Enter a whole number: "))
if value < 0:
    raise Exception("Negative numbers are not allowed")
# If the entered value is a negative number, Exception: Numbers below zero are not allowed is raised and shown

# slide 25: The previous 2 examples joined together raise an error and
# stop the program if value is not an integer or if it is a negative integer
value = input("Enter a whole number: ")
if value.isdigit() or value[0] == '-' and value[1:].isdigit():
    if int(value) < 0:
        raise Exception("Negative numbers are not allowed; you entered: " + value)
else:
    raise TypeError("Only integers are allowed; you entered: " + value)
# If the entered value is a negative number (e.g. -1), the following is raised and shown:
# Exception: Numbers below zero are not allowed; you entered: -1
# If the entered value is not an int (e.g. 1.5), the following is raised and shown:
# TypeError: Only integers are allowed; you entered: 1.5