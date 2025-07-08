#################################
# Module 2B - Class Inheritance #
#################################

'''
When considering the relationship between a subclass and its
superclass, two situations need to be looked at separately:
1) If the subclass does not have a customised constructor
2) If the subclass does have a customised constructor
'''

# 1) If the subclass does not have a customised constructor,
#    then the object of the subclass is created through the
#    constructor of its superclass

# slides 8-9
# If superclass also does not have a customised constructor,
# then the object of the subclass is created through the
# default constructor of its superclass
class Employee:
    def work(self):
        print("This is superclass")

class Manager(Employee):
    def manage(self):
        print("This is subclass")

manager = Manager()
manager.work()    # This is superclass
manager.manage()  # This is subclass
employee = Employee()
employee.work()   # This is superclass
#employee.manage() # throws AttributeError: 'Employee' object has no attribute 'manage'

# slide 11
# If superclass does have a customised constructor, then the
# object of the subclass is created through the customised
# constructor of its superclass
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def work1(self):
        print("In superclass method: name:", self.name, "salary:", self.salary)

class Manager(Employee):
    def work2(self):
        print("In subclass method: name:", self.name, "salary:", self.salary)

# client code
manager = Manager('John Smith', 30000)
manager.work1()
manager.work2()
print("Outside both methods: name:", manager.name, "salary:", manager.salary)
employee = Employee('Ana Dix', 32000)
employee.work1()   # In superclass method: name: Ana Dix salary: 32000
#employee.work2()  # throws AttributeError: 'Employee' object has no attribute 'work2'

# 2) If the subclass does have a customised constructor,
#    then the object of the subclass is created through the
#    constructor of the subclass
class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title 
        self.salary = salary
    def work(self):
        print("work() method running")

class Manager(Employee):
    def __init__(self):
        self.team = []
    def manage(self, employee):
        self.team.append(employee.name)
        
# client code
manager = Manager()
#print(manager.name) # throws AttributeError: 'Manager' object has no attribute 'name'
manager.work()  # work() method running
# In the class Employee above, 'name', 'job_title' and 'salary'
# are instance variables of the (objects of) class Employee.
# Despite Manager being set as subclass of Employee, since
# Manager’s custom constructor does not invoke Employee’s
# constructor, the instance variables of class Employee:
# 'name', 'job_title' and 'salary’ will not be available to
# objects of Manager class.
# However, the Employee’s method work() is accessible from
# (objects of) class Manager, as Manager is defined as subclass
# of Employee and access to Employee’s methods is not affected
# by the constructor.

# slide 16
# If the subclass has a customised constructor, in order to
# make parent’s instance variables available to the child’s
# class, the child’s constructor must include a call to
# parent’s constructor
class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title 
        self.salary = salary
    def work(self):
        pass

class Manager(Employee):
    def __init__(self, name, job_title, salary):
        Employee.__init__(self, name, job_title, salary)
        self.team = []
    def manage(self, employee):
        self.team.append(employee.name)

# client code
john_smith = Employee('John Smith', 'Developer', 30000)
ana_dix = Employee('Ana Dix', 'Developer', 32000)
katie_brown = Manager('Katie Brown', 'Line Manager', 40000)
print(john_smith.__dict__)
print(ana_dix.__dict__)
print(katie_brown.__dict__)
katie_brown.manage(john_smith)
katie_brown.manage(ana_dix)
print(katie_brown.__dict__)

max_ross = Manager('Max Ross', 'Project Manager', 45000)
print(max_ross.__dict__)
sam_ford = Employee('Sam Ford', 'Designer', 29000)
print(sam_ford.__dict__)
max_ross.manage(sam_ford)
max_ross.manage(katie_brown)
print(max_ross.__dict__)

# slide 18
# the parent's constructor can also be called using the super() function
class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title 
        self.salary = salary
    def work(self):
        pass
    
class Manager(Employee):
    def __init__(self, name, job_title, salary):
        super().__init__(name, job_title, salary)
        self.team = []
    def manage(self, employee):
        self.team.append(employee.name)
        
# client code
john_smith = Employee('John Smith', 'Developer', 30000)
ana_dix = Employee('Ana Dix', 'Developer', 32000)
katie_brown = Manager('Katie Brown', 'Line Manager', 40000)
print(john_smith.__dict__)
print(ana_dix.__dict__)
print(katie_brown.__dict__)
katie_brown.manage(john_smith)
katie_brown.manage(ana_dix)
print(katie_brown.__dict__)

max_ross = Manager('Max Ross', 'Project Manager', 45000)
print(max_ross.__dict__)
sam_ford = Employee('Sam Ford', 'Designer', 29000)
print(sam_ford.__dict__)
max_ross.manage(sam_ford)
max_ross.manage(katie_brown)
print(max_ross.__dict__)

# slide 20
print(isinstance(john_smith, Employee))  # True
print(isinstance(katie_brown, Manager))  # True
print(isinstance(katie_brown, Employee)) # True 
print(isinstance(john_smith, Manager))   # False
print(issubclass(Manager, Employee))  # True
print(issubclass(Employee, Manager))  # False

# slide 27
# checking whether protected method in the superclass
# can be directly accessed through its subclass
class Animal:
    # protected method
    def _move(self):
        print('animal is moving')
    def jump(self):
        self._move()
        print('animal is jumping')
    
class Dog(Animal):
    def move(self):
        super()._move()
        print('dog is jumping')
        
# client code
animal = Animal()
animal._move() # directly calling protected method from the object of class itself
animal.jump()  # indirectly calling protected method from the object of class itself

dog = Dog()
dog.move()  # indirectly calling protected method from the object of subclass
dog._move() # directly calling protected method from the object of subclass
      

# slide 29
# checking whether private method in the superclass
# cannot be directly accessed through its subclass
class Animal:
    # private method
    def __move(self):
        print('animal is moving')
    def jump(self):
        self.__move()
        print('animal is jumping')
    
class Dog(Animal):
    def move(self):
        super().__move()
        print('dog is jumping')

animal = Animal()
animal._Animal__move() # directly calling protected method from the object of class itself
#animal.__move() # throws AttributeError: 'Animal' object has no attribute '__move'
animal.jump()  # indirectly calling protected method from the object of class itself

dog = Dog()
#dog.move() # throws AttributeError: 'super' object has no attribute '_Dog__move'
#dog.__move() # throws AttributeError: 'Dog' object has no attribute '__move'
dog._Animal__move()  # this works but should be refrained from

# slide 31
# defining a private attribute in the superclass, to make it
# not accessible from the subclass
class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title 
        self.__salary = salary  # salary is private attribute
    def print_salary(self):
        print(self.__salary)

class Manager(Employee):
    def __init__(self, name, job_title, salary):
        super().__init__(name, job_title, salary)
        self.team = []

# client code:
emp_john = Employee('John', 'Developer', 30000)
emp_john.print_salary()  # prints 30000
#print(emp_john.salary)  # throws AttributeError: 'Employee' object has no attribute 'salary'

mng_katie = Manager('Katie', 'Project manager', 45000)
mng_katie.print_salary()  # 45000
#print(mng_katie.salary)  # AttributeError: 'Manager' object has no attribute 'salary'

# slide 32
# check if private attribute oof a class can be accessed through
# a private method
class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.__salary = salary  # salary is private attribute
    def __print_salary(self):   # print_salary is private method
        print(self.__salary)
    def display_salary(self):
        self.__print_salary()
        
class Manager(Employee):
    def __init__(self, name, job_title, salary):
        super().__init__(name, job_title, salary)
        
# client code
emp_john = Employee('John', 'Developer', 30000)
#emp_john.print_salary()  # AttributeError: 'Employee' object has no attribute 'print_salary'
print('dir(emp_john):\n', dir(emp_john))  # does not include print_salary; includes '_Employee__print_salary' instead
emp_john._Employee__print_salary()   # prints 30000 (but should be refrained from)
#print(emp_john.salary)  # throws AttributeError: 'Employee' object has no attribute 'salary'
print(emp_john.__dict__)  # does not include salary; includes '_Employee__salary' instead
emp_john.display_salary()  # prints 30000 (and this is the correct way of printing employees' salary)

mng_katie = Manager('Katie', 'Project manager', 45000)
#mng_katie.print_salary()  # throws AttributeError: 'Manager' object has no attribute 'print_salary'
mng_katie._Employee__print_salary()# prints 45000 (but should be refrained from)
#print(mng_katie.salary)  # AttributeError: 'Manager' object has no attribute 'salary'

# slide 35 - Abstract Classes
# syntax for defining an abstract class
from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    
    @abstractmethod
    def abstract_method_name(self):
        pass

# A class that is derived from ABC metaclass cannot be instantiated
# unless all of its abstract methods and properties are overridden:
#abstract_class_object = AbstractClassName()
# The line above throws TypeError: Can't instantiate abstract class
# AbstractClassName with abstract methods abstract_method_name

# Any class with no abstract methods or properties like the one below
# can be instantiated:
class AbstractClassName(ABC):
    # public instance method
    def abstract_method_name(self):
        pass

abstract_class_object = AbstractClassName() # does not throw an error
# However, there is little use of creating an abstract class without
# any abstract method.

# slide 36 - Payroll program
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self): 
        return self.first_name + ' ' + self.last_name

    @abstractmethod
    def get_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self): 
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hours_worked, rate):
        super().__init__(first_name, last_name)
        self.hours_worked = hours_worked
        self.rate = rate

    def get_salary(self): 
        return self.hours_worked * self.rate

class Payroll:
    def __init__(self):
        self.employee_list = []
        
    def add_employee(self, employee): 
        self.employee_list.append(employee)

    def print_payroll(self):
        for e in self.employee_list:
            print(e.full_name + '\t' + '£' + str(e.get_salary()))
            
payroll = Payroll()

payroll.add_employee(FullTimeEmployee('John', 'Smith', 30000))
payroll.add_employee(FullTimeEmployee('Anna', 'Dix', 32000))
payroll.add_employee(HourlyEmployee('Katie', 'Brown', 800, 50))
payroll.add_employee(HourlyEmployee('Max', 'Ross', 450, 100))
payroll.add_employee(HourlyEmployee('Sam', 'Ford', 290, 100))

payroll.print_payroll()

# to change salary of a full-time employee:
target_emp_first_name = 'Anna'
target_emp_last_name = 'Dix'
new_salary = 38000
for e in payroll.employee_list:
    if e.first_name == target_emp_first_name and e.last_name == target_emp_last_name:
        e.salary = new_salary
            
# to change hours_worked & rate of an hourly-paid employee:
target_emp_first_name = 'Sam'
target_emp_last_name = 'Ford'
new_emp_hours_worked = 320
new_emp_rate = 100
for e in payroll.employee_list:
    if e.first_name == target_emp_first_name and e.last_name == target_emp_last_name:
         e.hours_worked = new_emp_hours_worked
         e.rate = new_emp_rate

payroll.print_payroll()

# displaying employee's first name through a property (getter) full_name:
ft_emp_ada_wallace = FullTimeEmployee('Ada', 'Wallace', 35000)
# full_name is not an instance attribute:
print('ft_emp_ada_wallace.__dict__ =', ft_emp_ada_wallace.__dict__)  # {'first_name': 'Ada', 'last_name': 'Wallace', 'salary': 35000}
# but full_name is listed as available property:
print('dir(ft_emp_ada_wallace):\n', dir(ft_emp_ada_wallace))   # includes 'first_name', 'full_name', 'get_salary', 'last_name', 'salary'
# to display Ada's full name (treat the property full_name as it was a common instance attribute):
print('ft_emp_ada_wallace.full_name:', ft_emp_ada_wallace.full_name)  # ft_emp_ada_wallace.full_name: Ada Wallace
# although full_name is in fact a property (getter):
print('FullTimeEmployee.full_name:', FullTimeEmployee.full_name)  # FullTimeEmployee.full_name: <property object at 0x03FC7A50>


# An alternative solution to the one from slide 36 - Payroll program:
# 2 changes:
# 1) remove the @property decorator above the full_time() getter
#    (transforming full_time() getter to a public instance method)
# 2) in the print_payroll() method of Payroll class, add brackets at the
#    end of full_name: e.full_name(), as full_name() is now a (public instance)
#    method instead of a property (getter)
# The only difference between these two solutions is that in the first one
# we can refer to full_name as if it was another instance attribute: e.full_name,
# while in the second solution we must refer to it as a (public instance) method: e.full_name().
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    #@property
    def full_name(self): 
        return self.first_name + ' ' + self.last_name

    @abstractmethod
    def get_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self): 
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hours_worked, rate):
        super().__init__(first_name, last_name)
        self.hours_worked = hours_worked
        self.rate = rate

    def get_salary(self): 
        return self.hours_worked * self.rate

class Payroll:
    def __init__(self):
        self.employee_list = []
        
    def add_employee(self, employee): 
        self.employee_list.append(employee)

    def print_payroll(self):
        for e in self.employee_list:
            print(e.full_name() + '\t' + '£' + str(e.get_salary()))
            
def main(): 
    payroll = Payroll()

    payroll.add_employee(FullTimeEmployee('John', 'Smith', 30000))
    payroll.add_employee(FullTimeEmployee('Anna', 'Dix', 32000))
    payroll.add_employee(HourlyEmployee('Katie', 'Brown', 800, 50))
    payroll.add_employee(HourlyEmployee('Max', 'Ross', 450, 100))
    payroll.add_employee(HourlyEmployee('Sam', 'Ford', 290, 100))

    payroll.print_payroll()

    # to change salary of a full-time employee:
    target_emp_first_name = 'Anna'
    target_emp_last_name = 'Dix'
    new_salary = 38000
    for e in payroll.employee_list:
        if e.first_name == target_emp_first_name and e.last_name == target_emp_last_name:
            e.salary = new_salary
                
    # to change hours_worked & rate of an hourly-paid employee:
    target_emp_first_name = 'Sam'
    target_emp_last_name = 'Ford'
    new_emp_hours_worked = 320
    new_emp_rate = 100
    for e in payroll.employee_list:
        if e.first_name == target_emp_first_name and e.last_name == target_emp_last_name:
             e.hours_worked = new_emp_hours_worked
             e.rate = new_emp_rate

    payroll.print_payroll()

    # displaying employee's full name through a public instance method full_name():
    ft_emp_ada_wallace = FullTimeEmployee('Ada', 'Wallace', 35000)
    # full_name is not an instance attribute:
    print('ft_emp_ada_wallace.__dict__ =', ft_emp_ada_wallace.__dict__)  # {'first_name': 'Ada', 'last_name': 'Wallace', 'salary': 35000}
    # but full_name is listed as available (instance) method:
    print('dir(ft_emp_ada_wallace):\n', dir(ft_emp_ada_wallace))   # includes 'first_name', 'full_name', 'get_salary', 'last_name', 'salary'
    # to display Ada's full name (treat full_name as a common public instance method):
    print('ft_emp_ada_wallace.full_name():', ft_emp_ada_wallace.full_name())  # ft_emp_ada_wallace.full_name: Ada Wallace
    # as in fact now full_name is a common public instance method:
    print('FullTimeEmployee.full_name:', FullTimeEmployee.full_name)  # FullTimeEmployee.full_name: <function Employee.full_name at 0x03EEC150>
    

main()


