# Mod1A: Lambda Functions & Comprehensions

'''
#1a. 
def salary_with_bonus(salary, bonus):
    return salary + bonus

salary = 25000
bonus = 1250

print('1a. labda: ', (lambda salary, bonus: salary + bonus)(25000, 1250))
print('1a: ', salary_with_bonus(25000, 1250))


#1b. 
def salary_with_bonus(salary):
    return salary + (salary * 0.5)

print('1b: ', salary_with_bonus(25000))

print('labda: ', (lambda salary, bonus=0.05: salary + (salary * 0.05))(25000))

#1c.
def salary_with_bonus(salary):
    bonus = salary * 0.05
    return salary + bonus
print('1c. ', salary_with_bonus(25000))

print('labda 1c: ', (lambda salary: salary + (salary * 0.05))(25000))



#2a.
#my understaning
#bonus = float(input("Tell me the value for the bonus: \n"))
#salary = float(input("Tell me the value for the salary: \n"))
#print('labda 2a: ', (lambda salary, bonus: salary + (salary * bonus))(salary, bonus))


#lambda function accepts two changeable parameters: salary & bonus
def regular_higher_order_func(salary, bonus, func):
          return func(salary, bonus)

print('regular_higher_order_func bonus = 0.05: ',regular_higher_order_func(25000, 0.05, lambda salary, bonus: salary + (salary * bonus)))
print('regular_higher_order_func bonus = 0.1: ',regular_higher_order_func(25000, 0.1, lambda salary, bonus: salary + (salary * bonus)))
print('regular_higher_order_func bonus = 0.2: ',regular_higher_order_func(25000, 0.2, lambda salary, bonus: salary + (salary * bonus)))

#lambda function accepts two parameters: salary & bonus, one of which (bonus) is fixed (keyword argument) 
# - making it effectively a lambda function that accepts one changeable parameter.
def regular_higher_order_func(salary, func):
          return func(salary)

print('regular_higher_order_func bonus=0.05', regular_higher_order_func(25000, lambda salary, bonus=0.05: salary + (salary * bonus)))


#2b.
lambda_higher_order_func = lambda salary, bonus, func : func(salary, bonus)

print('lambda_higher_order_func 0.05: ', lambda_higher_order_func(25000, 0.05, lambda salary, bonus: salary + (salary * bonus)))
print('lambda_higher_order_func 0.10: ', lambda_higher_order_func(25000, 0.10, lambda salary, bonus: salary + (salary * bonus)))
print('lambda_higher_order_func 0.20: ', lambda_higher_order_func(25000, 0.20, lambda salary, bonus: salary + (salary * bonus)))

lambda_higher_order_func = lambda salary, func : func(salary)

print('lambda_higher_order_func bonus = 0.05: ', lambda_higher_order_func(25000, lambda salary, bonus = 0.05: salary + (salary * bonus)))
print('lambda_higher_order_func bonus = 0.10: ', lambda_higher_order_func(25000, lambda salary, bonus = 0.10: salary + (salary * bonus)))
print('lambda_higher_order_func bonus = 0.20: ', lambda_higher_order_func(25000, lambda salary, bonus = 0.20: salary + (salary * bonus)))

#2c.
# returned from an ordinary custom-built higher order function
# passing only the bonus value as argument to the higher order function.
def ordinary_higher_order_function(bonus):
    return lambda salary: salary + (salary * bonus)

salary_with_bonus = ordinary_higher_order_function(0.05)
print('2c: ', salary_with_bonus(25000))


# d) returned from a lambda custom-built higher order function
#    passing only the bonus value as argument to the higher order function.

lambda_higher_order_function = lambda bonus : lambda salary : salary + salary * bonus
# to calculate salary with the bonus for a given employee's salary, 
# where the bonus value is passed as argument to the higher order function
salary_with_bonus = lambda_higher_order_function(0.05)
print('2d: ', salary_with_bonus(25000))



#3
lst_numbers = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]

#3a. list comprehension
def filter_valid_salaries(lstNum):
    positive_lst = [x for x in lstNum if type(x) == int and x >= 0]
    return positive_lst

print('\n3a: ', filter_valid_salaries(lst_numbers))

#3b. takes up no space in memory
lst_numbers = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]

def filter_valid_salaries(lstNum):
     # returns each value without saving it to a list
     return (x for x in lst_numbers if x >= 0)

generator_valid_salaries = filter_valid_salaries(lst_numbers)
list_valid_salaries = list(generator_valid_salaries)

print('\n3b: ', list_valid_salaries )

'''
#3c. filter function

#return only odd numbers
#for x in filter(lambda n : n % 2 == 1, lst_numbers):
#    print(x)

# non-comprehension
#positive_list = []
#for x in filter(lambda n : n >= 0, lst_numbers):
#    print(x)
#    positive_lst.append(x) 
#print('3c_: ', positive_lst)   

# list comprehension
'''
lst_numbers = [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000]

positive_lst = [x for x in filter(lambda n : n >= 0, lst_numbers)]
print('3c: ', positive_lst)


#q4.
#a. list comprehension
salaries = [29000, 48000, 31213, 15875, 17450, 50245, 75801]
def salary_with_bonus(salaries, bonus = 0.05):        
    return [salary + (salary * bonus) for salary in salaries]

print(salary_with_bonus(salaries))


#4b. generator comprehension
salaries = [29000, 48000, 31213, 15875, 17450, 50245, 75801]

def salary_with_bonus(salaries, bonus = 0.05):        
    return (salary + (salary * bonus) for salary in salaries)

generator_salaries_with_bonus = salary_with_bonus(salaries)
lst_salaries_with_bonus = list(generator_salaries_with_bonus)
print(lst_salaries_with_bonus)

#4c. the map() built-in function
def salaries_with_bonus(salaries):
    return list(map(lambda salary : salary + salary * 0.05, salaries))
lst_salaries = [29000, 48000, 31213, 15875, 17450, 50245, 75801]
lst_salaries_with_bonus = salaries_with_bonus(lst_salaries)
print("\nQ4c:", lst_salaries_with_bonus)  # returns [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]
# Assume bonus is 5%.

#q5

#5.a lambda function passed as an argument to an ordinary higher order function featuring
#5ai list function
def ordinary_higher_order_function(salary, func):
    return func(salary)

def salaries_with_bonus(salary, bonus):
    return list(ordinary_higher_order_function(sal, lambda sal : sal + (sal * bonus)) for sal in salary)

print('5ai: ', salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))


#5aii. list comprehension - will be the same as list function (i.e. "list()") but instead of the list we enclose it in []
def ordinary_higher_order_function(salary, func):
    return func(salary)

def salaries_with_bonus(salary, bonus):
    return [ordinary_higher_order_function(sal, lambda sal : sal + (sal * bonus)) for sal in salary]

print('5ai: ', salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))

#5aiii. generator comprehension - same as list but this time enclosed in an extra ()
def ordinary_higher_order_function(salary, func):
    return func(salary)

def salaries_with_bonus(salary, bonus):
    return list((ordinary_higher_order_function(sal, lambda sal : sal + (sal * bonus)) for sal in salary))

print('5ai: ', salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))

#b. lambda function passed as argument to a lambda higher order function featuring

#5bi list function
lambda_higher_order_function = lambda salary, func : func(salary)

def salaries_with_bonus(salary, bonus):
    return list(lambda_higher_order_function(sal, lambda sal : sal + (sal * bonus)) for sal in salary)

print('5ai: ', salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))

#5bii. list comprehension
lambda_higher_order_function = lambda salary, func : func(salary)

def salaries_with_bonus(salary, bonus):
    return [lambda_higher_order_function(sal, lambda sal : sal + (sal * bonus)) for sal in salary]

print('5ai: ', salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))

#5biii. generator comprehension
lambda_higher_order_function = lambda salary, func : func(salary)

def salaries_with_bonus(salary, bonus):
    return list((lambda_higher_order_function(sal, lambda sal : sal + (sal * bonus)) for sal in salary))

print('5ai: ', salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))


'''
#c lambda function returned from an ordinary higher order function featuring (NB: not the same as his solutions)
#5ci.
def ordinary_higher_order_function(bonus):
    return lambda sal : sal + (sal * bonus)

def salaries_with_bonus(salary, bonus):
    salary_with_bonus = ordinary_higher_order_function(bonus)
    return list(salary_with_bonus(sal) for sal in salary)

print("5ci:", salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))


#5bii. list comprehension
def ordinary_higher_order_function(bonus):
    return lambda sal : sal + (sal * bonus)

def salaries_with_bonus(salary, bonus):
    salary_with_bonus = ordinary_higher_order_function(bonus)
    return [salary_with_bonus(sal) for sal in salary]

print("5ci:", salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))

#5biii. generator comprehension
def ordinary_higher_order_function(bonus):
    return lambda sal : sal + (sal * bonus)

def salaries_with_bonus(salary, bonus):
    salary_with_bonus = ordinary_higher_order_function(bonus)
    return list((salary_with_bonus(sal) for sal in salary))
    
print("5ci:", salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801], 0.05))


#d.