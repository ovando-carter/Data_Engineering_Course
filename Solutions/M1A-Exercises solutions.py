################################
# Module 1A - Lambda Functions #
################################

# Question 1
# Create a lambda function salary_with_bonus that calculates employee's 
# salary with the bonus,
# a) where both employee's salary and bonus are passed in as parameters
salary_with_bonus = lambda salary, bonus : salary + salary * bonus
print("\nQ1a:", salary_with_bonus(25000, 0.05))
# b) where both employee's salary and bonus are passed in as parameters
#    but bonus is fixed as keyword argument ("kwarg")
salary_with_bonus = lambda salary, bonus=0.05 : salary + salary * bonus
print("\nQ1b:", salary_with_bonus(25000))
# c) where only employee's salary is passed in as a parameter and bonus is fixed (hard-coded)
salary_with_bonus = lambda salary : salary + salary * 0.05
print("\nQ1c:", salary_with_bonus(25000))
# Assume bonus is 5%.


# Question 2
# The value of the bonus can change over time. Therefore, we want to
# create a solution that will parametrise the bonus value as well as
# the salary.
# # However we don't want a function with two parameters; instead we want
# to re-use the existing lambda function created in Question 1.
# Use the lambda function from Question 1 as a lambda function:
# a)  passed as an argument to an ordinary higher order function
# soution 1 - where lambda function accept two changeable parameters: salary & bonus
def ordinary_higher_order_func(sal, bon, func):
    return func(sal, bon)
print("\nQ2a_sol_1:", ordinary_higher_order_func(25000, 0.05, lambda salary, bonus : salary + salary * bonus))
# soution 2 - where lambda function accepts two parameters: salary & bonus,
#             one of which (bonus) is fixed (keyword argument), making it
#             effectively a lambda function that accepts one changeable parameter
def ordinary_higher_order_func(sal, func):
    return func(sal)
print("\nQ2a_sol_2:", ordinary_higher_order_func(25000, lambda salary, bonus=0.05 : salary + salary * bonus))

# b)  passed as an argument to a lambda higher order function
# soution 1 - where lambda function accepts two changeable parameters: salary & bonus
lambda_higher_order_func = lambda sal, bon, func : func(sal, bon)
print("\nQ2b_sol_1:", lambda_higher_order_func(25000, 0.05, lambda salary, bonus : salary + salary * bonus))
# soution 2 - where lambda function accepts two parameters: salary & bonus,
#             one of which (bonus) is fixed (keyword argument), making it
#             effectively a lambda function that accepts one changeable parameter
lambda_higher_order_func = lambda sal, func : func(sal)
print("\nQ2b_sol_2:", lambda_higher_order_func(25000, lambda salary, bonus=0.05 : salary + salary * bonus))

# c) returned from an ordinary custom-built higher order function
#    passing only the bonus value as argument to the higher order function.
def ordinary_higher_order_function(bonus):
    return lambda salary : salary + salary * bonus
# and use it to calculate salary with the bonus for a given employee's salary
# with bonus value to be passed as argument to the higher order function.
salary_with_bonus = ordinary_higher_order_function(0.05)
print("\nQ2c:", salary_with_bonus(25000))

# d) returned from a lambda custom-built higher order function
#    passing only the bonus value as argument to the higher order function.
lambda_higher_order_function = lambda bonus : lambda salary : salary + salary * bonus
# to calculate salary with the bonus for a given employee's salary, 
# where the bonus value is passed as argument to the higher order function
salary_with_bonus = lambda_higher_order_function(0.05)
print("\nQ2d:", salary_with_bonus(25000))


# Question 3
# Write the function filter_valid_salaries that removes any non-positive 
# salary from the list of salaries (leaving only positive salaries) using:
# a) list comprehension
def filter_valid_salaries(salaries):
    return [salary for salary in salaries if salary > 0]
lst_salaries = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]
lst_valid_salaries = filter_valid_salaries(lst_salaries)
print("\nQ3a:", lst_valid_salaries) # returns [29000, 48000, 31213, 15875, 17450, 50245, 75801]

# b) generator comprehension
def filter_valid_salaries(salaries):
    return (salary for salary in salaries if salary > 0)
lst_salaries = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]
generator_valid_salaries = filter_valid_salaries(lst_salaries)
lst_valid_salaries_salaries = list(generator_valid_salaries)
print("\nQ3b:", lst_valid_salaries) # returns [29000, 48000, 31213, 15875, 17450, 50245, 75801]

# c) the filter() built-in function
def filter_valid_salaries(salaries):
    return list(filter(lambda salary: salary > 0, salaries))
lst_salaries = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]
lst_valid_salaries = filter_valid_salaries(lst_salaries)
print("\nQ3c:", lst_valid_salaries) # returns [29000, 48000, 31213, 15875, 17450, 50245, 75801]


# Question 4
# Create a function salaries_with_bonus that returns the list of salaries with the bonus
# for a list of employees' salaries passed to it as parameter using:
# a) list comprehension
def salaries_with_bonus(salaries):
    return [salary + salary * 0.05 for salary in salaries]

lst_salaries = [29000, 48000, 31213, 15875, 17450, 50245, 75801]
lst_salaries_with_bonus = salaries_with_bonus(lst_salaries)
print("\nQ4a:", lst_salaries_with_bonus) # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]

# b) generator comprehension
def salaries_with_bonus(salaries):
    return (salary + salary * 0.05 for salary in salaries)

lst_salaries = [29000, 48000, 31213, 15875, 17450, 50245, 75801]
generator_salaries_with_bonus = salaries_with_bonus(lst_salaries)
lst_salaries_with_bonus = list(generator_salaries_with_bonus)
print("\nQ4b:", lst_salaries_with_bonus) # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]

# c) the map() function
def salaries_with_bonus(salaries):
    return list(map(lambda salary : salary + salary * 0.05, salaries))
lst_salaries = [29000, 48000, 31213, 15875, 17450, 50245, 75801]
lst_salaries_with_bonus = salaries_with_bonus(lst_salaries)
print("\nQ4c:", lst_salaries_with_bonus)  # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]
# Assume bonus is 5%.


# Question 5
# Create a function salaries_with_bonus that returns the list of salaries with the bonus for a list of employees' salaries passed to it as parameter using:
# a) lambda function passed as an argument to an ordinary higher order function
def ordinary_higher_order_func(salary, func):
    return func(salary)
# featuring
#    i. list function
def salaries_with_bonus(bonus, salaries):
    return list(ordinary_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries)
print("\nQ5a_i:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    ii. list comprehension
def salaries_with_bonus(bonus, salaries):
    return [ordinary_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries]
print("\nQ5a_ii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    iii. generator  comprehension
def salaries_with_bonus(bonus, salaries):
    return list((ordinary_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries))
print("\nQ5a_iii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
# b) lambda function passed as argument to a lambda higher order function featuring
lambda_higher_order_func = lambda salary, func : func(salary)
#    i. list function
def salaries_with_bonus(bonus, salaries):
    return list(lambda_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries)
print("\nQ5b_i:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    ii. list comprehension
def salaries_with_bonus(bonus, salaries):
    return [lambda_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries]
print("\nQ5b_ii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    iii. generator comprehension
def salaries_with_bonus(bonus, salaries):
    return list((lambda_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries))
print("\nQ5b_iii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
# c) lambda function returned from an ordinary higher order function
#    Option c1 - where the returned lambda function acts upon one value
def ordinary_higher_order_function(bonus):
    return lambda salary : salary + salary * bonus
# featuring
#    i. list function
def salaries_with_bonus(bonus, salaries):
    salary_with_bonus = ordinary_higher_order_function(bonus)
    return list(salary_with_bonus(salary) for salary in salaries)
print("\nQ5c1_i:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    ii. list comprehension
def salaries_with_bonus(bonus, salaries):
    salary_with_bonus = ordinary_higher_order_function(bonus)
    return [salary_with_bonus(salary) for salary in salaries]
print("\nQ5c1_ii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    iii. generator comprehension
def salaries_with_bonus(vat, prices):
    salary_with_bonus = ordinary_higher_order_function(vat)
    return list((salary_with_bonus(price) for price in prices))
print("\nQ5c1_iii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    Option c2 - where the returned lambda function acts upon a list of values:
# featuring
#    i. list function
def ordinary_higher_order_function(bonus):
    return lambda salaries : list(salary + salary * bonus for salary in salaries)

def salaries_with_bonus(bonus, salaries):
    salaries_after_bonus = ordinary_higher_order_function(bonus)
    lst_salaries_with_bonus = salaries_after_bonus(salaries)
    return lst_salaries_with_bonus

print("\nQ5c2_i:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))

#    ii. list comprehension
def ordinary_higher_order_function(bonus):
    return lambda salaries : [salary + salary * bonus for salary in salaries]
def salaries_with_bonus(bonus, salaries):
    salaries_after_bonus = ordinary_higher_order_function(bonus)
    lst_salaries_with_bonus = salaries_after_bonus(salaries)
    return lst_salaries_with_bonus
print("\nQ5c2_ii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    iii. generator comprehension
def ordinary_higher_order_function(bonus):
    return lambda salaries : list((salary + salary * bonus for salary in salaries))
def salaries_with_bonus(bonus, salaries):
    salaries_after_bonus = ordinary_higher_order_function(bonus)
    lst_salaries_with_bonus = salaries_after_bonus(salaries)
    return lst_salaries_with_bonus
print("\nQ5c2_iii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))

# d) lambda function returned from a lambda higher order function featuring
#    Option d1 - where the returned lambda function acts upon one value
lambda_higher_order_function = lambda bonus: lambda salary : salary + salary * bonus
# featuring
#    i. list function
def salaries_with_bonus(bonus, salaries):
    salary_with_bonus = lambda_higher_order_function(bonus)
    return list(salary_with_bonus(salary) for salary in salaries)
print("\nQ5d1_i:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    ii. list comprehension
def salaries_with_bonus(bonus, salaries):
    salary_with_bonus = lambda_higher_order_function(bonus)
    return [salary_with_bonus(salary) for salary in salaries]
print("\nQ5d1_ii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    iii. generator comprehension
def salaries_with_bonus(bonus, salaries):
    prices_after_tax = lambda_higher_order_function(bonus)
    return list((prices_after_tax(salary) for salary in salaries))
print("\nQ5d1_iii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))

#    Option d2 - where the returned lambda function acts upon a list of values:
# featuring
#    i. list function
lambda_higher_order_function = lambda bonus : lambda salaries: list(salary + salary * bonus for salary in salaries)
def salaries_with_bonus(bonus, salaries):
    salaries_after_bonus = lambda_higher_order_function(bonus)
    lst_salaries_with_bonus = salaries_after_bonus(salaries)
    return lst_salaries_with_bonus
print("\nQ5d2_i:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    ii. list comprehension
lambda_higher_order_function = lambda bonus : lambda salaries: [salary + salary * bonus for salary in salaries]
def salaries_with_bonus(bonus, salaries):
    salaries_after_bonus = ordinary_higher_order_function(bonus)
    lst_salaries_with_bonus = salaries_after_bonus(salaries)
    return lst_salaries_with_bonus
print("\nQ5d2_ii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))
#    iii. generator comprehension
lambda_higher_order_function = lambda bonus : lambda salaries: list((salary + salary * bonus for salary in salaries))
def salaries_with_bonus(bonus, salaries):
    salaries_after_bonus = lambda_higher_order_function(bonus)
    lst_salaries_with_bonus = salaries_after_bonus(salaries)
    return lst_salaries_with_bonus
print("\nQ5d2_iii:", salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801]))

# Question 6
# The input list contains integer values that should represent employee's salaries,
# however some of its values are erroneous: some values are 0, while others are negative.
# Assuming that bonus is 5%, write the function valid_salaries_with_bonus that returns
# a list of salaries with the bonus for a list of employees' salaries passed to it as
# parameter, while ignoring any erroneous values using:
# a) list comprehension
def valid_salaries_with_bonus(salaries):
    return [salary + salary * 0.05 for salary in salaries if salary > 0]

lst_salaries = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]
lst_valid_salaries_with_bonus = valid_salaries_with_bonus(lst_salaries)
print("\nQ6a:", lst_valid_salaries_with_bonus) # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]

# b) generator comrehension
def valid_salaries_with_bonus(salaries):
    return (salary + salary * 0.05 for salary in salaries if salary > 0)

lst_salaries = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]
generator_valid_salaries_with_bonus = valid_salaries_with_bonus(lst_salaries)
lst_valid_salaries_with_bonus = list(generator_valid_salaries_with_bonus)
print("\nQ6b:", lst_valid_salaries_with_bonus) # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]

# c) map() and filter() built-in functions
def valid_salaries_with_bonus(salaries):
    return list(map(lambda salary : salary + salary * 0.05, filter(lambda salary: salary > 0, salaries)))
lst_salaries = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]
lst_valid_salaries_with_bonus = valid_salaries_with_bonus(lst_salaries)
print("\nQ6c:", lst_valid_salaries_with_bonus)  # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]


# Question 7
# Write a Python program to sort a list of tuples using lambda function.
# Sort the courses by their achievement in descending order
# Tip: pass the lambda function as the value to the key parameter of sorted() function or sort() method
course_marks = [('SQL', 88), ('Excel', 90), ('Python', 97), ('Unix', 82), ('Web Apps', 78), ('Java', 75)]
print("\nQ7: Original list of tuples:")
print(course_marks)
sorted_course_marks = sorted(course_marks, key = lambda x: x[1], reverse=True)
print("Sorted list of tuples - using sorted() function:")
print(sorted_course_marks)
course_marks.sort(key = lambda x: x[1], reverse=True)
print("Sorted list of tuples - using sort() method:")
print(course_marks)


# Question 8
# Write a Python program to sort a list of dictionaries using lambda function.
# Sort the mobile phone models by their colour in alphabetical order
models = [{'make':'Nokia', 'model':216, 'colour':'Black'}, {'make':'Mi Max', 'model':'2', 'colour':'Gold'}, {'make':'Samsung', 'model': 7, 'colour':'Blue'}]
print("\nQ8: Original list of dictionaries:")
print(models)
sorted_models = sorted(models, key = lambda x: x['colour'])
print("Sorted list of dictionaries :")
print(sorted_models)


# Question 9
# Write a lambda function starts_with that finds if a given string starts with a character 'P'
# (returns True if it does; False if it doesn't)
# Tip: use the dir command to list all string methods and try to find one that could help with this task
starts_with = lambda x: True if x.startswith('P') else False
print("\nQ9:", starts_with('Python'))
print(starts_with('Java'))


# Question 10
# Change the lambda function from previous question to find if a given string starts with a given character passed to it as a parameter
starts_with = lambda x, y: True if x.startswith(y) else False
print("\nQ10:", starts_with('Python', 'P'))
print(starts_with('Java', 'P'))


# Question 11
# Write a Python program to find intersection of two given lists using lambda function
# Tip: pass the lambda function as argument to the filter() function
list_nums1 = [8, 7, 1, 9, 3, 6, 5, 2]
list_nums2 = [1, 2, 4, 8, 9]
print("\nQ11: Original lists:")
print(list_nums1)
print(list_nums2)
result = list(filter(lambda x: x in list_nums1, list_nums2)) 
print ("Intersection of the said lists: ", result)


# Question 12
# Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.
# Tip: pass the lambda function as argument to the filter() function
list_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
substring = 'emb'
print("\nQ12: Original list:", list_strings)
print("Substring to search:", substring)
result = list(filter(lambda x: substring in x, list_strings)) 
print ("Elements of the said list that contain specific substring: ", result)


# Question 13
# Write a Python program to find the values of length 5 in a given list using lambda function
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_5 = filter(lambda month: month if len(month)==5 else '', months)
print("\nQ13:")
for m in months_5:
    print(m)


# Question 14
# Change the lambda function from previous question to find values of any given length in a given list
months_length = filter(lambda month, length=8: month if len(month)==length else '', months)
print("\nQ14:")
for month in months_length:
    print(month)


# Question 15
# Write a Python program to find palindromes in a given list of strings using lambda function
texts = ["!", "php", "w3r", "Python", "ada", "Java", "abcd", "aaa", 'aoxomoxoa', 'BaroccoraB']
print("\nQ15: Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("List of palindromes:")
print(result)


# Question 16
# Write a Python program that multiplies each number of a given list with a given number using lambda function.
# Print the result as a string of numbers.
# Example:
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22
nums = [2, 4, 6, 9 , 11]
n = 2
print("\nQ16: Original list: ", nums)
print("Given number: ", n)
filtered_numbers = list(map(lambda number: number*n, nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))


# Question 17
# Write a Python function to multiply all the numbers in a given list using lambda.
#Original list:
#[4, 3, 2, 2, -1, 18]
#Multiply all the numbers of the said list: -864
#Original list:
#[2, 4, 8, 8, 3, 2, 9]
#Multiply all the numbers of the said list: 27648
# Tip: import the functools module and find help on the function reduce()
from functools import reduce 
def mutiple_list(nums):
    result =  reduce(lambda x, y: x*y, nums)
    return result
nums = [4, 3, 2, 2, -1, 18]
print ("\nQ17: Original list: ")
print(nums)
print("Multiply all the numbers of the said list:", mutiple_list(nums))
nums = [2, 4, 8, 8, 3, 2, 9]
print ("Original list: ")
print(nums)
print("Multiply all the numbers of the said list:", mutiple_list(nums))


# Question 18
# Write a Python function that finds the maximum of all the numbers in a given list using lambda.
def max_list(nums):
    result =  reduce(lambda x, y: max(x,y), nums)
    return result

print("\nQ18: The maximum of all the numbers of the said list:", max_list(nums))


# Question 19
# Write a Python function that finds the minimum of all the numbers in a given list using lambda.
def min_list(nums):
    result =  reduce(lambda x, y: min(x,y), nums)
    return result

print("\nQ19: The minimum of all the numbers of the said list:", min_list(nums))


# Question 20
# Write a Python function that finds the average of all the numbers in a given list using lambda.
def avg_list(nums):
    result =  reduce(lambda x, y: x+y, nums) / len(nums)
    return result

print("\nQ20: The average of all the numbers of the said list:", avg_list(nums))


# Question 21
# Write a Python function to find the list with maximum length in a list of lists using lambda function.
# The function should return a tuple consisting of two elements:
# 1) the max length
# 2) the list having the max length
# Example:
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
orig_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("\nQ21: Original list:")
print(orig_list)
print("List with maximum length of lists:")
print(max_length_list(orig_list))

# Note: the above function returns two values in form of a 2-value tuple
# The print() statement just prints the tuple out as it is
# Another way of calling this function is:
maxLength, maxList = max_length_list(orig_list) # assigns the 1st returned value to maxLength and the 2nd to maxList
# we can then print the returned values separately:
print('The longest list length is', maxLength, 'and is obtained by the list', maxList)


# Question 22
# Write a Python function to find the list with minimum length in a list of lists using lambda function.
# The function should return a tuple consisting of two elements:
# 1) the min length
# 2) the list having the min length
# Example:
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with minimum length of lists:
# (1, [0])   
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
      
orig_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("\nQ22: Original list:")
print(orig_list)
print("List with minimum length of lists:")
print(min_length_list(orig_list))

# Note: the above function returns two values in form of a 2-value tuple
# The print() statement just prints the tuple out as it is
# Another way of calling this functions is:
minLength, minList = min_length_list(orig_list) # assigns the 1st returned value to minLength and the 2nd to minList
# we can then print the returned values separately:
print('The shortest list length is', minLength, 'and is obtained by the list', minList)


# Question 23
# a) Write an ordinary function to create the biggest number by rearranging the digits of a given number.
def rearrange_biggest(number):
    #Break the number into digits and store in a list
    numbers = list(str(number))
    # sort the list in descending order
    numbers_desc = sorted(numbers, reverse=True)
    # convert the list back to string
    biggest_num =''.join(numbers_desc)
    return int(biggest_num)

number = 213
print("\nQ23a: The biggest number from", number, "is:", rearrange_biggest(number))

# b) Use method chaining to create a one-line version of the above function
def rearrange_biggest_V2(number):
    return int(''.join(sorted(list(str(number)), reverse=True)))

number = 213
print("\nQ23b: The biggest number from", number, "is:", rearrange_biggest_V2(number))

# c) Create a lambda function from the one-line version of the above function
rearrange_biggest_lambda = lambda number: int(''.join(sorted(list(str(number)), reverse=True)))

number = 213
print("\nQ23c: The biggest number from", number, "is:", rearrange_biggest_lambda(number))


# Question 24
# Write a Python program to count the occurrences of the items in a given list using lambda.
# Tip: return the dictionary where the keys are the different (unique) items and the values
# are their corresponding frequency. Use the count() list method to count the occurrences of
# different list items.
# Example:
# Original list:
#  [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
#  Count the occurrences of the items in the said list:
#  {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

# without lambda:
def count_occurrences_v1(nums):
    # building dictionary gradually
    dictionary = {}
    for el in nums:
        if el not in dictionary.keys():
            dictionary[el] = nums.count(el)
    return dictionary
nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
print("\nQ24a: Original list:")
print(nums)
print("Count the occurrences of the items in the said list (gradually):")
print(count_occurrences_v1(nums))  # returns {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

# Dictionary Comprehension:
def count_occurrences_v2(nums):
    # using dictionary comprehension
    dictionary = {el: nums.count(el) for el in nums}
    return dictionary
nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
print("\nQ24b: Original list:")
print(nums)
print("Count the occurrences of the items in the said list (using dictionary comprehension):")
print(count_occurrences_v2(nums))  # returns {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

# dict() function:
def count_occurrences_v3(nums):
    # using dict() function
    dictionary = dict({(el, nums.count(el)) for el in nums})
    return dictionary
nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
print("\nQ24c: Original list:")
print(nums)
print("Count the occurrences of the items in the said list (using dict() function):")
print(count_occurrences_v3(nums))  # returns {8: 2, 1: 1, 2: 2, 4: 2, 3: 4, 0: 2, 5: 3}

# using lambda function
def count_occurrences_V4(nums):
    # combining the dict() function and lambda as key argument to the map() function
    result = dict(map(lambda el : (el, nums.count(el)), nums))
    return result
nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
print("\nQ24d: Original list:")
print(nums)
print("Count the occurrences of the items in the said list (using lambda):")
print(count_occurrences_V4(nums))  # returns {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}


# Question 25
# Write a lambda function named cap_string that capitalises the first letter of a string.
cap_string = lambda string : string[:1].upper() + string[1:]
print("\nQ25:")
print(cap_string('Uppercase'))        # prints 'Uppercase'
print(cap_string('lowercase'))        # prints 'Lowercase'
print(cap_string('UpperCamelCase'))   # prints 'UpperCamelCase' 
print(cap_string('lowerCamelCase'))   # prints 'LowerCamelCase'


# Question 26
# a) Write an ordinary function that accepts two parameters: a string and a boolean key variable upper_rest.
# If upper_rest=True is passed as 2nd argument, lambda function capitalises the first letter and capitalises
# the rest of the string. If upper_rest=False is passed as 2nd argument, lambda function capitalises the
# first letter and leaves the rest of the string as the original string.
# Tip: use the expression from the lambda function created in question 25 as starting point to produce a one-line
# solution by including the if statement to it.
def capitalise(string, upper_rest=False):
    return string[:1].upper() + (string[1:].upper() if upper_rest else string[1:])

print("\nQ26a: Using capitalise ordinary function:")
print(capitalise('Uppercase', upper_rest=True))        # prints 'UPPERCASE'
print(capitalise('lowercase', upper_rest=True))        # prints 'LOWERCASE'
print(capitalise('UpperCamelCase', upper_rest=True))   # prints 'UPPERCAMELCASE'
print(capitalise('lowerCamelCase', upper_rest=True))   # prints 'LOWERCAMELCASE'

print()

print(capitalise('Uppercase', upper_rest=False))       # prints 'Uppercase'
print(capitalise('lowercase', upper_rest=False))       # prints 'Lowercase'
print(capitalise('UpperCamelCase', upper_rest=False))  # prints 'UpperCamelCase'
print(capitalise('lowerCamelCase', upper_rest=False))  # prints 'LowerCamelCase'

print()

# upper_rest=False is the default parameter; hence if the key upper_rest is not passed, False is assumed:
print(capitalise('Uppercase'))         # prints 'Uppercase'
print(capitalise('lowercase'))         # prints 'Lowercase'
print(capitalise('UpperCamelCase'))    # prints 'UpperCamelCase'
print(capitalise('lowerCamelCase'))    # prints 'LowerCamelCase'


# b) Write a lambda function that performs the task given in question 26a.
# When testing the ordinary function and the lambda function, call them with upper_rest=True, upper_rest=False and by omitting the parameter upper_rest altogether.
print("\n26b: Using capitalise lambda function:")
capitalise_lambda = lambda string, upper_rest=False : string[:1].upper() + (string[1:].upper() if upper_rest else string[1:])

print(capitalise_lambda('Uppercase', True))        # prints 'UPPERCASE'
print(capitalise_lambda('lowercase', True))        # prints 'LOWERCASE'
print(capitalise_lambda('UpperCamelCase', True))   # prints 'UPPERCAMELCASE'
print(capitalise_lambda('lowerCamelCase', True))   # prints 'LOWERCAMELCASE'

print()

print(capitalise_lambda('Uppercase', False))       # prints 'Uppercase'
print(capitalise_lambda('lowercase', False))       # prints 'Lowercase'
print(capitalise_lambda('UpperCamelCase', False))  # prints 'UpperCamelCase'
print(capitalise_lambda('lowerCamelCase', False))  # prints 'LowerCamelCase'

print()

# upper_rest=False is the default parameter; hence if the key upper_rest is not passed, False is assumed:
print(capitalise_lambda('Uppercase'))         # prints 'Uppercase'
print(capitalise_lambda('lowercase'))         # prints 'Lowercase'
print(capitalise_lambda('UpperCamelCase'))    # prints 'UpperCamelCase'
print(capitalise_lambda('lowerCamelCase'))    # prints 'LowerCamelCase'

