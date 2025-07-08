##############################
# Module 2A - Python Classes #
##############################

# slide 10
class Trainee:
    # class attributes
    name = None
    courses = {}
    
    # instance methods
    def assign_course(self, course):
        self.courses[course] = 0
        return

# client code
print("type(Trainee) =", type(Trainee))      # prints <class 'type'>

# create an object of class Trainee
trainee = Trainee()
print(type(trainee))                         # prints <class '__main__.Trainee'>
print(type(trainee).__name__)                # prints 'Trainee'
print(trainee.__class__.__name__)            # prints 'Trainee'
print("trainee.name =", trainee.name)        # prints trainee.name = None
print("trainee.courses =", trainee.courses)  # prints trainee.courses = {}

trainee.name = 'John'
trainee.assign_course('SQL')
print("trainee.name =", trainee.name)        # prints trainee.name = John
print("trainee.courses =", trainee.courses)  # prints trainee.courses = {'SQL': 0}


# slide 13
# the class above is the same (equivalent) as this one:
class Trainee:
    # class attributes
    name = None
    courses = {}
    
    # constructor
    def __init__(self):
        pass
    # instance methods
    def assign_course(self, course):
        self.courses[course] = 0
        return

# client code
trainee = Trainee()
print(type(trainee))                           # prints <class '__main__.Trainee'>
print("trainee.name =", trainee.name)          # prints trainee.name = None
print("trainee.courses =", trainee.courses)    # prints trainee.courses = {'SQL': 0}

trainee.name = 'John'
trainee.assign_course('SQL')
print("trainee.name =", trainee.name)          # prints trainee.name = John
print("trainee.courses =", trainee.courses)    # prints trainee.courses = {'SQL': 0}

# customising the class constructor:
class Trainee:
    # class attributes
    name = None
    courses = {}
    
    # constructor (an instance method)
    def __init__(self, name, courses):
        # instance attributes
        self.name = name
        self.courses = courses

# client code
'''
- dir(object_name>) lists ALL ATTRIBUTES and methods available for the object <object_name>
- dir(class_name>) lists all attributes and methods available for the class <class_name>
Class.__dict__: applied to a class, __dict__ attribute displays all of its methods and any class attributes
                you define as part of it, in form of a dictionary.
object.__dict__: when appplied to an object, __dict__ attribute lists all
                 INSTANCE ATTRIBUTES to which a value has been assigned, as
(key,value) pairs. 

'''
print(Trainee.__dict__)         # lists (class) variables 'name': None, 'courses': {}
trainee = Trainee('Julia', {})  
print(trainee.__dict__)         # prints {'name': 'Julia', 'courses': {}} (instance attributes)
print(Trainee.__dict__)         # lists (class) 'name': None, 'courses': {}
print("trainee.name =", trainee.name)        # prints trainee.name = Julia
print("trainee.courses =", trainee.courses)  # prints trainee.courses = {}
print(trainee.__dict__)         # prints {'name': 'Julia', 'courses': {}} (instance attributes)
print(dir(trainee))             # lists 'courses', 'name'

trainee2 = Trainee('Mark', {})
print(trainee2.__dict__)   # prints {'name': 'Mark', 'courses': {}}  (lists instance attributes only)
print(dir(trainee2))       # lists all attributes and methods vailable to the object (lists 'courses', 'name')


# slide 14
class Trainee:  
    # class constructor - initialises instance attributes
    def __init__(self, name, stream, weeks, courses):
        self.name = name
        self.stream = stream
        self.weeks = weeks
        self.courses = courses

    # instance methods   
    def assign_course(self, course):
        self.courses[course] = 0
        return 

    def assign_mark_for_course(self, course, mark):
        pass

# client code:
trainee_julia = Trainee('Julia', 'DE', 6, {})
trainee_mark = Trainee('Mark', 'DE', 6, {})
print("trainee_julia.__dict__:\n", trainee_julia.__dict__)
print("trainee_mark.__dict__:\n", trainee_mark.__dict__)
trainee_julia.assign_course('SQL')
trainee_mark.assign_course('Python')
print("trainee_julia.__dict__:\n", trainee_julia.__dict__)
print("trainee_mark.__dict__:\n", trainee_mark.__dict__)


# slide 15
class Trainee:
    # class attributes
    courses = {}  # class variable (shared by all instances)
    
    # class constructor - initialises instance attributes
    def __init__(self, name):
        self.name = name  # instance variable (unique to each instance)
     # instance methods
    def assign_course(self, course):
        self.courses[course] = 0


# client code
trainee_Lucy = Trainee('Lucy')
print(trainee_Lucy.__dict__)
trainee_Lucy.assign_course('SQL')
print(trainee_Lucy.__dict__)  
print(trainee_Lucy.courses)  # {'SQL': 0}
print(dir(trainee_Lucy))

trainee_Sam = Trainee('Sam')
print(trainee_Sam.__dict__)
trainee_Sam.assign_course('Java')
print(trainee_Sam.__dict__)  
print(trainee_Sam.courses)   # {'SQL': 0, 'Java': 0} instead of {'Java': 0}
print(dir(trainee_Sam))
print(trainee_Lucy.courses)  # {'SQL': 0, 'Java': 0} instead of {'SQL': 0}


# slide 17 - correct implementation
class Trainee:
    # class attributes
    
    # class constructor - initialises instance attributes
    def __init__(self, name):
        self.name = name  # instance variable (unique to each instance)
        self.courses = {} # instance variable (unique to each instance)

    # instance methods
    def assign_course(self, course):
        self.courses[course] = 0

# client code
trainee_Lucy = Trainee('Lucy')
print(trainee_Lucy.__dict__)  # {'name': 'Lucy', 'courses': {}}
trainee_Lucy.assign_course('SQL')
print(trainee_Lucy.__dict__)  # {'name': 'Lucy', 'courses': {'SQL': 0}}
print(trainee_Lucy.courses)
print(dir(trainee_Lucy))

trainee_Sam = Trainee('Sam')
print(trainee_Sam.__dict__)  # {'name': 'Sam', 'courses': {}}
trainee_Sam.assign_course('Java')
print(trainee_Sam.__dict__)  # {'name': 'Sam', 'courses': {'Java': 0}}
print(trainee_Sam.courses)
print(dir(trainee_Sam))
print(trainee_Lucy.courses)  # {'SQL': 0}


# slide 22
# in Python there is no variable declaration
a = 1      # assigning a value to a variable creates the variable
a = 'one'

# the same applies to classes and objects
class Rectangle():
    pass

# client code:
rect_obj1 = Rectangle()
# assigning a variable name and value to a class creates the class attribute:
Rectangle.colour = 'blue' # adds a class atribute 'colour': 'blue'
print(Rectangle.__dict__)
# assigning a variable name and value to an object creates the instance attribute:
rect_obj1.height = 2      # adds height: 2 as instance attribute
rect_obj1.width = 3       # adds width:3 as instance attribute
print(rect_obj1.height)  
print(rect_obj1.width)   
print(rect_obj1.__dict__)  # prints {'height': 2, 'width': 3}

rect_obj2 = Rectangle()
#print(rect_obj2.height)  # throws AttributeError: 'Rectangle' object has no attribute 'height'


# slide 24
# proper way of defining instance attributes (within the class constructor or an instance method)
class Learner:
    # class constructor - initialises instance attributes
    def __init__(self, name, courses):
        self.name = name       # instance variable (unique to each instance)
        self.courses = courses # creates a new dictionary (unique for each learner)
        
    # instance methods
    def set_weeks(self, weeks):
        self.weeks = weeks    # initialises instance variable weeks (unique for each learner)
        return
    
    def assign_course(self, course):
        self.courses[course] = 0
        return

# client code:
learner_Ema = Learner('Ema', {})
print(learner_Ema.__dict__)  # {'name': 'Ema', 'courses': {}}
print(dir(learner_Ema))
learner_Ema.set_weeks(6)
print(dir(learner_Ema))
print(learner_Ema.__dict__)  # {'name': 'Ema', 'courses': {}, 'weeks': 6}
print(Learner.__dict__)      # lists class atributes (does not list any)


# slide 26
# example illustrating setting up instance attributes through
# instance methods (instead of through a constructor)
class Student:
    # class methods
    def assign_name(self, name):
        self.name = name
        return
    def create_courses(self):
        self.courses = {}
        return
    def assign_course(self, course):
        self.courses[course] = 0


# slides 31-37
class Trainee: 
    # class attributes
    count = 0    # instance counter (shared by all instances) 
    
    # class constructor                         
    def __init__(self, name, stream, weeks, courses):
        self.name = name
        self.stream = stream
        self.weeks = weeks            # instance attributes
        self.courses = courses
        self.__class__.count += 1     # <=> Trainee.count += 1 <=> type(self).count += 1

    # instance methods  
    def assign_course(self, course):  # course is a method parameter variable
        self.courses[course] = 0      # courses is an instance attribute

    def assign_mark_for_course(self, course, mark): 
        if course in self.courses:       # courses is an instance attribute
            self.courses[course] = mark  # course & mark are method parameters

    def avg_mark(self): 
        total_marks = 0                     # total_marks is a local method variable
        for mark in self.courses.values():  # courses is an instance attribute
            total_marks += mark             # mark is a local method variable
        return total_marks / len(self.courses.values())

    def print_count(self):
        print('self.count =', self.count)  # object's class attribute count
        print('self.__class__.count =', self.__class__.count)  # class's class attribute count
        
    # class destructor
    def __del__(self):
        self.__class__.count -= 1  # <=> Trainee.count -= 1 <=> type(self).count -= 1

# client code
print('Trainee.count = ', Trainee.count)  # prints Trainee.count = 0
# create the object trainee1 from class Trainee
trainee1 = Trainee("John",
                   "Development",
                   6,
                   {'SQL':75, 'UNIX':78, 'Python':94,
                    'Java':81, 'Web Apps':100, 'Excel':90}
                   )

print(dir(trainee1))  # lists all attributes and methods available for the object trainee1
print(trainee1.__dict__) # {'name': 'John', 'stream': 'Development', 'weeks': 6, 'courses': {'SQL': 75, 'UNIX': 78, 'Python': 94, 'Java': 81, 'Web Apps': 100, 'Excel': 90}}
# class's class attribute 'count' is accessible from the class:
print("Trainee.count =", Trainee.count)   # prints Trainee.count = 1
# object's class attribute 'count' is accessible from the object:
print("trainee1.count =", trainee1.count) # prints trainee1.count = 1
# both class's and object's class attribute 'count' are accessible from the print_count() instance method:
trainee1.print_count()  # prints self.count = 1 & self.__class__.count = 1
print("trainee1.avg_mark():", trainee1.avg_mark())  # prints trainee1.avg_mark(): 86.33333333333333

trainee2 = Trainee("Ana",
                   "Development",
                   6,
                   {'SQL':85, 'UNIX':75, 'Python':77,
                    'Java':80, 'Web Apps':90}
                   )
print(trainee2.__dict__)  # {'name': 'Ana', 'stream': 'Development', 'weeks': 6, 'courses': {'SQL': 85, 'UNIX': 75, 'Python': 77, 'Java': 80, 'Web Apps': 90}}
print('before deleting trainee2:')
print("Trainee.count =", Trainee.count)  # Trainee.count = 2
# to remove (delete) an object use the del keyword to invoke the class destructor
del trainee2
print('after deleting trainee2:')
print("Trainee.count =", Trainee.count)  # Trainee.count = 1
del trainee1
print('after deleting trainee1:')
print("Trainee.count =", Trainee.count)  # Trainee.count = 0


# slides 40-41
trainee3 = Trainee('Keith',
                   'Development',
                   6,
                   {'SQL':77, 'UNIX':78, 'Python':90, 
                    'Java':82, 'Web Apps':88, 'Excel':95}
                   )
# access attributes of trainee3
print('trainee3 name:', trainee3.name)       # trainee3 name: Keith
print('trainee3 stream:', trainee3.stream)   # trainee3 stream: Development
print('trainee3 weeks:', trainee3.weeks)     # trainee3 weeks: 6
print('trainee3 courses:', trainee3.courses) # trainee3 courses: {'SQL’: 77, 'UNIX': 78, 'Python’: 90, 'Java’: 82, 'Web Apps’: 88, 'Excel’: 95}
# call methods of trainee3
print('trainee3 average mark:', trainee3.avg_mark()) # trainee3 average mark: 85.0
trainee3.print_count()  # self.count = 1 & self.__class__.count = 1


# slides 42-43
trainee4 = Trainee('Sarah',
                   'Development',
                   6,
                   {}
                   )
# access attributes of trainee4
print('trainee4 name:', trainee4.name)      # trainee4 name: Sarah
print('trainee4 stream:', trainee4.stream)  # trainee4 stream: Development
print('trainee4 weeks:', trainee4.weeks)    # trainee4 weeks: 6
# call methods of trainee4
trainee4.assign_course('SQL')
trainee4.assign_course('Python')
trainee4.assign_mark_for_course('SQL', 90)
trainee4.assign_mark_for_course('Python', 82)
print('trainee4 average mark:', trainee4.avg_mark())  # trainee4 average mark: 86.0
trainee4.print_count()  # self.count = 2 & self.__class__.count = 2


# slides 44-45
trainee1 = Trainee('John',
                   'Development',
                   6,
                   {}
                   )
trainee1_second_ref = trainee1
trainees_list = []
trainees_list.append(trainee1)
print('trainee1           :', trainee1)
print('trainee1_second_ref:', trainee1_second_ref)
print('trainees_list[0]   :', trainees_list[0])
# modifying a value of an attribute of the object
# will be refelcted in all references to the same object
trainees_list[0].name = trainees_list[0].name + ' Smith'
print('trainee1           :', trainee1.name)
print('trainee1_second_ref:', trainee1_second_ref.name)
print('trainees_list[0]   :', trainees_list[0].name)


# slide 48
class Car:
    def __init__(self):
        pass

car = Car()
print('memory address of car object is:', car)


# slide 49
class Car:
    def __init__(self):
        print("self printed from inside the class is:", self)

car = Car()
print('memory address of car object is:', car)


# slide 50
class Car:
    def move(self):
        print('the car is moving')
   
car = Car()
car.move()


# slide 51
class Car:
    def move(self):
        print('the car is moving')
    
class CarValet:
    def valet_car(self, car):  # valet_car() method expects an object 'car'
        car.move()

car = Car()
car_valet = CarValet()
car_valet.valet_car(car)


# slide 52
class Car:
    def move(self):
        print('the car is moving')

    def move_me(self, valet):
        valet.valet_car(self)
    
class CarValet:
    def valet_car(self, car):
        car.move()

car = Car()
car_valet = CarValet()
car.move_me(car_valet)


# slides 60-70 explain the mechanism behind Python properties
# These slides are for information only. 
# The final example on slide 71 illustrates the implementation
# of properties through decorators to implement getters, setters
# and deleters in Python.


# slide 71
class Student:
    def __init__(self, value):
        self.name = value
    # getter function
    @property
    def name(self):
        print('Getting name:')
        return self.__name
    # setter function
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        self.__name = value
    # deleter function
    @name.deleter
    def name(self):
        print('Deleting name')
        del self.__name

# client code
student_john = Student('John')
print("student_john.__dict__:\n", student_john.__dict__)
print("student_john.name =", student_john.name)


# slide 72 - example of real use of getters & setters
class Car:
    def __init__(self):
        self.speed = 0

    # Use of a 'decorator'
    # getting the value of the instance attribute speed
    @property
    def speed(self):
        print('Getting value...')
        return self._speed
    # setting the value for the instance attribute speed
    @speed.setter
    def speed(self, speed):
        if (speed > 80):
            print('this speed will damage the engine')
            return    
        print('Setting value...')
        self._speed = speed

    # deleting the instance attribute speed
    @speed.deleter 
    def speed(self): 
        print('Deleting attribute...')
        del self._speed

# client code
car = Car()
print(car.__dict__)
car.speed = 10
print(car.__dict__)
print(car.speed)
car.speed = 81
print(car.speed)
del car.speed
print(car.__dict__)

# additional example:
# In the above example the setter is invoked both from the
# constructor (when the object is being created) as well as
# whenever trying to change the speed directly by the object.
# To ensure the setter for an instance attribute is not
# invoked when the object is created, name the instance
# attribute with the 'real' name of the instance attribute.
# Note: assigning a value to that instance attribute from
# client code (outside the class) will still invoke the
# setter, getter & deleter.
class Car:
    def __init__(self):
        self._speed = 0

    # Use of a 'decorator'
    # getting the value of the instance attribute speed
    @property
    def speed(self):
        print('Getting value...')
        return self._speed

    # setting the value for the instance attribute speed
    @speed.setter
    def speed(self, speed):
        if (speed > 80):
            print('this speed will damage the engine')
            return    
        print('Setting value...')
        self._speed = speed

    # deleting the instance attribute speed
    @speed.deleter 
    def speed(self): 
        print('Deleting attribute...')
        del self._speed

# client code
car = Car()          # prints nothing (proving that the setter is not invoked)
print(car.__dict__)  # prints {'_speed': 0}
car.speed = 10       # prints 'Setting value...' and sets car.speed to 10 
print(car.speed)     # prints 'Getting value...' and 10 
print(car.__dict__)  # prints {'_speed': 10}
car.speed = 81       # prints this speed will damage the engine
print(car.speed)     # prints 'Getting value...' and 10 
print(car.__dict__)  # prints {'_speed': 10}
del car.speed        # prints 'Deleting attribute...'
print(car.__dict__)  # prints {}


# slide 76: class & static methods
class MyClass:
    name = None  # class attribute

    @classmethod
    def set_fruit(cls):
        cls.name = "Rhubarb"
        
    @staticmethod
    def calculate_vat(in_value):
        return in_value * 20 /100
 
MyClass.set_fruit()   # sets the value of the class attribute 'name' to 'Rhubarb'
print(MyClass.name)   # prints Rhubarb
print(MyClass.calculate_vat(10)) # prints 2.0


# slide 77
class MyClass:
    name = None  # class attribute

    #@classmethod
    # Note: set_fruit() is now instance method
    def set_fruit(cls):   # cls acts as 'self'
        cls.name = "Rhubarb"  # same as self.name
        
    @staticmethod
    def calculate_vat(in_value):
        return in_value * 20 /100

print("MyClass.__dict__:\n", MyClass.__dict__)
MyClass.set_fruit(MyClass)   # sets the value of the class attribute 'name' to 'Rhubarb'
print("MyClass.__dict__:\n", MyClass.__dict__)
print(MyClass.name)   # prints Rhubarb
#print(MyClass.calculate_vat(10)) # prints 2.0


# slide 78
class MyClass:
    name = None  # class attribute

    #@classmethod
    # Note: set_fruit() is now instance method
    def set_fruit(cls):   # cls acts as 'self'
        cls.name = "Rhubarb"  # same as self.name
        
    @staticmethod
    def calculate_vat(in_value):
        return in_value * 20 /100

my_obj = MyClass()
my_obj.set_fruit()   # sets the value of the class attribute 'name' to 'Rhubarb'
print(my_obj.name)   # prints Rhubarb
print(my_obj.calculate_vat(10)) # prints 2.0


# slide 79
class ClassName():
    c_var = 'class variable'

    def __init__(self):
        # instance attribute
       self.i_var =  'instance variable'

    @classmethod
    def print_class_attr_using_cls(cls):
        print("Class's class attribute c_var =", cls.c_var)
        #print(cls.ivar)  # raises AttributeError

    # instance methods
    def print_class_attr_using_self(self):
        print("Class's class attribute c_var =", self.__class__.c_var)
        print("Object's class attribute c_var =", self.c_var)
        
    def print_instance_attr(self):
        print("Object's instance attribute i_var =", self.i_var)

# client code
obj_name = ClassName()
obj_name.print_class_attr_using_cls()
obj_name.print_class_attr_using_self()
obj_name.print_instance_attr()


# slides 80-84
class MyClass:
    # class attribute
    fruit = None
    
    @classmethod # (can be called from both class and its intances)
    def set_fruit_from_class(cls, fruit):
        cls.fruit = fruit
        
    # instance method (can be called from intances only, not from class)
    def set_fruit_from_object(self, fruit):
        self.__class__.fruit = fruit

# client code
print("MyClass.fruit =", MyClass.fruit)  # None
obj1 = MyClass()
print("obj1.fruit =", obj1.fruit)        # None
obj2 = MyClass()
print("obj2.fruit =", obj2.fruit)        # None

# changing class attribute directly through class
print("\nMyClass.fruit = 'lemon':")
MyClass.fruit = 'lemon'
print("MyClass.fruit =", MyClass.fruit)  # 'lemon'
print("obj1.fruit =", obj1.fruit)        # 'lemon'
print("obj2.fruit =", obj2.fruit)        # 'lemon'

# changing class attribute from class through class method
print("\nMyClass.set_fruit_from_class('orange'):")
MyClass.set_fruit_from_class('orange')
print("MyClass.fruit =", MyClass.fruit)  # 'orange'
print("obj1.fruit =", obj1.fruit)        # 'orange'
print("obj2.fruit =", obj2.fruit)        # 'orange'

# changing class attribute from class through instance method
# cannot be done, as instance methods cannot be called from class

# changing class attribute from object through class method
print("\nobj1.set_fruit_from_class('apple'):")
obj1.set_fruit_from_class('apple')
print("MyClass.fruit =", MyClass.fruit)  # 'apple'
print("obj1.fruit =", obj1.fruit)        # 'apple'
print("obj2.fruit =", obj2.fruit)        # 'apple'

# changing class attribute from object through instance method
print("\nobj1.set_fruit_from_object('fig'):")
obj1.set_fruit_from_object('fig')
print("MyClass.fruit =", MyClass.fruit)  # 'fig'
print("obj1.fruit =", obj1.fruit)        # 'fig'
print("obj2.fruit =", obj2.fruit)        # 'fig'

# slides 84-86
class Trainee: 
    # class attributes (shared by all instances)
    company = None
    company_owners = []
    count = 0

    # class methods (manage class attributes)
    @classmethod
    def set_company(cls, name):
        cls.company = name 

    @classmethod
    def add_company_owner(cls, name):
        cls.company_owners.append(name)

    @classmethod
    def print_count(cls):
        print("Count trainees:", cls.count)

    # class constructor - initialises instance attributes and increments
    # class attribute count whenever a new Trainee object is created
    def __init__(self, name, stream, weeks, courses):
        self.name = name
        self.stream = stream
        self.weeks = weeks
        self.courses = courses
        self.__class__.count += 1

    # class destructor - decrements class attribute count whenever a
    # Trainee object is deleted
    def __del__(self):
        self.__class__.count -= 1

    # instance methods  
    def assign_course(self, course):
        self.courses[course] = 0 
        
    def assign_mark_for_course(self, course, mark): 
        if course in self.courses:
            self.courses[course] = mark
         
    def avg_mark(self):
        total_marks = 0
        for mark in self.courses.values():
            total_marks += mark
        return total_marks / len(self.courses.values())

# client code
# create the object trainee1 from class Trainee
trainee1 = Trainee("John",
                   "Development",
                   6,
                   {'SQL':75, 'UNIX':78, 'Python':94,
                    'Java':81, 'Web Apps':100, 'Excel':90}
                   )

print(dir(trainee1))
print(trainee1.__dict__)
# {'name': 'John', 'stream': 'Development', 'weeks': 6, 'courses': {'SQL': 75, 'UNIX': 78, 'Python': 94, 'Java': 81, 'Web Apps': 100, 'Excel': 90}}
# class attribute 'count' is accessible from the class:
print("Trainee.count =", Trainee.count)   # Trainee.count = 1
# class attribute 'count' is accessible from the object:
print("trainee1.count =", trainee1.count) # trainee1.count = 1
# class attribute 'count' is accessible from the print_count() instance method:
trainee1.print_count()   # Count trainees: 1
print("trainee1.avg_mark():", trainee1.avg_mark())   # trainee1.avg_mark(): 86.33333333333333

trainee2 = Trainee("Ana",
                   "Development",
                   6,
                   {'SQL':85, 'UNIX':75, 'Python':77,
                    'Java':80, 'Web Apps':90}
                   )
print(trainee2.__dict__)
print('before deleting trainee2:')
Trainee.print_count()   # Count trainees: 2
# to remove (delete) an object use the del keyword to invoke the class destructor
del trainee2
print('after deleting trainee2:')
Trainee.print_count()   # Count trainees: 1
del trainee1
print('after deleting trainee1:')
Trainee.print_count()   # Count trainees: 0


# slide 94
# if defined as public class attributes, constants can still
# be changed (both from the class and from its objects)
class Circle:
    PI = 3.141592  # public class constant PI
    
Circle.PI = 3.141
print(Circle.PI)   # prints 3.141
circle = Circle()
circle.PI = 3.14
print(circle.PI)   # prints 3.14


# slide 95
class Circle:
    _PI = 3.141592  # protected class constant PI

    @property
    def PI(self):
        return self.__class__._PI

    @PI.setter
    def PI(self, new_value):
        # raise AssertionError if PI is not 3.141592
        try:
            assert self.__class__.PI == new_value
        except AssertionError:
            print("PI is defined as a constant and cannot be modified")

print(Circle.__dict__)   # includes '_PI': 3.141592
Circle.PI = 3.141        # includes new attribute PI = 3.141
print(Circle.__dict__)   # includes '_PI': 3.141592, 'PI': 3.141
print(Circle.PI)         # prints 3.141

circle = Circle()
print(circle.__dict__)   # prints {}
circle.PI = 3.14         # prints PI is defined as a constant and cannot be modified
print(circle.__dict__)   # prints {}
print(circle.PI)         # prints 3.141592


# slide 96 - alternative implementation (PI as an instance attribute)
class Circle:
    def __init__(self):
        # Note: 
        # The name of the instance attribute in the constructor
        # must be different from the property name: PI, as in
        # this case constructor should not invoke the setter.
        self._PI = 3.141592
    @property
    def PI(self):
        return self._PI

    @PI.setter
    def PI(self, new_value):
        # print message as MAKE cannot be changed
        print("PI is defined as a constant and cannot be modified")

# client code
circle = Circle()
print(circle.PI)
circle.PI = 3.14  # prints 'PI is defined as a constant and cannot be modified'
print(circle.PI)


# slide 97 - another alternative implementation
class Circle:
    def __init__(self):
        self.PI = 3.141592
    @property
    def PI(self):
        return self._PI

    @PI.setter
    def PI(self, new_value):
        # initialise PI only if it does not exist
        if hasattr(self, '_PI'):  # <=> if '_PI' in self.__dict__.keys():
            print("PI is defined as a constant and cannot be modified")
        else:
            print('Setting PI to', new_value)
            self._PI = new_value

# client code
circle = Circle()
print(circle.PI)
circle.PI = 3.14  # PI is defined as a constant and cannot be modified
print(circle.PI)




