#################################################
# Module 1A - Lambda Functions & Comprehensions #
#################################################

# slides 7-8 - defining lambda functions

# 1-parameter lambda function example:
lambda x : x + 1
# equivalent regular (ordinary) function:
def add1(x):
    return x + 1
# calling ordinary function add1:
print(add1(5))

# multi-parameter lambda function example:
lambda x, y : x + y
# equivalent regular (ordinary) function:
def add(x, y):
    return x + y
# calling ordinary function add:
print(add(2, 3))

# no parameter lambda function example:
lambda : 1
# equivalent regular (ordinary) function:
def one():
    return 1
# calling ordinary function one:
print(one())

# lambda function definition with a default argument example:
lambda x, y=10 : x + y
# equivalent regular (ordinary) function:
def add_default(x, y=10):
    return x + y
# calling ordinary function with two parameters and with one parameter:
print(add_default(2, 3)) # prints 5
print(add_default(2))    # prints 12

# lambda function definition returning more than one value:
lambda x, y, z : (x + 1, y * 2, z ** 3)
# equivalent regular (ordinary) function:
def multi_expressions(x, y, z):
    return (x + 1, y * 2, z ** 3)
# calling ordinary function multi_expressions
result = multi_expressions(1, 2, 3)
print(result)  # prints (2, 4, 27)
# the above lambda and regular functions return multiple values within one tuple
# a regular function can also return multiple values as they are:
def multi_expressions2(x, y, z):
    return x + 1, y * 2, z ** 3
a, b, c = multi_expressions2(1, 2, 3)
print(a, b, c)  # prints 2 4 27

# slides 9-14 - calling lambda functions
# 2 ways:
# 1) Immediately Invoked Function Expression - IIFE, pronounced 'iffy'
# 1a) Surround the function and its argument with parentheses
(lambda x : x + 1)(2)             # returns 3
(lambda x, y : x + y)(2, 3)       # returns 5
(lambda : 1)()                    # returns 1
(lambda x, y = 10 : x + y)(2)     # returns 12
(lambda x, y = 10 : x + y)(2, 3)  # returns 5
(lambda x, y, z : (x + 1, y * 2, z ** 3))(1, 2, 3)  # returns (2, 4, 27)

# 1b) IIFE - Invoke the last evaluated lambda function definition in
#     the shell, by using _ with parentheses surrounding its argument(s)
#     (can be done in the shell only)

# 2) Assign a name to it and call it like an ordinary function
add1 = lambda x : x + 1
add1(2)  # returns 3

add = lambda x, y : x + y
add(2, 3)  # returns 5

one = lambda : 1
one()   # returns 1

add_default = lambda x, y = 10 : x + y
add_default(2)   # returns 12
add_default(2, 3)   # returns 5

multi_expressions = lambda x, y, z : (x + 1, y * 2, z ** 3)
multi_expressions(1, 2, 3)  # returns (2, 4, 27)

# slides 15-27 - Appropriate use of lambda functions
# high_order_function(par1, par2, ..., parn, function())

# 1) Lambda function passed as argument to a (regular or lambda) higher order function
# 1a) Lambda function passed as argument to a regular higher order function
# regular higher order function definition:
def regular_higher_order_func(x, func):
    return x + func(x)
# lambda function passed as argument to a regular higher order function call:
regular_higher_order_func(2, lambda x : x * x)  # returns 6

# 1b) Lambda function passed as argument to a lambda higher order function
# lambda higher order function definition
lambda_higher_order_func = lambda x, lambda_func : x + lambda_func(x)
# lambda function passed as argument to a lambda higher order function call:
lambda_higher_order_func(2, lambda x : x * x)  # returns 6
# Note 1: the same could have been achieved with:
(lambda x : x + x * x)(2)  # returns 6
# but here we can't supply the function as argument in runtime
# Note 2: the function to be passed as argument can be defined as an ordinary function:
def regular_func(x):
    return x * x
lambda_high_order_func = lambda x, regular_func : x + regular_func(x)
lambda_high_order_func(2, regular_func)  # returns 6
# However, in order to implement the second function call from slide 17, 
# the regular function regular_func() would have to be re-defined: 
def regular_func(x):
    return x + 3
regular_higher_order_func(2, regular_func)  # returns 7
# making this implementation less flexible than the implementation through lambda function:
lambda_higher_order_func(2, lambda x : x + 3)  # returns 7
# Passing a lambda function as argument to a higher order function allows
# passing different functions ad hoc in runtime, without pre-defining them within the code
# To pass a function in runtime to a higher order function, define it as a string 
# and use the eval() function to evaluate it:
lambda_higher_order_func = lambda x, lambda_func : x + lambda_func(x)
lambda_func = input('Enter the lambda function definition: ')
lambda_higher_order_func(2, eval(lambda_func))  #  returns 6 if the inputted function was lambda x : x * x
lambda_higher_order_func(2, eval(lambda_func))  #  returns 7 if the inputted function was lambda x : x + 3
# the first parameter (x) can also be passed to the higher order function in runtime:
x = int(input('Enter the value for the first parameter (variable x): '))
lambda_func = input('Enter the lambda function definition: ')
lambda_higher_order_func(x, eval(lambda_func))  #  returns 6 if the inputted value for x is 2 and the function was lambda x : x * x
lambda_higher_order_func(x, eval(lambda_func))  #  returns 7 if the inputted value for x is 2 and the function was lambda x : x + 3

# 2) Lambda functions defined within custom-built higher order functions
# 2a) A lambda function defined within a regular custom-built higher-order function
def my_product(n):
    return lambda a : a * n
double = my_product(2)
double(10)  # returns 20
triple = my_product(3)
triple(10)  # returns 30
# Note: the same could have been achieved with just one call:
my_product(2)(10)  # returns 20
my_product(3)(10)  # returns 30
# but this way we need to supply both arguments within the function call
# rather than supplying one at a time.

# 2b) A lambda function defined within a lambda custom-built higher-order function
my_product = lambda n: lambda a : a * n
double = my_product(2)
double(10)  # returns 20
triple = my_product(3)
triple(10)  # returns 30

# 3) Lambda functions passed as arguments to the built-in functions
# 3a) Lambda function passed to the map() function
'''
Syntax:
    map(in_function, iterable1[, iterable2, iterable3, ...]) -> map object (an iterator)
The map() function takes at least two arguments. 
The first argument is a user-defined function, and then one or more iterable types.
If you pass only one iterable, then map() applies the user-defined function to each
of the elements of its second argument (the iterable). However, if you provide multiple
iterables, then the function will be called with each of their elements as arguments.
Important rule for map() function:
When passed to the map() function, lambda function must have the same number
of parameters as the number of iterables passed to the map() function
'''
# Example 1 - with map() and the lambda function with 1 parameter
lst_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for el in map(lambda n : n * n, lst_numbers):
    print(el)  # prints squared numbers from the above list
lst_squared = list(map(lambda n : n * n, lst_numbers))  # stores the list of squared numbers from the above list: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 2 - with map() and the lambda function with 2 parameters
# Option 1: fix one of the parameters and use map() with one iterable:
lst_squared = list(map(lambda n, k=2 : n ** k, lst_numbers))
# Option 2: use lambda with 2 parameters and map() with two iterables:
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_powered = list(map(lambda n, k : n ** k, list_1, list_2))  # stores [1, 32, 729]  ( 1 ** 4 = 1; 2 ** 5 = 32; 3 ** 6 = 729 )
# Note:
# In computer science the technique illustrated in the example above is called partial application.
# Partial application (or partial function application) refers to the process of fixing a number of parameters
# to a function, producing another function of smaller number of parameters.
# In the above example, the initial lambda function has 2 parameters: n & k, of which we fixed the second:
# k to value 2, producing a lambda function with smaller number of parameters (just one: n).

# 3b) Lambda function passed to the filter() function:
'''
Syntax:
    filter(function or None, iterable) -> filter object (an iterator)
The filter() function returns an iterator yielding those items of the
iterable for which function(item) is True. If function is None,
return the items that are True.
'''
lst_numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# to return all odd numbers from the given list
# of numbers, use filter() within the loop:
for el in filter(lambda n : n % 2 == 1, lst_numbers):
    print(el) 
# to store all odd numbers from the given list in a list
# nest filter() within the list() function: 
lst_odd = list(filter(lambda n : n % 2 == 1, lst_numbers))  # stores [-5, -3, -1, 1, 3, 5]
# Note:
# Since filter() always accepts just two arguments: a function and an iterable,
# the function must always include only one parameter. To pass a function with
# multiple parameters to the filter() function, you need to apply partial
# application to the function (if the function has n parameters, you need to
# fix n-1 parameters to specific values).


# 3c) Lambda function passed to the reduce() function from functools module
'''
Syntax:
    reduce(function, sequence[, initial]) -> value
The function reduce() applies a function of two arguments cumulatively
to the items of a sequence, from left to right, so as to reduce the
sequence to a single value.
If initial is present, it is placed before the items of the sequence
in the calculation, and serves as a default when the sequence is empty.
'''
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4])  # adds numbers in the list together, returning 10 ((((1+2)+3)+4) 
# applying the same function to a list of strings concatenates
# list elements into a single string
reduce(lambda x, y: x + y, ['1', '2', '3', '4'])  # returns '1234' (((('1'+'2')+'3')+'4')
reduce(lambda x, y: x + y, [[1], [2, 3], [], [4, 5, 6]])  # returns [1, 2, 3, 4, 5, 6] ((([1]+[2, 3])+[])+[4, 5, 6]) 
reduce(lambda x, y: x + y, [1, 2, 3, 4], 100)  # returns 110, as 100 serves as initial value to ((((1+2)+3)+4) 
reduce(lambda x, y: x + y, [], "Empty list")  # returns 'Empty list', as the sequence is empty
reduce(lambda x, y: x + 1, [1, 2, 3, 4], 0)  # returns 4 (the number of elements in the list [1, 2, 3, 4], with the initiall value 0)
# calculate the total of numeric values in a list and the number of elements in the list at the same time:
reduce(lambda x, y: (x[0] + y, x[1] + 1), [1, 2, 3, 4], (0, 0))  # returns (10, 4)
# a sequence of 2 values is needed to return two values, e.g. tuple - determined by brackets around
# the returned values: x[0] + y and x[1] + 1; initial value is set to (0, 0) - 1st 0 for the total
# and 2nd 0 for the number of elements in the list; x[0] refers to the 1st value (total), x[1] refers to
# the 2nd value (no. of elements)
# reduce() can be use to find the average:
total_count = reduce(lambda x, y: (x[0] + y, x[1] + 1), [1, 2, 3, 4], (0, 0))  # sum_count stores (10, 4)
average = total_count[0]/total_count[1]  # average stores 2.5
# or (simplified version):
lst_num = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, lst_num, 0)  # total stores 10
average = total/len(lst_num)  # average stores 2.5 

# 4) Lambda functions passed as arguments to the key functions
# 4a) example with sorted() function
lst_dimensions = [(3, 3), (4, 2), (2, 2), (5, 2), (1, 7)]
lst_areas = sorted(lst_dimensions, key=lambda tpl : tpl[0] * tpl[1])
print(lst_areas)  # prints [(2, 2), (1, 7), (4, 2), (3, 3), (5, 2)]

# 4b) example with sort() list method
lst_dates = ['01/May/2018', '21/Oct/2020', '05/Jan/2018', '16/Dec/2019', '10/Mar/2020']
months = {'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'Jun':5, 'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11}
lst_dates.sort(key=lambda date : months[date.split('/')[1]])
# lst_dates contains the list of dates sorted by months:
print(lst_dates)  # prints ['05/Jan/2018', '10/Mar/2020', '01/May/2018', '21/Oct/2020', '16/Dec/2019']

# slides 28-30 - If Statements within Lambda Function
# lambda with a two-way if statement
sign = lambda number : 'positive' if number >= 0 else 'negative'
sign(10)

# lambda with a three-way if statement
sign = lambda number : 'positive' if number > 0 else ('zero' if number == 0 else 'negative')
sign(0)

# lambda with a 4-way if statement
grade = lambda mark : 'fail' if mark < 75 else ('pass' if mark < 80 else ('merit' if mark < 90 else 'distinction'))
grade(74)  # returns 'fail'
grade(75)  # returns 'pass'
grade(80)  # returns 'merit'
grade(90)  # returns 'distinction'

# Motivating Example from slides 32-33:
# Given a list of elements of different data types,
# create a new list by extracting and squaring the integers
# Solution 1: using list(), filter() and map() built-in functions: 
a_list = [3, 'Z', 7, -2, '4', 2.53, 'w', '!']
filtered_ints = list(filter(lambda e: type(e) == int, a_list))
filtered_ints  # returns [3, 7, -2]
modified_ints = list(map(lambda e: e**2, filtered_ints))
modified_ints  # returns [9, 49, 4]
# combining list(), filter() and map() into one statement:
a_list = [3, -2, 0, 7.28, 'C', 'a string', ['a', 'list', 3], ('a', 'tuple')]
squared_ints = list(map(lambda e: e**2, filter(lambda e: type(e) == int, a_list)))
print(squared_ints)  # prints [9, 4, 0]

# Solution 2: using list comprehension:
squared_ints = [e**2 for e in a_list if type(e) == int]
print(squared_ints)  # prints [9, 4, 0]

# the above solution 2 is an example of a list comprehension
# with one condition

# slides 36-37
# list comprehension with multiple conditions:
a_list = [3, -2, 0, 7.28, 'C', 'a string', ['a', 'list', 3], ('a', 'tuple')]
# Example 1: extract non-negative integer values from the above list 
non_negative_ints = [e for e in a_list if type(e) == int and e >= 0]
print(non_negative_ints)  # prints [3, 0]

# Example 2: from the above list extract integer values that negative or greater than 5 
ints_and_floats_lt_0_and_gt_5 = [e for e in a_list if (type(e) == int or type(e) == float) and (e < 0 or e > 5)]
print(ints_and_floats_lt_0_and_gt_5)  # prints [-2, 7.28]

# slide 38-40 - dictionary comprehension:
# Example 1: dictionary comprehension from a range of integer values
power_dict = {num: num**num for num in range(1, 6)}
print(power_dict)  # prints {1: 1, 2: 4, 3: 27, 4: 256, 5: 3125}

# Example 2: dictionary comprehension from a dictionary
price_eu = {'milk':1, 'bread':2.5, 'tea':1.55}
euro_to_pound = 0.86
price_gb = {prod: price*euro_to_pound for (prod, price) in price_eu.items()}
print(price_gb)  # prints {'milk': 0.86, 'bread': 2.15, 'tea': 1.333}

# Example 3: dictionary comprehension from a dictionary with a condition
ages = {'paul': 47, 'ada': 38, 'sam': 15, 'luna': 22, 'neil':67, 'julia': 55}
life_stages = {name: ('minor' if age < 18 else 'young' if age < 40 else 'middle-aged' if age < 65 else 'elderly') for (name, age) in ages.items()}
print(life_stages)  # prints {'paul': 'middle-aged', 'ada': 'young', 'sam': 'minor', 'luna': 'young', 'neil': 'elderly', 'julia': 'middle-aged'}

# slides 42-43 - generator comprehension:
power_gen = (num**num for num in range(1, 6))
print(power_gen)  # prints <generator object <genexpr> at 0x03F36AB0>
# To view the values generated by the generator object you can use a loop:
for value in power_gen:
    print(value, end=' ')  # prints 1 4 27 256 3125 
# Once a generator object is used, it becomes empty
# Trying to display the values again won’t work, unless you re-create the generator object
# If needed, we can store the generated values in an iterable (for example in a list):
lst_power_gen = list(num**num for num in range(1, 6))
print(lst_power_gen)  # prints [1, 4, 27, 256, 3125]

# slide 44 - Combining lambda function with list comprehension
# For example, the solution from slide 37 can be parametrised as follows:
ints_and_floats_lt_0_and_gt_5 = lambda prices : [e for e in prices if (type(e) == int or type(e) == float) and (e < 0 or e > 5)]
# Now we can call this lambda function by passing any list to it as an argument:
ints_and_floats_lt_0_and_gt_5(a_list)  # returns [-2, 7.28]

# slide 45 - Combining lambda function with generator comprehension
ints_and_floats_lt_0_and_gt_5 = lambda prices : (e for e in prices if (type(e) == int or type(e) == float) and (e < 0 or e > 5))
# Now we can call this lambda function by passing any list to it as an argument:
ints_and_floats_lt_0_and_gt_5(a_list)  # returns <generator object <lambda>.<locals>.<genexpr> at 0x037E6770>
# This creates a generator, which can be either traversed within a loop, or saved into a data structure (e.g. a list):
list_ints_and_floats_lt_0_and_gt_5 = list(ints_and_floats_lt_0_and_gt_5(a_list))
print(list_ints_and_floats_lt_0_and_gt_5)  # prints [-2, 7.28]

