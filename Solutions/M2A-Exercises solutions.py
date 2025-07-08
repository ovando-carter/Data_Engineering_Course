#######################
# Module 2A - Classes #
#######################


# Question 1
# ----------
"""
a) Write an empty Python class named Trainee and display its
   type and namespace. Additionally, display only the keys of
   the Trainee's namespace.
b) Create an object of class Trainee, and display its type,
   namespace and its class name.
c) Write an empty Python class named Trainer and create an object
   of this class. Check whether this object and the object of
   class Trainee created in question 1b are instances of the said
   classes or not. Also, check whether the classes Trainee and
   Trainer are subclasses of the built-in object class or not.
d) Add two class attributes: academy and trainee_name to the class
   Trainee. Modify the attribute values of the class Trainee
   and print the original and modified values of the attributes.
e) Add a class method to print the values of the two class 
   attributes: academy and trainee_name. Use this method to
   print the values of the two class attributes.
   Check that the two attributes and their values are included
   to the Trainee's class namespace.
f) Add an instance method to print the values of the two class
   attributes: academy and trainee_name from an object. Create
   an object of class Trainee and use the method to print the
   values of the two class attributes.
   Using the object's namespace check that the object has no 
   instance attributes.
   Access each class attribute from the object to print its value.
g) Add another instance method to the Trainee class to print the 
   values of its instance attributes (from an object, as instance
   attributes are not accessible from the class). 
   Create another object of class Trainee. 
   Print its class attributes:
   - using the class method created in question 1e
   - using the instance method created in question 1f
   - using the class namespace 
   - directly from the object. 
   Assign new values to the attributes academy and trainee_name 
   directly from the object. 
   Print class attributes and their values
   - using the class method created in question 1e
   - using the instance method created in question 1f    
   - using the class namespace.
   Then print the values of the object's instance attributes
   - using the instance method created in this question
   - using the object's namespace 
   - directly from the object. 
   Explain what has happened. 

Tip: use the __dict__ attribute to display the namespaces.
"""
# Question 1a)
# ------------
print('--- Q1a) ---')
class Trainee:
    pass
# Trainee's type
print(type(Trainee))            # prints <class 'type'>
# Trainee's namespace
print(Trainee.__dict__)
# the keys of the Trainee's namespace
print(Trainee.__dict__.keys())  # prints dict_keys(['__module__', '__dict__', '__weakref__', '__doc__'])


# Question 1b)
# ------------
print('--- Q1b) ---')
trainee = Trainee()
# trainee's type
print(type(trainee))           # prints <class '__main__.Trainee'>
# trainee's namespace
print(trainee.__dict__)        # prints {}
# trainee's class name
print(type(trainee).__name__)  # prints Trainee


# Question 1c
# -----------
print('--- Q1c) ---')
class Trainer:
    pass

trainer = Trainer()
print(isinstance(trainee, Trainee))  # prints True
print(isinstance(trainee, Trainer))  # prints False
print(isinstance(trainer, Trainee))  # prints False
print(isinstance(trainer, Trainer))  # prints True
print(issubclass(Trainee, object))   # prints True
print(issubclass(Trainer, object))   # prints True


# Question 1d)
# ------------
print('--- Q1d) ---')
class Trainee:
    academy = 'London'
    trainee_name = 'Paul'
    
print(Trainee.academy)        # prints 'London'
print(Trainee.trainee_name)   # prints 'Paul'
Trainee.academy = 'Leeds'
Trainee.trainee_name = 'Ana'
print(Trainee.academy)        # prints 'Leeds'
print(Trainee.trainee_name)   # prints 'Ana'


# Question 1e)
# ------------
print('--- Q1e) ---')
class Trainee:
    academy = 'London'
    trainee_name = 'Paul'

    @classmethod
    def print_class_attr_from_class_method(cls):
        print('class attribute academy =', cls.academy)
        print('class attribute trainee_name =', cls.trainee_name)

Trainee.print_class_attr_from_class_method()   # prints 'London' and 'Paul'
print('Trainee.__dict__\n', Trainee.__dict__)  # includes 'academy': 'London', 'trainee_name': 'Paul'


# Question 1f)
# ------------
print('--- Q1f) ---')
class Trainee:
    academy = 'London'
    trainee_name = 'Paul'

    @classmethod
    def print_class_attr_from_class_method(cls):
        print('class attribute academy =', cls.academy)
        print('class attribute trainee_name =', cls.trainee_name)

    # instance method
    def print_class_attr_from_instance_method(self):
        print('class attribute academy =', self.__class__.academy)
        print('class attribute trainee_name =', self.__class__.trainee_name)

trainee1 = Trainee()
trainee1.print_class_attr_from_instance_method()         # prints 'London' and 'Paul'
print('trainee1.__dict__:', trainee1.__dict__)           # prints {}
print('trainee1.academy =', trainee1.academy)            # prints 'London'
print('trainee1.trainee_name =', trainee1.trainee_name)  # prints 'Paul'


# Question 1g)
# ------------
print('--- Q1g) ---')
class Trainee:
    academy = 'London'
    trainee_name = 'Paul'

    @classmethod
    def print_class_attr_from_class_method(cls):
        print('class attribute academy =', cls.academy)
        print('class attribute trainee_name =', cls.trainee_name)
        
    # instance methods
    def print_class_attr_from_instance_method(self):
        print('class attribute academy =', self.__class__.academy)
        print('class attribute trainee_name =', self.__class__.trainee_name)

    def print_instance_attr(self):
        print('instance attribute academy =', self.academy)
        print('instance attribute trainee_name =', self.trainee_name)

trainee2 = Trainee()
# Print trainee2's class attributes and their values:
# - from the class method (created in question 1e)
trainee2.print_class_attr_from_class_method()     # prints 'London' and 'Paul'
# - from the instance method (created in question 1f)
trainee2.print_class_attr_from_instance_method()  # prints 'London' and 'Paul'
# - using the class namespace
print('Trainee.__dict__:', Trainee.__dict__)      # includes 'academy': 'London', 'trainee_name': 'Paul'
# - directly from the object
print('trainee2.academy =', trainee2.academy)     # prints 'London'
print('trainee2.trainee_name =', trainee2.trainee_name)  # prints 'Paul'

# the following two lines do not change the class attributes.
# instead, two new instance variables are createed, with the
# same name as the class attributes.
trainee2.academy = 'Leeds'
trainee2.trainee_name = 'Ana'

# Print trainee2's class attributes and their values:
# - from the class method (created in question 1e)
trainee2.print_class_attr_from_class_method()     # prints 'London' and 'Paul'
# - from the instance method (created in question 1f)
trainee2.print_class_attr_from_instance_method()  # prints 'London' and 'Paul'
# - using the class namespace
print('Trainee.__dict__:', Trainee.__dict__)      # includes 'academy': 'London', 'trainee_name': 'Paul'

# Print trainee2's instance attributes and their values:
# - from instance method (created in this question)
trainee2.print_instance_attr()                    # prints 'Leeds' and 'Ana'
# - using the object's namespace
print('trainee2.__dict__:', trainee2.__dict__)    # prints {'academy': 'Leeds', 'trainee_name': 'Ana'}
# - directly from the object
print('trainee2.academy =', trainee2.academy)     # prints 'Leeds'
print('trainee2.trainee_name =', trainee2.trainee_name)  # prints 'Ana'
# Explain what has happened:
# Values of class attributes cannot be assigned/changed through its
# objects. An attempt to do so creates new instance variable instead
# with the same name as the class attribute. The class attribute
# remains unchanged. If an object has a class and instance attribute
# with the same name, then the instance variable is prioritised.
# Thereforethe  value of instance attribute will be displayed when 
# accessed directly from the object.



# Question 2
# ----------
'''
Rewrite the class Trainee so that it has 2 class attributes:
company - initialised as 'FDM Group', and count - initialised
to 0, to count the number of trainees.
Also add two instance attributes: academy and trainee_name.
Keep the three methods created in your solution for question 1
and add two more methods: the constructor to set up the values
for the two instance attributes when creating a new object and
to increase the trainee counter, as well as the destructor to
decrease the counter every time a trainee is removed.
Once the class has been created, write the client code to do
the following:
- print the values of class attributes as soon as the class has
  been created
- print the Trainee class namespace (using the __dict__ attribute)
- create three trainees and for each one print its class and
  instance attributes, and its namespace (using the __dict__ attribute)
- remove the first trainee
- print the values of Trainee class attributes using the class
  (not an object)
'''
print('--- Q2 ---')
class Trainee:
    company = 'FDM Group'
    count = 0

    # class constructor
    def __init__(self, academy, trainee_name):
        print('adding ' + trainee_name + '...')
        self.academy = academy   
        self.trainee_name = trainee_name
        self.__class__.count += 1
        
    # class method
    @classmethod
    def print_class_attr_from_class_method(cls):
        print('class attribute company =', cls.company)
        print('class attribute count =', cls.count)

    #instance methods
    def print_class_attr_from_instance_method(self):
        print('class attribute company =', self.__class__.company)
        print('class attribute count =', self.__class__.count)

    def print_instance_attr(self):
        print('instance attribute academy =', self.academy)
        print('instance attribute trainee_name =', self.trainee_name)

    # class constructor
    def __del__(self):
        print('removing ' + self.__dict__['trainee_name'] + '...')
        self.__class__.count -= 1

# print the class attributes as soon as the class has been created
Trainee.print_class_attr_from_class_method()  # prints FDM Group and 0
# print the Trainee class namespace
print(Trainee.__dict__)     # includes 'company': 'FDM Group', 'count': 0
# create the 1st trainee
john_smith = Trainee('London', 'John Smith')
# print the values of its class and instance attributes
john_smith.print_class_attr_from_instance_method()  # prints FDM Group and 1
john_smith.print_instance_attr()                    # prints 'London' and 'John Smith'
# print its namespace
print(john_smith.__dict__)  # prints {'academy': 'London', 'trainee_name': 'John Smith'}
# create the 2nd trainee
ana_rogers = Trainee('London', 'Ana Rogers')
# print the values of its class and instance attributes
ana_rogers.print_class_attr_from_instance_method()  # prints FDM Group and 2
ana_rogers.print_instance_attr()                    # prints 'London' and 'Ana Rogers'
# print its namespace
print(ana_rogers.__dict__)  # prints {'academy': 'London', 'trainee_name': 'Ana Rogers'}
# create the 3rd trainee
pat_larson = Trainee('Leeds', 'Pat Larson')
# print the values of its class and instance attributes
pat_larson.print_class_attr_from_instance_method()  # prints FDM Group and 3
pat_larson.print_instance_attr()                    # prints 'Leeds' and 'Pat Larson'
# print its namespace
print(pat_larson.__dict__)  # prints {'academy': 'Leeds', 'trainee_name': 'Pat Larson'}
# delete John Smith
del john_smith
# print the class attributes using the class
Trainee.print_class_attr_from_class_method()        # prints FDM Group and 2
pat_larson.print_class_attr_from_instance_method()


# Question 3
# ----------
'''
Create a set of classes as depicted by the UML diagram below
a) All methods that don't return values should simply print
   out a message containing the name of the method and the
   value of its argument(s).
b) The read_data method returns a String. The String should
   contain a simple message like: "reading data from "+file.
c) Ensure that attributes shown in upper case are read-only
   instances attributes.
d) Use the Python property decorators to get and set all
   attributes
e) Create a constructor for each class. Ensure that it only
   initialises the attributes shown in the UML.
'''
# Question 3
# ----------
print('--- Q3: HardDrive ---')
class HardDrive:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
        
    # getter function for model
    @property
    def model(self):
        print('Getting model:')
        return self.__model
    
    # setter function for model
    @model.setter
    def model(self, value):
        # if object has '_HardDrive__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_HardDrive__model'):  # <=> if '_HardDrive__model' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: model")
        else:
            print('Setting model to', value)
            self.__model = value
        
    # deleter function for model
    @model.deleter
    def model(self):
        print('Deleting model:', self.__model)
        del self.__model

    # getter function for capacity
    @property
    def capacity(self):
        print('Getting capacity:')
        return self.__capacity
    
    # setter function for capacity
    @capacity.setter
    def capacity(self, value):
        # if object has '_HardDrive__capacity' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_HardDrive__capacity'):  # <=> if '_HardDrive__capacity' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: capacity")
        else:
            print('Setting capacity to', value)
            self.__capacity = value
        
    # deleter function for capacity
    @capacity.deleter
    def capacity(self):
        print('Deleting capacity:', self.__capacity)
        del self.__capacity

    # instance methods
    def set_used_space(self, used_space):
        self.used_space = used_space

    def read_data(self, file):
        print('read_data: reading data from', file)

    def write_data(self, file):
        print('write_data: writing data to', file)

# client code to test HardDrive class
# create HardDrive object (calling the setter)
hd = HardDrive('Seagate', 2048)  # prints Setting model to Seagate and Setting capacity to 2048 before initialising private instance attributes model and capacity
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_HardDrive__capacity': 2048}
print(HardDrive.__dict__)        # lists 'model', 'capacity' properties, and __doc__
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# calls the setter
hd.model = 'WD'                  # prints 'Attempting to alter read-only attribute: model'
hd.capacity = 3072               # prints 'Attempting to alter read-only attribute: capacity'
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_HardDrive__capacity': 2048}
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# execute the instance methods
hd.set_used_space(0)             # sets the public instance attribute used_space to 0
print(hd.used_space)             # prints 0
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_HardDrive__capacity': 2048, 'used_space': 0}
hd.read_data('readable_file.txt')   # prints 'read_data: reading data from readable_file.txt'
hd.write_data('writable_file.txt')  # prints 'write_data: writing data to writable_file.txt'
# set the docstring
HardDrive.model.__doc__ = 'name of the hard disk model'
HardDrive.capacity.__doc__ = 'hard disk capacity'
# display the docstring
print('Docstring:', HardDrive.model.__doc__)    # prints Docstring: name of the hard disk model
print('Docstring:', HardDrive.capacity.__doc__) # prints Docstring: hard disk capacity
# calls the deleter
del hd.model                     # prints Deleting model: Seagate
print(hd.__dict__)               # prints {'_HardDrive__capacity': 2048, 'used_space': 0}
del hd.capacity                  # prints Deleting capacity: 2048
print(hd.__dict__)               # prints {'used_space': 0}
del hd.used_space
print(hd.__dict__)               # prints {}
print(HardDrive.__dict__)        # lists 'model' and 'capacity' properties, and '__doc__'

print('--- Q3: Memory ---')
class Memory:
    def __init__(self, model, capacity, speed):
        self.model = model
        self.capacity = capacity
        self.speed = speed
        
    # getter function for model
    @property
    def model(self):
        print('Getting model:')
        return self.__model
    
    # setter function for model
    @model.setter
    def model(self, value):
        # if object has '_Memory__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__model'):  # <=> if '_Memory__model' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: model")
        else:
            print('Setting model to', value)
            self.__model = value
        
    # deleter function for model
    @model.deleter
    def model(self):
        print('Deleting model:', self.__model)
        del self.__model

    # getter function for capacity
    @property
    def capacity(self):
        print('Getting capacity:')
        return self.__capacity
    
    # setter function for capacity
    @capacity.setter
    def capacity(self, value):
        # if object has '_Memory__capacity' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__capacity'):  # <=> if '_Memory__capacity' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: capacity")
        else:
            print('Setting capacity to', value)
            self.__capacity = value
        
    # deleter function for capacity
    @capacity.deleter
    def capacity(self):
        print('Deleting capacity:', self.__capacity)
        del self.__capacity

    # getter function for speed
    @property
    def speed(self):
        print('Getting speed:')
        return self.__speed
    
    # setter function for speed
    @speed.setter
    def speed(self, value):
        # if object has '_Memory__speed' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__speed'):  # <=> if '_Memory__speed' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: speed")
        else:
            print('Setting speed to', value)
            self.__speed = value
        
    # deleter function for speed
    @speed.deleter
    def speed(self):
        print('Deleting speed:', self.__speed)
        del self.__speed

    # instance methods
    def set_used_space(self, used_space):
        self.used_space = used_space

    def store_data(self, data):
        print('store_data: storing data:', data)

# client code to test Memory class
# create Memory object (calling the setter)
memory = Memory('Kingston', 4, 1600)  # prints Setting model to Kingston, Setting capacity to 4 and Setting speed to 1600 before initialising private instance attributes model, capacity and speed
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Memory__capacity': 4, '_Memory__speed': 1600}
print(Memory.__dict__)                # lists 'model', 'capacity' and 'speed' properties, and __doc__
# calls the getter
print(memory.model)                   # prints Getting model: Kingston
print(memory.capacity)                # prints Getting capacity: 4
print(memory.speed)                   # prints Getting speed: 1600
# calls the setter
memory.model = 'Corsair'              # prints 'Attempting to alter read-only attribute: model'
memory.capacity = 8                   # prints 'Attempting to alter read-only attribute: capacity'
memory.speed = 1333                   # prints 'Attempting to alter read-only attribute: speed'
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Memory__capacity': 4, '_Memory__speed': 1600}
# calls the getter
print(memory.model)                  # prints Getting model: Kingston
print(memory.capacity)               # prints Getting capacity: 4
print(memory.speed)                  # prints Getting speed: 1600
# execute the instance methods
memory.set_used_space(0.5)           # sets the public instance attribute used_space to 0.5
print(memory.used_space)             # prints 0.5
print(memory.__dict__)               # prints {'_Memory__model': 'Kingston', '_Memory__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
memory.store_data('data_to_store')   # prints 'store_data: storing data: data_to_store'
# set the docstring
Memory.model.__doc__ = 'name of the memory model'
Memory.capacity.__doc__ = 'memory capacity'
Memory.speed.__doc__ = 'memory speed'
# display the docstring
print('Docstring:', Memory.model.__doc__)    # prints Docstring: name of the memory model
print('Docstring:', Memory.capacity.__doc__) # prints Docstring: memory capacity
print('Docstring:', Memory.speed.__doc__)    # prints Docstring: memory speed
# calls the deleter
del memory.model                     # prints Deleting model: Kingston
print(memory.__dict__)               # prints {'_Memory__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
del memory.capacity                  # prints Deleting capacity: 4
print(memory.__dict__)               # prints {'_Memory__speed': 1600, 'used_space': 0.5}
del memory.speed                     # prints Deleting speed: 1600
print(memory.__dict__)               # prints {'used_space': 0.5}
del memory.used_space
print(memory.__dict__)               # prints {}
print(Memory.__dict__)               # lists 'model', 'capacity' and 'speed' properties, and __doc__



# Question 4
# ----------
'''
Write a Python class which has two methods get_string() and
print_string(). get_string() accepts a string from the user
and print_string() prints the string in 'proper' case
(the first character of each word of the string is upper
case and the rest of the characters are lower case).
Example:
'tHiS iS My UNTIDY string' -> This Is My Untidy String
'''
print('--- Q4 ---')
class IOString():
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input('Enter a string: ')

    def print_string(self):
        # create a list of words in the string
        words = self.string.split()
        # capitalise each word and append it to the 'proper' string
        proper_string = ''
        for word in words:
            proper_string += word.capitalize() + ' '
        # return the string in 'proper' case without the trailing space
        print(proper_string.rstrip())

str1 = IOString()
str1.get_string()
str1.print_string()


# Question 5
# ----------
'''
Write a Python class named Circle consisting of an instance
attribute radius and two methods which will compute the area
and the perimeter of a circle.
Note: import and use the constant pi from the math module.
'''
print('--- Q5 ---')
from math import pi
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius ** 2 * pi, 2)
    
    def perimeter(self):
        return round(2 * self.radius * pi, 2)

circle = Circle(7)
print(circle.area())      # prints 153.94
print(circle.perimeter()) # prints 43.98



# Question 6
# ----------
'''
a) Write a Python class for the 'Tesla' car manufacturer.
  It needs to include the following:
  - 2 class attributes: MAKE (a constant set to 'Tesla')
    and condition, set to value 'new' (by default a car is new)
  - 4 instance variables: model, fuel, max_speed, colour
  - 4 methods: the constructor, drive_car() - which sets the object's
    condition to 'used', change_colour() - which changes the colour
    of the car and display() - which prints all car details, using
    this format:
    This is a silver Tesla 3 electric with max speed of 140 mph. Condition: new.
  Once the class has been created, write the client code to do
  the following:
  - create a car object as make: 3, fuel: electric, max_speed: 140, colour: "silver"
  - display the Car class namespace and the namespace of the Car's object (using the __dict__ attribute)
  - execute the object's display() method
  - execute the object's drive_car() method
  - print the value of class attribute condition from the Car's object
  - print the value of class attribute condition from the Car class
  - Explain why the attribute condition of the car object is 'used' but the 
    attribute condition of the Car class remains 'new' (you may want to
    display the namespace of the Car's object to help you answer the question)

  - create another car object as make: X, fuel: petrol, max_speed: 200, colour: "red"
  - execute the object's display() method
  - print the value of class attribute condition from the Car's object
  - print the value of class attribute condition from the Car class
  
b) improve the class Car by preventing users to change the class attribute MAKE
   through an object of class Car in the client code
'''
# https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/content/exercise_car/car.html

# 1st version
print('--- Q6a 1st version ---')
# Two class attributes: the constant MAKE and variable condition
# set as 'Tesla' and 'new' respectively.
# The instance method drive_car() creates a new instance variable
# condition and sets it to 'used'. The class variable condition
# co-exists and remains unchanged.
class Car(object):
    # class attributes
    MAKE = 'Tesla'
    condition = 'new'
    
    # class constructor
    def __init__(self, model, fuel, max_speed, colour):
        self.model = model # 3 (140), S(160), X (200), Y (220) 
        self.fuel = fuel
        self.max_speed = max_speed
        self.colour = colour
        
    # instance methods
    def drive_car(self):
        self.condition = 'used'

    def change_colour(self, colour):
        self.colour = colour

    def display(self):
      print('This is a %s %s %s %s with max speed of %d mph. Condition: %s.' % (self.colour, self.MAKE, self.model, self.fuel, self.max_speed, self.condition))


car1 = Car('3', 'electric', 140, 'silver')
print(Car.__dict__)   # includes 'MAKE': 'Tesla', 'condition': 'new'
print(car1.__dict__)  # prints {'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver'}
car1.display()        # prints: This is a silver Tesla 3 electric with max speed of 140 mph. Condition: new
car1.drive_car()      # sets class attribute condition to 'used'
car1.display()        # prints: This is a silver Tesla 3 electric with max speed of 140 mph. Condition: used
print(car1.condition) # prints 'used'
print(Car.condition)  # prints 'new'
print(car1.__dict__)  # prints {'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'used'}
# an attempt to change the class constant MAKE from the object
# will result in creating a new instance constant MAKE set to 'dummy'
# the class constant MAKE will co-exist and remain unchanged
car1.MAKE = 'dummy'   # creates new instance attribute MAKE and sets it to 'dummy', leaving the class attribute 'MAKE unchanged
print(Car.__dict__)   # includes 'MAKE': 'Tesla', 'condition': 'new'
print(car1.__dict__)  # prints {'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'used', 'MAKE': 'dummy'}

car2 = Car('X', 'petrol', 200, 'black')
car2.display()        # prints: This is a black Tesla X petrol with max speed of 200 mph. Condition: new
print(car2.condition) # prints 'new'
print(Car.condition)  # prints 'new'
print(car2.__dict__)  # prints {'model': 'X', 'fuel': 'petrol', 'max_speed': 200, 'colour': 'black'}

# improvement to protect the class constant MAKE
print('--- Q6b 1st version ---')
class Car(object):
    # class attributes
    _MAKE = 'Tesla'
    condition = 'new'
    
    # class constructor
    def __init__(self, model, fuel, max_speed, colour):
        self.model = model # 3 (140), S(160), X (200), Y (220) 
        self.fuel = fuel
        self.max_speed = max_speed
        self.colour = colour
        
    @property
    def MAKE(self):
        return self.__class__._MAKE

    @MAKE.setter
    def MAKE(self, new_value):
        # print message as MAKE cannot be changed
        print("MAKE is defined as a constant and cannot be modified")

    # instance methods
    def drive_car(self):
        self.condition = 'used'

    def change_colour(self, colour):
        self.colour = colour

    def display(self):
      print('This is a %s %s %s %s with max speed of %d mph. Condition: %s.' % (self.colour, self.MAKE, self.model, self.fuel, self.max_speed, self.condition))


# now users are not able to change the value of class constant
# MAKE from the object
car1 = Car('3', 'electric', 140, 'silver')
car1.MAKE = 'dummy'   # prints 'MAKE is defined as a constant and cannot be modified'
print(Car.__dict__)   # includes 'MAKE': 'Tesla', 'condition': 'new'
print(car1.__dict__)  # prints {'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver'}

# 2nd version
print('--- Q6a - 2nd version ---')
# No class attributes; MAKE and condition are implemented as
# instance attributes with values 'Tesla' and 'new' assigned
# in the class constructor.
# As before, the instance method drive_car() changes the value
# of instance variable condition to 'used'
class Car(object):
    # class constructor
    def __init__(self, model, fuel, max_speed, colour):
        self.MAKE = 'Tesla'
        self.model = model # 3 (140), S(160), X (200), Y (220) 
        self.fuel = fuel
        self.max_speed = max_speed
        self.colour = colour
        self.condition = 'new'

    # instance methods
    def drive_car(self):
        self.condition = 'used'

    def change_colour(self, colour):
        self.colour = colour

    def display(self):
      print('This is a %s %s %s %s with max speed of %d mph. Condition: %s.' % (self.colour, self.MAKE, self.model, self.fuel, self.max_speed, self.condition))


car1 = Car('3', 'electric', 140, 'silver')
print(Car.__dict__)   # no class attributes listed
print(car1.__dict__)  # prints {'MAKE': 'Tesla', 'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'new'}
car1.display()        # prints: This is a silver Tesla 3 electric with max speed of 140 mph. Condition: new
car1.drive_car()      # sets class attribute condition to 'used'
car1.display()        # prints: This is a silver Tesla 3 electric with max speed of 140 mph. Condition: used
print(car1.condition) # prints 'used'
print(car1.__dict__)  # prints {'MAKE': 'Tesla', 'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'used'}
# users can now change the instance attribute MAKE
# from the object
car1.MAKE = 'dummy'
print(car1.__dict__)  # prints {'MAKE': 'dummy', 'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'used'}

car2 = Car('X', 'petrol', 200, 'black')
car2.display()        # prints: This is a black Tesla X petrol with max speed of 200 mph. Condition: new
print(car2.condition) # prints 'new'
print(car2.__dict__)  # prints {'MAKE': 'Tesla', 'model': 'X', 'fuel': 'petrol', 'max_speed': 200, 'colour': 'black', 'condition': 'new'}


# improvement to protect the instance constant MAKE
print('--- Q6b 2nd version ---')
class Car(object):
    # class constructor
    def __init__(self, model, fuel, max_speed, colour):
        # the name of the instance attribute in the constructor
        # must be different from the property name: MAKE, as in
        # this case constructor should not invoke the setter 
        self._MAKE = 'Tesla'
        self.model = model # 3 (140), S(160), X (200), Y (220) 
        self.fuel = fuel
        self.max_speed = max_speed
        self.colour = colour
        self.condition = 'new'

    @property
    def MAKE(self):
        print('Getting value...')
        return self._MAKE

    @MAKE.setter
    def MAKE(self, MAKE):
        # print message as MAKE cannot be changed
        print("MAKE is defined as a constant and cannot be modified")

    # instance methods
    def drive_car(self):
        self.condition = 'used'

    def change_colour(self, colour):
        self.colour = colour

    def display(self):
      print('This is a %s %s %s %s with max speed of %d mph. Condition: %s.' % (self.colour, self.MAKE, self.model, self.fuel, self.max_speed, self.condition))

# now users are not able to change the value of
# instance constant MAKE from the object
car1 = Car('3', 'electric', 140, 'silver') # no message printed as constructor does not invoke the setter
print(car1.__dict__)  # prints {'_MAKE': 'Tesla', 'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'new'}
car1.MAKE = 'dummy'   # prints 'MAKE is defined as a constant and cannot be modified'
print(car1.MAKE)      # prints Getting value... Tesla
print(car1.__dict__)  # prints {'_MAKE': 'Tesla', 'model': '3', 'fuel': 'electric', 'max_speed': 140, 'colour': 'silver', 'condition': 'new'}



# Question 7
# ----------
'''
Write a Python class to convert a positive integer to the
equivalent roman numeral. The roman numerals and their
corresponding decimal values are given below:
M:1000, CM:900, D:500, CD: 400, C:100, XC:90,
L:50, XL:40, X:10, IX:9, V:5, IV:4, I:1
Examples:
8 -> VIII
54 -> LIV
100 -> C
153 -> CLIII
2022 -> MMXXII
4000 -> MMMM
'''
print('--- Q7 ---')
class Convert:
    @staticmethod
    def int_to_roman(integer):
        # store the roman symbols in a list
        symbols = ["M", "CM", "D", "CD",
                   "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]
        # and their corresponding values in another list
        values = [1000, 900, 500, 400,
                   100, 90, 50, 40,
                    10, 9, 5, 4, 1]
        # initialise the variable to store the roman numeral
        roman_numeral = ''
        # initialise the starting list index
        i = 0
        # repeat until the whole integer has been converted
        while  integer > 0:
            # find the first symbol whose corresponding value
            # is <= the integer; perform integer division to
            # obtain the number of times the symbol needs to
            # repeat
            for iteration in range(integer // values[i]):
                # concatenate the symbol symbols[i]
                # integer // values[i] times and reduce the
                # integer by the corresponding value values[i]
                roman_numeral += symbols[i]
                integer -= values[i]
            # take the next list index
            i += 1
        return roman_numeral

# client code
# static methods can be called directly from the class
print(Convert.int_to_roman(8))
print(Convert.int_to_roman(19))
print(Convert.int_to_roman(54))
print(Convert.int_to_roman(100))
print(Convert.int_to_roman(153))
print(Convert.int_to_roman(2022))
print(Convert.int_to_roman(4000))
print(Convert.int_to_roman(7689))
print(Convert.int_to_roman(12345))



# Question 8
# ----------
'''
Write a Python class to convert a roman numeral to the
equivalent integer value.
Examples:
VIII -> 8
XIX -> 19
XXXIX -> 39
XLIV -> 44
LIV -> 54
C -> 100
CLIII -> 153
CM -> 900
MMXXII -> 2022
MMMM -> 4000
'''
print('--- Q8 - 1st version ---')
# version 1 ('pedestrian')
class Convert:
    @staticmethod
    def roman_to_int(roman_numeral):
        # store the roman symbols and the corresponding integer
        # value in a dictionary (to avoid searching for the
        # symbol through the list)
        sym_int = {"M":1000, "CM":900, "D":500, "CD":400,
                   "C":100, "XC":90, "L":50, "XL":40,
                   "X":10, "IX":9, "V":5, "IV":4, "I":1}
        # if there is only one symbol return its value
        if len(roman_numeral) == 1:
            return sym_int[roman_numeral[0]]
        # initialise the variable to store the integer
        # the variable to store the index
        integer = 0
        index = 0
        # compare pairs of adjacent symbols
        while index < len(roman_numeral)-1:
            # if the value of first symbol is less than value of
            # the second symbol (case of CM, CD, XC, XL, IX or IV)
            if sym_int[roman_numeral[index]] < sym_int[roman_numeral[index+1]]:
                # add value of second symbol reduced by value of first symbol
                integer += sym_int[roman_numeral[index+1]] - sym_int[roman_numeral[index]]
                index += 2
            else:
                # if the last two characters are being compared
                if index == len(roman_numeral)-2:
                    # add values of both symbols
                    integer += sym_int[roman_numeral[index]] + sym_int[roman_numeral[index+1]]
                    index += 2
                else:
                    # otherwise add value of the current symbol
                    integer += sym_int[roman_numeral[index]]
                    index += 1
        # convert the last symbol if it wasn't converted
        if index == len(roman_numeral)-1:
            integer += sym_int[roman_numeral[index]]
        return integer

# client code
print(Convert.roman_to_int('VIII'))
print(Convert.roman_to_int('XIX'))
print(Convert.roman_to_int('XXXIX'))
print(Convert.roman_to_int('XLIV'))
print(Convert.roman_to_int('LIV'))
print(Convert.roman_to_int('C'))
print(Convert.roman_to_int('CLIII'))
print(Convert.roman_to_int('CM'))
print(Convert.roman_to_int('MMXXII'))
print(Convert.roman_to_int('MMMM'))
print(Convert.roman_to_int('MMMMMMMDCLXXXIX'))
print(Convert.roman_to_int('MMMMMMMMMMMMCCCXLV'))


print('--- Q8 - 2nd version ---')
# version 2 - realising that in case of any of the 2-digit
# symbols (CM, CD, XC, XL, IX or IV) the value of the first
# symbol 
# 1) is C, X or I (which are already existing as symbols)
# 2) was added in the previous iteration - hence it must
# be subtracted twice in the current iteration (once because
# it comes before the 2nd symbol and the 2nd time because
# it was already added in the previous iteration)
class Convert:
    @staticmethod
    def roman_to_int(roman_numeral):
        sym_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for index in range(len(roman_numeral)):
            # if the value of first symbol is less than value of
            # the second symbol (case of CM, CD, XC, XL, IX or IV)
            if index > 0 and sym_int[roman_numeral[index-1]] < sym_int[roman_numeral[index]]:
                # add value of second symbol reduced by value of first symbol
                # and reduced again by value of first symbol (added in prev. iteration)
                integer += sym_int[roman_numeral[index]] - 2 * sym_int[roman_numeral[index-1]]
            else:
                # index == 0 or sym_int[roman_numeral[index-1]] >= sym_int[roman_numeral[index]]
                integer += sym_int[roman_numeral[index]]
        return integer

# client code
print(Convert.roman_to_int('VIII'))
print(Convert.roman_to_int('XIX'))
print(Convert.roman_to_int('XXXIX'))
print(Convert.roman_to_int('XLIV'))
print(Convert.roman_to_int('LIV'))
print(Convert.roman_to_int('C'))
print(Convert.roman_to_int('CLIII'))
print(Convert.roman_to_int('CM'))
print(Convert.roman_to_int('MMXXII'))
print(Convert.roman_to_int('MMMM'))
print(Convert.roman_to_int('MMMMMMMDCLXXXIX'))
print(Convert.roman_to_int('MMMMMMMMMMMMCCCXLV'))


            
