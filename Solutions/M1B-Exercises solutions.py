###################################
# Module 1B - Handling Exceptions #
###################################

# Question 1
# ----------
"""
The following code is prone to runtime errors:
    employee_list = ['Jane', 'Claire', 'Van', 'Sarah', 'Tomasz', 'Alisha']
    emp_code = input('Enter a employee code between 0 and ' + str(len(employee_list)-1) + ' to retrieve the corresponding employee name: ')
    print("The corresponding employee is: %s" % employee_list[int(emp_code)])
Run it and enter an inexistent list index to cause the code to throw an error
and find out the name of the specific exception from the traceback message.
Then use that exception name to change the code to make it safe
a) using the try-except block
b) using the try-except-else block
In both cases prompt the user to enter the employee code until it is valid.
"""
# solution 1a:
employee_list = ['Jane', 'Claire', 'Van', 'Sarah', 'Tomasz', 'Alisha']
while True:
    emp_code = input('Enter a employee code between 0 and ' + str(len(employee_list)-1) + ' to retrieve the corresponding employee name: ')
    try:
        # Throws error if emp_code < -len(employee_list) or emp_code > len(employee_list)-1
        print('The corresponding employee is: %s' % employee_list[int(emp_code)])
        break
    except IndexError:
        print('ERROR: The entered employee code is not within the requested range.')

# solution 1b:
employee_list = ['Jane', 'Claire', 'Van', 'Sarah', 'Tomasz', 'Alisha']
while True:
    emp_code = input('Enter a employee code between 0 and ' + str(len(employee_list)-1) + ' to retrieve the corresponding employee name: ')
    try:
        # Throws error if emp_code < -len(employee_list) or emp_code > len(employee_list)-1
        print('The corresponding employee is: %s' % employee_list[int(emp_code)])
    except IndexError:
        print('ERROR: The entered employee code is not within the requested range.')
    else:
        break


# Question 2
# ----------
"""
The following code is prone to runtime errors:
    employee_dict = {'id': 425137, 'name': 'Ali Rahmani', 'job-title':'Developer', 'emp_date': '15-04-2018'}
    attr = input('Enter an employee attribute (id, name, job-title, emp-date): ')
    print('The value for the employee attribute', attr, 'is:', employee_dict[attr])
Run it and enter an inexistent dictionary key to cause the code to throw an error and
find out the name of the specific exception from the traceback message.
Then use that exception name to change the code to make it safe
a) using the try-except block
b) using the try-except-else block
In both cases prompt the user to enter the employee attribute (key) until it is valid.
"""
# solution 2a:
employee_dict = {'id': 425137, 'name': 'Ali Rahmani', 'job-title':'Developer', 'emp-date': '15-04-2018'}
while True:
    attr = input('Enter an employee attribute (id, name, job-title, emp-date): ')
    try:
        # Throws error if the entered employee attribute (dictionary key) doesn't exist
        print('The value for the employee attribute', attr, 'is:', employee_dict[attr])
        break
    except KeyError:
        print("ERROR: The entered value is not an existing employee attribute.")

# solution 2b:
employee_dict = {'id': 425137, 'name': 'Ali Rahmani', 'job-title':'Developer', 'emp-date': '15-04-2018'}
while True:
    attr = input('Enter an employee attribute (id, name, job-title, emp-date): ')
    try:
        # Throws error if the entered employee attribute (dictionary key) doesn't exist
        print('The value for the employee attribute', attr, 'is:', employee_dict[attr])
    except KeyError:
        print("ERROR: The entered value is not an existing employee attribute.")
    else:
        break


# Question 3
# ----------
"""
The following code throws an error when the user enters a non-numeric value.
    number = float(input('Enter a number:'))
    print("You entered the number: ", number)
Find the name of the exception and use it to change the code to make it safe using the try-except-else block.
"""
# solution:
try:
    number = float(input('Enter a number: '))
except ValueError:
    print("ERROR: The entered value is not numeric.")
else:
    print("You entered the number:", number)


# Question 4
# ----------
"""
The solutions in question 1 will still throw an error if user enters a non-integer value.
Amend the code from questions 1a and 1b to make them safe.
"""
# solution 4a:
employee_list = ['Jane', 'Claire', 'Van', 'Sarah', 'Tomasz', 'Alisha']
while True:
    emp_code = input('Enter a employee code between 0 and ' + str(len(employee_list)-1) + ' to retrieve the corresponding employee name: ')
    try:
        # Throws error if emp_code < 0 or emp_code > len(employee_list)-1 or if emp_code is not an integer value
        print('The corresponding employee is: %s' % employee_list[int(emp_code)])
        break
    except ValueError:
        print("ERROR: The entered employee code is not a whole number.")
    except IndexError:
        print('ERROR: The entered employee code is within the requested range.')

# solution 4b:
employee_list = ['Jane', 'Claire', 'Van', 'Sarah', 'Tomasz', 'Alisha']
while True:
    emp_code = input('Enter a employee code between 0 and ' + str(len(employee_list)-1) + ' to retrieve the corresponding employee name: ')
    try:
        # Throws error if emp_code < 0 or emp_code > len(employee_list)-1 or if emp_code is not an integer value
        print('The corresponding employee is: %s' % employee_list[int(emp_code)])
    except ValueError:
        print("ERROR: The entered employee code is not a whole number.")
    except IndexError:
        print('ERROR: The entered employee code is within the requested range.')
    else:
        break

# Note:
# The order in which the exceptions (ValueError and IndexError) are listed is not important.
# If the entered value would cause throwing both exceptions (e.g. 9.88), Python will first try
# to convert the value to an integer - thus causing ValueError exception because of int('9.88').
# IndexError exception will be thrown only if the entered value is an integer
# (thus not throwing the ValueError exception).


# Question 5
# ----------
"""
# The follwing code throws an error if the user enters a file name that does not exist in the current working directory.
    file_name = input('Enter a file name:')
    f = open(file_name, 'r')
    print(f.read())
# Rectify the code to make it safe using the try-except block (without using the 'with' statement).
"""
# solution:
file_name = input('Enter a file name: ')
try:
    f = open(file_name, 'r')
except IOError:
    print('The file', file_name, 'does not exist.')


# Question 6
# ----------
# The safe code you wrote in question 5 will still throw an error if the file entered by the user includes some unreadable characters.
# Rectify the code to ensure it does not throw an error if the file is not found and if it is found but is unreadable.
# solution 1
file_name = input('Enter a file name: ')
try:
    f = open(file_name, 'r')
except IOError:
    print('The file', file_name, 'does not exist.')
else:
    # perform file operations and close the file only if file exists
    # (if file could not be opened, no need to close it)
    try:
        text = f.read()
        print(text)
    except ValueError:
        print("Error reading file '%s'." % file_name)
    except Exception as e:
        # any other error:
        print(e)        
    finally:
        f.close()
# Note: the unreadable file in fact throws the UnicodeDecodeError. Therefore, replacing ValueError
# with UnicodeDecodeError will work just as well. However, ValueError is a more generic error than
# UnicodeDecodeError (see Python exception hierarchy: https://docs.python.org/2/library/exceptions.html#exception-hierarchy)
# and will trap some other errors as well as UnicodeDecodeError when the input file is not in the expected format.

# solution 2 (shortened version of the above solution)
import os    # needed for the os.path.exists() function
file_name = input('Enter a file name: ')
if os.path.exists(file_name):
    f = open(file_name, 'r')
    try:
        text = f.read()
        print(text)
    except ValueError:
        print("Error reading file '%s'." % file_name)
    except Exception as e:
        # any other error:
        print(e)        
    finally:
        # the file was successfully opened as the if statement ensures 
        # the file exists; therefore the file must be closed
        f.close()
else:
    print('The file', file_name, 'does not exist.')
    
# solution 3 (using the 'with' statement)
file_name = input('Enter a file name: ')
try:
    with open(file_name, 'r') as f:
        text = f.read()
        print(text)
except IOError:
    print('The file', file_name, 'does not exist.')
except ValueError:
    print("Error reading file '%s'." % file_name)
except Exception as e:
    # any other error:
    print(e)        
# Note:
# Unlike the first two versions, there is no need to close the file when using WITH statement.
# The WITH statement ensures proper acquisition and release of resources.
# The two 'except' sections are still needed in case there is an error opening or reading the file.


# Question 7
# ----------
"""
Two lists are given: lst_monthly_incomes lists 3 freelancer's potential monthly incomes after tax (for each month in a quarter);
                     lst_weeks lists the number of weeks freelancer worked in each of the 3 months for that quarter (0-5)
Create an ordinary function safe_weekly_income() that takes the two lists as parameters and returns the third list, lst_weekly_incomes,
listing weekly amounts each salary produces rounded to 2 decimal places.
Examples:
If the list of monthly incomes is:
lst_monthly_incomes = [12345.67, 10646.77, 11734.34]
a) lst_weeks = [4, 3, 2] produces lst_weekly_incomes = [3086.42, 3548.92, 5867.17]
b) lst_weeks = [0, 3, 2] produces lst_weekly_incomes = []
c) lst_weeks = [5, 0, 1] produces lst_weekly_incomes = [2469.13]
d) lst_weeks = [4, 1, 0] produces lst_weekly_incomes = [3086.42, 10646.77]
e) lst_weeks = [4, 0, 0] produces lst_weekly_incomes = [3086.42]
f) lst_weeks = [0, 0, 0] produces lst_weekly_incomes = []
Tip: remember that if the finally clause executes a return statement, the saved exception is discarded.
"""
# solution:
def safe_weekly_income(lst_m_inc, lst_w):
    lst_w_in = []
    try:
        for index in range(len(lst_m_inc)):
            weekly_income = round(lst_m_inc[index] / lst_w[index], 2)
            lst_w_in.append(weekly_income)
    finally:
        return lst_w_in

# to call the function:
lst_monthly_incomes = [12345.67, 10646.77, 11734.34]
lst_weeks = [4, 1, 0]
print(safe_weekly_income(lst_monthly_incomes, lst_weeks))


# Question 8
# ----------
"""
Create a function improved_safe_weekly_income() to improve the function safe_weekly_income() from question 7
by including a user friendly message informing the user that the weekly income was not calculated in case(s)
0 number of weeks is entered in the second list.
"""
# solution:
def improved_safe_weekly_income(lst_m_inc, lst_w):
    lst_w_in = []
    error_msg = ''  # needed in case there is no ZeroDivisionError exception
    try:
        for index in range(len(lst_m_inc)):
            weekly_income = round(lst_m_inc[index] / lst_w[index], 2)
            lst_w_in.append(weekly_income)
    except ZeroDivisionError:
        error_msg = 'Error: The number of weeks (0) for the month ' + str(index+1) + ' produces no value for the weekly income.'
    finally:
        return error_msg, lst_w_in

# to call the function:
lst_monthly_incomes = [12345.67, 10646.77, 11734.34]
lst_weeks = [5, 4, 0]
print(improved_safe_weekly_income(lst_monthly_incomes, lst_weeks))
# OR
err_msg, lst_weekly_incomes = improved_safe_weekly_income(lst_monthly_incomes, lst_weeks)
print('List of weekly incomes:', lst_weekly_incomes)
if err_msg != '':
    print(err_msg)


# Question 9
# ----------
"""
Create a function further_improved_safe_weekly_income() to further improve the function improved_safe_weekly_income() from question 8
by including a user friendly message in case the second list (lst_weeks) has more elements than the first (lst_monthly_incomes).
"""
# solution:
def further_improved_safe_weekly_income(lst_m_inc, lst_w):
    lst_w_in = []
    error_msg1 = ''
    error_msg2 = ''
    try:
        for index in range(len(lst_m_inc)):
            weekly_income = round(lst_m_inc[index] / lst_w[index], 2)
            lst_w_in.append(weekly_income)
    except ZeroDivisionError:
        error_msg1 = 'Error: The number of weeks (0) for the month ' + str(index+1) + ' produces no value for the weekly income.'
    except IndexError:
        error_msg2 = 'Error: index ' + str(index) + ' does not exist in the list of weeks' + str(lst_w) + '.'
    finally:
        return error_msg1, error_msg2, lst_w_in

# to call the function:
lst_monthly_incomes = [12345.67, 10646.77, 11734.34]
lst_weeks = [4, 3]
print(further_improved_safe_weekly_income(lst_monthly_incomes, lst_weeks))
# OR
err_msg1, err_msg2, lst_weekly_incomes = further_improved_safe_weekly_income(lst_monthly_incomes, lst_weeks)
print('List of weekly incomes:', lst_weekly_incomes)
if err_msg1 != '':
    print(err_msg1)
if err_msg2 != '':
    print(err_msg2)


# Question 10
# -----------
"""
Create a function final_safe_weekly_income() to improve further still the function further_improved_safe_weekly_income() from question 9
by including a user friendly message in case any of the two lists do not have 3 elements.
Tip: raise an exception to direct dealing with this error within the same place where IndexError exception is dealt with
and change the error message accordingly to relate to both errors
"""
def final_safe_weekly_income(lst_m_inc, lst_w):
    lst_w_in = []
    error_msg1 = ''
    error_msg2 = ''
    try:
        for index in range(len(lst_m_inc)):
            weekly_income = round(lst_m_inc[index] / lst_w[index], 2)
            lst_w_in.append(weekly_income)       
        if (len(lst_m_inc) != len(lst_w) or len(lst_m_inc) != 3 or len(lst_w) != 3):
            raise IndexError
    except ZeroDivisionError:
        error_msg1 = 'Error: The number of weeks (0) for the month ' + str(index+1) + ' produces no value for the weekly income.'
    except IndexError:
        error_msg2 = 'Error: the two lists: ' + str(lst_m_inc) + ' and ' + str(lst_w) + ' must be of the same length: 3.'
    finally:
        return error_msg1, error_msg2, lst_w_in
# Note:
# the if statement must come after the loop otherwise the list of weekly incomes won't be created
# in case the lists are not of the same length: 3

# to call the function (testing error_msg2):
lst_monthly_incomes = [12345.67, 10646.77, 11734.34]
lst_weeks = [4, 2]
err_msg1, err_msg2, lst_weekly_incomes = final_safe_weekly_income(lst_monthly_incomes, lst_weeks)
print('List of weekly incomes:', lst_weekly_incomes)
if err_msg1 != '':
    print(err_msg1)
if err_msg2 != '':
    print(err_msg2)
    
# to call the function (testing error_msg1):
lst_monthly_incomes = [12345.67, 10646.77, 11734.34]
lst_weeks = [3, 0]
err_msg1, err_msg2, lst_weekly_incomes = final_safe_weekly_income(lst_monthly_incomes, lst_weeks)
print('List of weekly incomes:', lst_weekly_incomes)
if err_msg1 != '':
    print(err_msg1)
if err_msg2 != '':
    print(err_msg2)