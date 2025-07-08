###########################
# Module 2B - Inheritance #
###########################


# Question 1
# ----------
'''
a) Define a simple empty class called Vehicle.
b) Add an instance method called move() to the Vehicle class.
   Create an instance (object) of this class and call its move()
   method through its object.
c) Convert this class into an abstract class in order to use it
   as common interface (blueprint) for classes that represent
   different types of vehicles. What happens when trying to
   create an instance of this class? Why?
d) Create an empty concrete child class Aircraft that is derived
   from the class Vehicle. What happens when trying to create an
   instance of the class Aircraft? Why?
e) Include the method move() to the concrete child class Aircraft
   and that cpntains just one print statement displaying the
   message 'flying...'.
   Create an instance (object) of the class Aircraft and call its
   move() method through its object. 
f) Add another abstract method to class Vehicle, called
   accelerate(). Create an instance of the class Vehicle.
   What happens? Why?
g) Implement the accelerate() method in Aircraft class by
   displaying the message: 'reached 150 mph in 30 seconds'
   Create an instance (object) of the class Aircraft and call its
   accelerate() method through its object. 
h) Add a print statement to the accelerate() method of the Vehicle
   abstract class, displaying the message 'engine started...'.
   Call the accelerate method of the abstract class from the
   Aircraft child class before printing the message 'reached 150
   mph in 30 seconds'. See what happens and explain why.
i) Create another concrete child class Car that is derived from
   the class Vehicle and implements both move() and accelerate()
   methods. The move() method displays the message 'driving...'
   and the accelerate method displays the message 'reached 60 mph
   in 10 seconds'
   Create an object of classes Car and Aircraft, and call both 
   their move and accelerate methods. See what happens and explain
   the benefit of having the message 'engine started...' displayed in the
   abstract method accelerate().
j) Introduce an instance attribute called speed to the abstract
   class Vehicle and include property methods to read and modify
   its value (getter and setter). Declare these two property
   methods as abstract in order to enforce their implementation in
   every subclass of Vehicle. Create an instance of the Aircraft
   or Car class after adding the abstract property methods to
   their parent abstract class. What happens and why?
k) Implement the property methods to read and modify the value of
   instance attribute speed.
   Create an instance of the Aircraft and Car class after adding
   the abstract property methods to their parent abstract class.
   Modify the speed of both the aircraft and car objects.
l) Change the constructor to set the initial speed at 0 mph (once
   created, any vehicle is not moving), ensuring that every
   vehicle must have its initial speed set to 0 once created.
   Set the speed in the accelerate() method of both Aircraft and
   Car concrete classes to the speed displayed in the message.
   Test that it all works correctly by creating an object of both
   Aircraft and Car and doing the following for each object:
   - prints its speed
   - call its acccelerate method
   - print its speed
   - change its speed to some value above the one stated in the accelerate method
   - print its speed
   - call its move method
'''
# Question 1a)
# ------------
print('--- Q1a) ---')
class Vehicle:
    pass

# Question 1b)
# ------------
print('--- Q1b) ---')
class Vehicle():
    def move(self):
        pass

vehicle1 = Vehicle()
vehicle1.move()

# Question 1c)
# ------------
print('--- Q1c) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move():
        pass

# Abstract classes cannot be instantiated.
# an attempt to instantiate an abstract class results in
# TypeError: Can't instantiate abstract class Vehicle with
# abstract methods move:
#vehicle1 = Vehicle()

# Question 1d)
# ------------
print('--- Q1d) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move():
        pass

class Aircraft(Vehicle):
    pass

# To be able to create an object of class Aircraft, Aircraft
# must provide an implementation for the abstract method move()
# Since Aircraft class doesn't, an attempt to instantiate it
# throws TypeError: Can't instantiate abstract class Vehicle
# with abstract methods move
#jet1 = Aircraft()

# Question 1e)
# ------------
print('--- Q1e) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move():
        pass

class Aircraft(Vehicle):
    def move(self):
        print('flying...')

jet1 = Aircraft()
jet1.move()        # prints 'flying...'

# Question 1f)
# ------------
print('--- Q1f) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move():
        pass
    
    @abstractmethod
    def accelerate():
        pass


class Aircraft(Vehicle):
    def move(self):
        print('flying...')

# The Aircraft subclass doesn't provide a concrete implementation
# for the abstract method accelerate in Vehicle abstract class.
# To instantiate a class that derives from an abstract class
# the derived class must provide an implementation for ALL the
# abstract methods inherited from the parent abstract class.
# Since this is not the case here, an attempt to instantiate
# Aircraft results in TypeError: Can't instantiate abstract
# class Aircraft with abstract methods accelerate
#jet1 = Aircraft()

# Question 1g)
# ------------
print('--- Q1g) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move():
        pass
    
    @abstractmethod
    def accelerate():
        pass


class Aircraft(Vehicle):
    def move(self):
        print('flying...')

    def accelerate(self):
        print('reached 150 mph in 30 seconds')

jet1 = Aircraft()
jet1.accelerate()  # prints 'reached 150 mph in 30 seconds'


# Question 1h)
# ------------
print('--- Q1h) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        print('engine started...')


class Aircraft(Vehicle):
    def move(self):
        print('flying...')

    def accelerate(self):
        super().accelerate()
        print('reached 150 mph in 30 seconds')

# An abstract method in Python doesn't necessarily have to be
# completely empty. It can contain some implementation that can
# be reused by child classes by calling the abstract method
# with super(). This doesn’t exclude the fact that child
# classes still have to implement the abstract method.
jet1 = Aircraft()
jet1.accelerate()  # prints 'engine started...' followed by 'reached 150 mph in 30 seconds'

# Question 1i)
# ------------
print('--- Q1i) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        print('engine started...')


class Aircraft(Vehicle):
    def move(self):
        print('flying...')

    def accelerate(self):
        super().accelerate()
        print('reached 150 mph in 30 seconds')

class Car(Vehicle):
    def move(self):
        print('driving...')

    def accelerate(self):
        super().accelerate()
        print('reached 60 mph in 5 seconds')

# Placing the code that is common for all derived classes
# in the abstract method of the abstract class avoids repeating
# the same code in all the child classes of the abstract class.
# Since the common code is in the abstract class, it must be
# invoked from the derived classes, ensuring that all derived
# classes will have the common code executed.
jet1 = Aircraft()
jet1.move()
jet1.accelerate()  # prints 'engine started...' followed by 'reached 150 mph in 30 seconds'

car1 = Car()
car1.move()
car1.accelerate()  # prints 'engine started...' followed by 'reached 150 mph in 30 seconds'


# Question 1j)
# ------------
print('--- Q1j) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass
        
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        print('engine started...')

class Aircraft(Vehicle):
    def move(self):
        print('flying...')

    def accelerate(self):
        super().accelerate()
        print('reached 150 mph in 30 seconds')

class Car(Vehicle):
    def move(self):
        print('driving...')

    def accelerate(self):
        super().accelerate()
        print('reached 60 mph in 5 seconds')
        
# The abstract property methods in abstract class must be
# implemented in its child concrete classes in order to be
# instantiable.
# Since the abstract property methods have not been implemented
# in any of its child concrete classes, an attempt to instantiate
# any of them throws TypeError: Can't instantiate abstract
# class Car with abstract methods speed
#car1 = Car()
# throws TypeError: Can't instantiate abstract class Aircraft
# with abstract methods speed
#jet1 = Aircraft()

# Question 1k)
# ------------
print('--- Q1k) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass
        
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        print('engine started...')

class Aircraft(Vehicle):
    def __init__(self, speed):
        self.__speed = speed
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    def move(self):
        print('flying...')

    def accelerate(self):
        super().accelerate()
        print('reached 150 mph in 30 seconds')

class Car(Vehicle):
    def __init__(self, speed):
        self.__speed = speed
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    def move(self):
        print('driving...')

    def accelerate(self):
        super().accelerate()
        print('reached 60 mph in 5 seconds')

jet1 = Aircraft(150)
print('jet1.speed =', jet1.speed)
print('jet1.__dict__:', jet1.__dict__)
jet1.speed = 180
print('jet1.speed =', jet1.speed)

car1 = Car(60)
print('car1.speed =', car1.speed)
print('car1.__dict__:', car1.__dict__)
car1.speed = 80
print('car1.speed =', car1.speed)

# Question 1l)
# ------------
print('--- Q1l) ---')
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def __init__(self):
        self.speed = 0
    
    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass
        
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def accelerate(self):
        print('engine started...')

class Aircraft(Vehicle):
    def __init__(self):
        super().__init__()
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    def move(self):
        print('flying...')

    def accelerate(self):
        super().accelerate()
        self.speed = 150
        print('reached 150 mph in 30 seconds')

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    def move(self):
        print('driving...')

    def accelerate(self):
        super().accelerate()
        self.speed = 60
        print('reached 60 mph in 5 seconds')

# create a Aircraft object jet 1
jet1 = Aircraft()
# prints its speed
print('jet1.speed =', jet1.speed)  # prints jet1.speed = 0
# call its acccelerate method
jet1.accelerate()  # prints 'engine started...' followed by 'reached 150 mph in 30 seconds'
# print its speed
print('jet1.speed =', jet1.speed)  # prints jet1.speed = 150
# change its speed to some value above the one stated in the
# accelerate method
jet1.speed = 300
# print its speed
print('jet1.speed =', jet1.speed)  # prints jet1.speed = 300
# call its move method
jet1.move()  # prints 'flying..'

# create a Car object car1
car1 = Car()
# prints its speed
print('car1.speed =', car1.speed)  # prints car1.speed = 0
# call its acccelerate method
car1.accelerate()  # prints 'engine started...' followed by 'reached 60 mph in 5 seconds'
# print its speed
print('car1.speed =', car1.speed)  # prints car1.speed = 60
# change its speed to some value above the one stated in the accelerate method
car1.speed = 80
# print its speed
print('car1.speed =', car1.speed)  # prints car1.speed = 80
# call its move method
car1.move()  # prints 'driving..'


# Question 2
# ----------
'''
Add the class Hardware to the classes created in Module 2A Question 3
and make it parent of both HardDrive and Memory. Move the common
attributes and methods from the two existing classes to the
Hardware class. Then write the client code to do the following:
• All tasks listed under client code to test the HardDrive class in Module 2A question 3.
    In addition, check that:
    o the private instance attributes model and capacity are name-mangled to _Hardware__model and _Hardware__capacity, instead of _HardDrive__model and _HardDrive__capacity (by printing the object's namespace as soon as the HardDrive object is created)
    o model & capacity properties are now listed in the Hardware namespace instead of HardDrive namespace (by printing both HardDrive and Hardware namespaces as soon as the HardDrive object is created)
• All tasks listed under client code to test the Memory class in Module 2A question 3. In addition, check that:
    o the private instance attributes model and capacity are name-mangled to _Hardware__model and _Hardware__capacity, instead of _Memory__model and _ Memory __capacity but that speed is name-mangled to _Memory__speed (by printing the object's namespace as soon as the Memory object is created)
    o model & capacity properties are now listed in the Hardware namespace instead of Memory namespace, but speed property is still listed in the Memory namespace (by printing both Memory and Hardware namespaces as soon as the Memory object is created)
• create a Hardware object
• display the namespace of both the class and the object
• display the model and capacity directly from the object (ensure the getter gets invoked in both cases)
• set the value of model for the object to 'Dell' and the value of capacity to 4096GB (ensure the setter gets invoked in both cases displaying the appropriate message)
• display the values of model and capacity directly from the object (ensure the getter gets invoked in both cases and that the values of both attributes have not been changed)
• use the set_used_space method to change the used space to 500GB and check that it was changed by displaying the used_space attribute directly from the object
• set the docstring for the model to 'name of the hard disk model' and for the capacity to 'hard disk capacity', and then display them both
• delete the model, capacity and used space attributes and check their removal by displaying the object's namespace after each attribute is deleted
'''
class Hardware:
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
        # if object has '_Hardware__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Hardware__model'):  # <=> if '_Hardware__model' in self.__dict__.keys():
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
        # if object has '_Hardware__capacity' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Hardware__capacity'):  # <=> if '_Hardware__capacity' in self.__dict__.keys():
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

class HardDrive(Hardware):
    def __init__(self, model, capacity):
        super().__init__(model, capacity)  # or Hardware.__init__(self, model, capacity)

    def read_data(self, file):
        print('read_data: reading data from', file)

    def write_data(self, file):
        print('write_data: writing data to', file)

class Memory(Hardware):
    def __init__(self, model, capacity, speed):
        super().__init__(model, capacity)  # or Hardware.__init__(self, model, capacity)
        self.speed = speed

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

    def store_data(self, data):
        print('store_data: storing data:', data)

print('--- Q2: HardDrive ---')
# client code to test HardDrive class
# create HardDrive object (calling the Hardware's setter)
hd = HardDrive('Seagate', 2048)  # prints Setting model to Seagate and Setting capacity to 2048 before initialising private instance attributes model and capacity name-mangled to _Hardware__model and _Hardware__capacity
print(hd.__dict__)               # prints {'_Hardware__model': 'Seagate', '_Hardware__model': 2048}
print(HardDrive.__dict__)        # does not list 'model' & 'capacity' properties
print(Hardware.__dict__)         # lists 'model' & 'capacity' properties
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# calls the setter
hd.model = 'WD'                  # prints 'Attempting to alter read-only attribute: model'
hd.capacity = 3072               # prints 'Attempting to alter read-only attribute: capacity'
print(hd.__dict__)               # prints {'_Hardware__model': 'Seagate', '_Hardware__capacity': 2048}
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# execute the instance methods
hd.set_used_space(0)             # sets the public instance attribute used_space to 0
print(hd.used_space)             # prints 0
print(hd.__dict__)               # prints {'_Hardware__model': 'Seagate', '_Hardware__capacity': 2048, 'used_space': 0}
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
print(HardDrive.__dict__)        # does not list 'model' & 'capacity' properties
print(Hardware.__dict__)         # lists 'model' and 'capacity' properties

print('--- Q2: Memory ---')
# client code to test Memory class
# create Memory object (calling the setter)
memory = Memory('Kingston', 4, 1600)  # prints Setting model to Kingston, Setting capacity to 4 and Setting speed to 1600 before initialising private instance attributes model, capacity and speed, name-mangled as _Hardware__model, _Hardware__capacity and _Memory__speed 
print(memory.__dict__)                # prints {'_Hardware__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600}
print(Memory.__dict__)                # lists 'speed' property
print(Hardware.__dict__)              # lists 'model' and 'capacity' properties

# calls the getter
print(memory.model)                   # prints Getting model: Kingston
print(memory.capacity)                # prints Getting capacity: 4
print(memory.speed)                   # prints Getting speed: 1600
# calls the setter
memory.model = 'Corsair'              # prints 'Attempting to alter read-only attribute: model'
memory.capacity = 8                   # prints 'Attempting to alter read-only attribute: capacity'
memory.speed = 1333                   # prints 'Attempting to alter read-only attribute: speed'
print(memory.__dict__)                # prints {'_Hardware__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600}
# calls the getter
print(memory.model)                  # prints Getting model: Kingston
print(memory.capacity)               # prints Getting capacity: 4
print(memory.speed)                  # prints Getting speed: 1600
# execute the instance methods
memory.set_used_space(0.5)           # sets the public instance attribute used_space to 0.5
print(memory.used_space)             # prints 0.5
print(memory.__dict__)               # prints {'_Hardware__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
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
print(memory.__dict__)               # prints {'_Hardware__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
del memory.capacity                  # prints Deleting capacity: 4
print(memory.__dict__)               # prints {'_Memory__speed': 1600, 'used_space': 0.5}
del memory.speed                     # prints Deleting speed: 1600
print(memory.__dict__)               # prints {'used_space': 0.5}
del memory.used_space
print(memory.__dict__)               # prints {}
print(Memory.__dict__)               # lists 'speed' property
print(Hardware.__dict__)             # lists 'model' and 'capacity' properties

print('--- Q2: Hardware ---')
# client code to test Hardware class
# create Hardware object (calling the setter)
hardware = Hardware('Seagate', 2048)  # prints Setting model to Seagate and Setting capacity to 2048 before initialising private instance attributes model and capacity, name-mangled to _Hardware__model and _Hardware__capacity 
print(hardware.__dict__)              # prints {'_Hardware__model': 'Seagate', '_Hardware__capacity': 2048}
print(Hardware.__dict__)              # lists 'model' and 'capacity' properties
# calls the getter
print(hardware.model)                  # prints Getting model: Seagate
print(hardware.capacity)               # prints Getting capacity: 2048
# calls the setter
hardware.model = 'Dell'                # prints 'Attempting to alter read-only attribute: model'
hardware.capacity = 4096               # prints 'Attempting to alter read-only attribute: capacity'
print(hardware.__dict__)               # prints {'_Hardware__model': 'Seagate', '_Hardware__capacity': 2048}
# calls the getter
print(hardware.model)                  # prints Getting model: Seagate
print(hardware.capacity)               # prints Getting capacity: 2048
# execute the instance methods
hardware.set_used_space(500)           # sets the public instance attribute used_space to 0
print(hardware.used_space)             # prints 500
print(hardware.__dict__)               # prints {'_Hardware__model': 'Seagate', '_Hardware__capacity': 2048, 'used_space': 500}
# set the docstring
Hardware.model.__doc__ = 'name of the hard disk model'
Hardware.capacity.__doc__ = 'hard disk capacity'
# display the docstring
print('Docstring:', Hardware.model.__doc__)    # prints Docstring: name of the hard disk model
print('Docstring:', Hardware.capacity.__doc__) # prints Docstring: hard disk capacity
# calls the deleter
del hardware.model                     # prints Deleting model: Seagate
print(hardware.__dict__)               # prints {'_Hardware__capacity': 2048, 'used_space': 500}
del hardware.capacity                  # prints Deleting capacity: 2048
print(hardware.__dict__)               # prints {'used_space': 500}
del hardware.used_space
print(hardware.__dict__)               # prints {}
print(Hardware.__dict__)               # lists 'model' and 'capacity' properties


# Question 3
# ----------
'''
The class Hardware created in Module 2B Question 2 is generic
(relates to any hardware device) and should therefore not be
instantiable. Modify the class Hardware to make it abstract and
ensure that its subclasses HardDrive and Memory work as before.
Check that an attempt to instantiate the Hardware class
throws an error.
Note: although every hard drive and memory will always have both
memory and capacity attributes, not every hardware component
will necessarily have capacity, but it will always have the model.
'''
# import the ABC class and abstractmethod from the abc module
from abc import ABC, abstractmethod

class Hardware(ABC):
    # by not making the constructor as abstract, subclasses
    # can choose whether to invoke it or not.
    # Both HardDrive and Memory classes have model & capacity
    # attributes, hence they should call it
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    # only model attribute is present in all subclasses of the
    # abstract class Hardware - hence in the abstract class the
    # implementation of getter, setter and deleter is enforced
    # only for the attribute 'model' (made abstract here but must be
    # implemented in its subclasses HardDrive and Memory)
    # getter, setter and deleter for the attribute 'capacity'
    # are left as non-abstract in the abstract class Hardware
    # so that they can be ignored if not needed in subclasses,
    # or inherited if needed
    
    # getter method for model
    @property
    @abstractmethod
    def model(self):
        pass
    
    # setter method for model
    @model.setter
    @abstractmethod
    def model(self, value):
        pass
    
    # deleter method for model
    @model.deleter
    @abstractmethod
    def model(self):
        pass
    
    # getter method for capacity
    @property
    def capacity(self):
        print('Getting capacity:')
        return self.__capacity
    
    # setter method for capacity
    @capacity.setter
    def capacity(self, value):
        # if object has '_Hardware__capacity' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Hardware__capacity'):  # <=> if '_Hardware__capacity' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: capacity")
        else:
            print('Setting capacity to', value)
            self.__capacity = value
        
    # deleter method for capacity
    @capacity.deleter
    def capacity(self):
        print('Deleting capacity:', self.__capacity)
        del self.__capacity

    @abstractmethod
    def set_used_space(self, used_space):
        self.used_space = used_space

class HardDrive(Hardware):
    def __init__(self, model, capacity):
        super().__init__(model, capacity)  # or Hardware.__init__(self, model, capacity)

    # getter method for model
    @property
    def model(self):
        print('Getting model:')
        return self.__model

    # setter method for model
    # (assigns the model value passed from the constructor to 
    # the private instance attribute __model, name mangled to
    # _HardDrive__model, that cannot be changed thereafter)
    @model.setter
    def model(self, value):
        # if object has '_HardDrive__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_HardDrive__model'):  # <=> if '_Hardware__model' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: model")
        else:
            print('Setting model to', value)
            self.__model = value
            
    # deleter method for model
    @model.deleter
    def model(self):
        print('Deleting model:', self.__model)
        del self.__model

    def read_data(self, file):
        print('read_data: reading data from', file)

    def write_data(self, file):
        print('write_data: writing data to', file)

    # instance methods
    def set_used_space(self, used_space):
        super().set_used_space(used_space)        

class Memory(Hardware):
    def __init__(self, model, capacity, speed):
        super().__init__(model, capacity)  # or Hardware.__init__(self, model, capacity)
        self.speed = speed

    # getter method for model
    @property
    def model(self):
        print('Getting model:')
        return self.__model

    # setter method for model
    # (assigns the model value passed from the constructor to 
    # the private instance attribute __model, name mangled to
    # _Memory__model, that cannot be changed thereafter)
    @model.setter
    def model(self, value):
        # if object has '_Memory__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__model'):  # <=> if '_Memory__model' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: model")
        else:
            print('Setting model to', value)
            self.__model = value
            
    # deleter method for model
    @model.deleter
    def model(self):
        print('Deleting model:', self.__model)
        del self.__model

    # getter method for speed
    @property
    def speed(self):
        print('Getting speed:')
        return self.__speed
    
    # setter method for speed
    @speed.setter
    def speed(self, value):
        # if object has '_Memory__speed' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__speed'):  # <=> if '_Memory__speed' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: speed")
        else:
            print('Setting speed to', value)
            self.__speed = value
        
    # deleter method for speed
    @speed.deleter
    def speed(self):
        print('Deleting speed:', self.__speed)
        del self.__speed

    def store_data(self, data):
        print('store_data: storing data:', data)

    # instance methods
    def set_used_space(self, used_space):
        super().set_used_space(used_space)


print('--- Q3: HardDrive ---')
# client code to test HardDrive class
# create HardDrive object (calling the Hardware's setter)
hd = HardDrive('Seagate', 2048)  # prints Setting model to Seagate and Setting capacity to 2048 before initialising private instance attributes model and capacity name-mangled to _HardDrive__model and _Hardware__capacity
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_Hardware__capacity': 2048}
print(HardDrive.__dict__)        # lists 'model property
print(Hardware.__dict__)         # lists 'model' & 'capacity' properties
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# calls the setter
hd.model = 'WD'                  # prints 'Attempting to alter read-only attribute: model'
hd.capacity = 3072               # prints 'Attempting to alter read-only attribute: capacity'
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_Hardware__capacity': 2048}
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# execute the instance methods
hd.set_used_space(0)             # sets the public instance attribute used_space to 0
print(hd.used_space)             # prints 0
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_Hardware__capacity': 2048, 'used_space': 0}
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
print(hd.__dict__)               # prints {'_Hardware__capacity': 2048, 'used_space': 0}
del hd.capacity                  # prints Deleting capacity: 2048
print(hd.__dict__)               # prints {'used_space': 0}
del hd.used_space
print(hd.__dict__)               # prints {}
print(HardDrive.__dict__)        # lists 'model' property
print(Hardware.__dict__)         # lists 'model' and 'capacity' properties

print('--- Q3: Memory ---')
# client code to test Memory class
# create Memory object (calling the setter)
memory = Memory('Kingston', 4, 1600)  # prints Setting model to Kingston, Setting capacity to 4 and Setting speed to 1600 before initialising private instance attributes model, capacity and speed, name-mangled as _Memory__model, _Hardware__capacity and _Memory__speed 
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600}
print(Memory.__dict__)                # lists 'model' and 'speed' properties
print(Hardware.__dict__)              # lists 'model' and 'capacity' properties

# calls the getter
print(memory.model)                   # prints Getting model: Kingston
print(memory.capacity)                # prints Getting capacity: 4
print(memory.speed)                   # prints Getting speed: 1600
# calls the setter
memory.model = 'Corsair'              # prints 'Attempting to alter read-only attribute: model'
memory.capacity = 8                   # prints 'Attempting to alter read-only attribute: capacity'
memory.speed = 1333                   # prints 'Attempting to alter read-only attribute: speed'
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600}
# calls the getter
print(memory.model)                   # prints Getting model: Kingston
print(memory.capacity)                # prints Getting capacity: 4
print(memory.speed)                   # prints Getting speed: 1600
# execute the instance methods
memory.set_used_space(0.5)            # sets the public instance attribute used_space to 0.5
print(memory.used_space)              # prints 0.5
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
memory.store_data('data_to_store')    # prints 'store_data: storing data: data_to_store'
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
print(memory.__dict__)               # prints {'_Hardware__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
del memory.capacity                  # prints Deleting capacity: 4
print(memory.__dict__)               # prints {'_Memory__speed': 1600, 'used_space': 0.5}
del memory.speed                     # prints Deleting speed: 1600
print(memory.__dict__)               # prints {'used_space': 0.5}
del memory.used_space
print(memory.__dict__)               # prints {}
print(Memory.__dict__)               # lists 'model' and 'speed' properties
print(Hardware.__dict__)             # lists 'model' and 'capacity' properties

# client code to test that the abstract Hardware class cannot be instantiated
#hardware = Hardware('Seagate', 2048)   # throws TypeError: Can't instantiate abstract class Hardware with abstract methods set_used_space


# Question 4
# ----------
'''
Improve the classes Hardware, HardDrive and Memory created in Module 2B Question 3 by implementing the following:
• include the hard drive counter: count_hard_drive, storing the number of created hard drives
• include the memory counter: count_memory, storing the number of created memory components
• include the hardware counter: count_hardware, storing the number of created hardware components, where the hardware
  counter will always show the total of hard drive and memory counters
• increase the counters count_hard_drive and count_memory whenever a hard disk or a memory has been produced respectively
• include the increment_counter() method to the Hardware class to increase the class attribute count_hardware whenever a
  hard disk or a memory has been produced, and display a message: "New hard drive created" or "New memory created",
  depending on whether a hard drive or memory has been created
• include the print_count() method to print the number of produced Hardware, HardDrive and Memory components.
'''
# import the ABC class and abstractmethod from the abc module
from abc import ABC, abstractmethod

class Hardware(ABC):
    # class attributes
    count_hardware = 0  # stores the number of created hardware components
    
    # by not making the constructor as abstract, subclasses
    # can choose whether to invoke it or not.
    # Both HardDrive and Memory classes have model & capacity
    # attributes, hence they should call it
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    # Only the attribute 'model' is present in all subclasses of the
    # abstract class Hardware - hence in the abstract class the
    # implementation of getter, setter and deleter is enforced
    # only for the attribute 'model' (made abstract here but 
    # must be implemented in its subclasses HardDrive and Memory).
    # The getter, setter and deleter for the attribute 'capacity'
    # are left as non-abstract in the abstract class Hardware
    # so that they can be ignored if not needed in subclasses,
    # or inherited if needed
    
    # getter method for model
    @property
    @abstractmethod
    def model(self):
        pass
    
    # setter method for model
    @model.setter
    @abstractmethod
    def model(self, value):
        pass
    
    # deleter method for model
    @model.deleter
    @abstractmethod
    def model(self):
        pass
    
    # getter method for capacity
    @property
    def capacity(self):
        print('Getting capacity:')
        return self.__capacity
    
    # setter method for capacity
    @capacity.setter
    def capacity(self, value):
        # if object has '_Hardware__capacity' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Hardware__capacity'):  # <=> if '_Hardware__capacity' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: capacity")
        else:
            print('Setting capacity to', value)
            self.__capacity = value
        
    # deleter method for capacity
    @capacity.deleter
    def capacity(self):
        print('Deleting capacity:', self.__capacity)
        del self.__capacity

    @abstractmethod
    def set_used_space(self, used_space):
        self.used_space = used_space
        
    # class methods
    '''
    The increment_counter() method needs to be defined as class method in Hardware class,
    as it modifies the class attribute count_hardware). Since it will be called from
    HardDrive and Memory classes to increase the counter for Hardware components, it is
    appropriate to define it as protected in Hardware class (to make it accessible only
    from Hardware class and its subclasses).
    To produce the message appropriate to the produced component (hard drive or memory), 
    increment_counter method needs to accept one parameter: component_type. When called from
    HardDrive class, it will be called as Hardware.increment_counter('hard drive'), but when called
    from Memory class, it will be called as Memory.increment_counter('memory').
    '''
    @classmethod
    def _increment_counter(cls, component_type):   # protected method (name preceded by _)
        print('New', component_type, 'created.')
        cls.count_hardware += 1
        
    '''
    The print_count() method in HardDrive class needs to print the number of produced hard drives.
    The print_count() method in Memory class needs to print the number of produced memory components.
    The print_count() method in both HardDrive and Memory classes must be defined as class method, because 
    it accesses (displays) the value of class attributes count_hard_drive and count_memory respectively.
    Since print_count() method also needs to access the class attribute count_hardware to print the number
    of produced hardware components, it must be defined as class method in Hardware class as well, but it
    cannot be defined as abstract, otherwise its implementation could not be written in the Hardware class.
    The solution is to use method overriding - defining a method in the subclass which already exists in the parent class.
    By defining the print_count() method in all three classes, print_count() method in HardDrive
    and Memory classes will override the print_count() method in Hardware class: although
    inherited from Hardware, being re-defined in its subclasses, print_count() from Hardware will be ignored
    and print_count() from HardDrive and Memory classes will be used respectively in these classes instead.
    The print_count() method in each class will have its own message to be printed.
    '''
    @classmethod
    def print_count(cls):
        print('The number of hardware components is', cls.count_hardware)


class HardDrive(Hardware):
    # class attributes
    count_hard_drive = 0  # stores the number of created hard drives

    def __init__(self, model, capacity):
        super().__init__(model, capacity)  # or Hardware.__init__(self, model, capacity)
        self.__class__.count_hard_drive += 1
        Hardware._increment_counter('hard drive')

    # getter method for model
    @property
    def model(self):
        print('Getting model:')
        return self.__model

    # setter method for model
    # (assigns the model value passed from the constructor to 
    # the private instance attribute __model, name mangled to
    # _HardDrive__model, that cannot be changed thereafter)
    @model.setter
    def model(self, value):
        # if object has '_HardDrive__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_HardDrive__model'):  # <=> if '_Hardware__model' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: model")
        else:
            print('Setting model to', value)
            self.__model = value
            
    # deleter method for model
    @model.deleter
    def model(self):
        print('Deleting model:', self.__model)
        del self.__model

    def read_data(self, file):
        print('read_data: reading data from', file)

    def write_data(self, file):
        print('write_data: writing data to', file)

    # instance methods
    def set_used_space(self, used_space):
        super().set_used_space(used_space)        

    # class methods
    @classmethod
    def print_count(cls):
        print('The number of hard drive components is', cls.count_hard_drive)


class Memory(Hardware):
    # class attributes
    count_memory = 0  # stores the number of created memory components
    
    def __init__(self, model, capacity, speed):
        super().__init__(model, capacity)  # or Hardware.__init__(self, model, capacity)
        self.speed = speed
        self.__class__.count_memory += 1
        Hardware._increment_counter('memory')

    # getter method for model
    @property
    def model(self):
        print('Getting model:')
        return self.__model

    # setter method for model
    # (assigns the model value passed from the constructor to 
    # the private instance attribute __model, name mangled to
    # _Memory__model, that cannot be changed thereafter)
    @model.setter
    def model(self, value):
        # if object has '_Memory__model' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__model'):  # <=> if '_Memory__model' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: model")
        else:
            print('Setting model to', value)
            self.__model = value
            
    # deleter method for model
    @model.deleter
    def model(self):
        print('Deleting model:', self.__model)
        del self.__model

    # getter method for speed
    @property
    def speed(self):
        print('Getting speed:')
        return self.__speed
    
    # setter method for speed
    @speed.setter
    def speed(self, value):
        # if object has '_Memory__speed' attribute print error message
        # otherwise create it and initialise with the given value
        if hasattr(self, '_Memory__speed'):  # <=> if '_Memory__speed' in self.__dict__.keys():
            print("Attempting to alter read-only attribute: speed")
        else:
            print('Setting speed to', value)
            self.__speed = value
        
    # deleter method for speed
    @speed.deleter
    def speed(self):
        print('Deleting speed:', self.__speed)
        del self.__speed

    def store_data(self, data):
        print('store_data: storing data:', data)

    # instance methods
    def set_used_space(self, used_space):
        super().set_used_space(used_space)

    # class methods
    @classmethod
    def print_count(cls):
        print('The number of memory components is', cls.count_memory)


print('--- Q4: HardDrive ---')
# client code to test HardDrive class
# create HardDrive object (calling the Hardware's setter)
hd = HardDrive('Seagate', 2048)  # prints Setting model to Seagate and Setting capacity to 2048 before initialising private instance attributes model and capacity name-mangled to _HardDrive__model and _Hardware__capacity
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_Hardware__capacity': 2048}
print(HardDrive.__dict__)        # lists 'model property
print(Hardware.__dict__)         # lists 'model' & 'capacity' properties
# test the counters
print('Hardware.count_hardware =', Hardware.count_hardware)
print('HardDrive.count_hard_drive =', HardDrive.count_hard_drive)
# test the print_count() methods
print('Hardware.print_count():')
Hardware.print_count()
print('HardDrive.print_count():')
HardDrive.print_count()

# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# calls the setter
hd.model = 'WD'                  # prints 'Attempting to alter read-only attribute: model'
hd.capacity = 3072               # prints 'Attempting to alter read-only attribute: capacity'
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_Hardware__capacity': 2048}
# calls the getter
print(hd.model)                  # prints Getting model: Seagate
print(hd.capacity)               # prints Getting capacity: 2048
# execute the instance methods
hd.set_used_space(0)             # sets the public instance attribute used_space to 0
print(hd.used_space)             # prints 0
print(hd.__dict__)               # prints {'_HardDrive__model': 'Seagate', '_Hardware__capacity': 2048, 'used_space': 0}
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
print(hd.__dict__)               # prints {'_Hardware__capacity': 2048, 'used_space': 0}
del hd.capacity                  # prints Deleting capacity: 2048
print(hd.__dict__)               # prints {'used_space': 0}
del hd.used_space
print(hd.__dict__)               # prints {}
print(HardDrive.__dict__)        # lists 'model' property
print(Hardware.__dict__)         # lists 'model' and 'capacity' properties

print('--- Q4: Memory ---')
# client code to test Memory class
# create Memory object (calling the setter)
memory = Memory('Kingston', 4, 1600)  # prints Setting model to Kingston, Setting capacity to 4 and Setting speed to 1600 before initialising private instance attributes model, capacity and speed, name-mangled as _Memory__model, _Hardware__capacity and _Memory__speed 
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600}
print(Memory.__dict__)                # lists 'model' and 'speed' properties
print(Hardware.__dict__)              # lists 'model' and 'capacity' properties
# test the counters
print('Hardware.count_hardware =', Hardware.count_hardware)
print('HardDrive.count_hard_drive =', HardDrive.count_hard_drive)
print('Memory.count_memory =', Memory.count_memory)
# test the print_count() methods
print('Hardware.print_count():')
Hardware.print_count()
print('HardDrive.print_count():')
HardDrive.print_count()
print('Memory.print_count():')
Memory.print_count()

# calls the getter
print(memory.model)                   # prints Getting model: Kingston
print(memory.capacity)                # prints Getting capacity: 4
print(memory.speed)                   # prints Getting speed: 1600
# calls the setter
memory.model = 'Corsair'              # prints 'Attempting to alter read-only attribute: model'
memory.capacity = 8                   # prints 'Attempting to alter read-only attribute: capacity'
memory.speed = 1333                   # prints 'Attempting to alter read-only attribute: speed'
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600}
# calls the getter
print(memory.model)                   # prints Getting model: Kingston
print(memory.capacity)                # prints Getting capacity: 4
print(memory.speed)                   # prints Getting speed: 1600
# execute the instance methods
memory.set_used_space(0.5)            # sets the public instance attribute used_space to 0.5
print(memory.used_space)              # prints 0.5
print(memory.__dict__)                # prints {'_Memory__model': 'Kingston', '_Hardware__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
memory.store_data('data_to_store')    # prints 'store_data: storing data: data_to_store'
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
print(memory.__dict__)               # prints {'_Hardware__capacity': 4, '_Memory__speed': 1600, 'used_space': 0.5}
del memory.capacity                  # prints Deleting capacity: 4
print(memory.__dict__)               # prints {'_Memory__speed': 1600, 'used_space': 0.5}
del memory.speed                     # prints Deleting speed: 1600
print(memory.__dict__)               # prints {'used_space': 0.5}
del memory.used_space
print(memory.__dict__)               # prints {}
print(Memory.__dict__)               # lists 'model' and 'speed' properties
print(Hardware.__dict__)             # lists 'model' and 'capacity' properties

# test the counters
print('Hardware.count_hardware =', Hardware.count_hardware)
print('HardDrive.count_hard_drive =', HardDrive.count_hard_drive)
print('Memory.count_memory =', Memory.count_memory)
# test the print_count() methods
print('Hardware.print_count():')
Hardware.print_count()
print('HardDrive.print_count():')
HardDrive.print_count()
print('Memory.print_count():')
Memory.print_count()

# client code to test that the abstract Hardware class cannot be instantiated
#hardware = Hardware('Seagate', 2048)   # throws TypeError: Can't instantiate abstract class Hardware with abstract methods set_used_space
