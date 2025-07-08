# example of a class with private attributes
class Rectangle:
    def __init__(self, length, width):
        self.__length = length  # private attribute
        self.__width = width    # private attribute

# By convention, the double underscore prefix for an instance variable marks it as private
# (and therefore cannot be accessed outside the class methods).

rectangle1 = Rectangle(10, 5)

# dir(rectangle1) lists all attributes and methods available for the rectangle1 object.
# Notice that attributes '__length' & '__width' are not listed. Instead,
# there are the renamed attributes: '_Rectangle__length' & '_Rectangle__width'
print(dir(rectangle1))
# Python performs name mangling of private variables. Every member with a double underscore
# will be changed to _class__variable and can be accessed outside the class through
# object._class__variable. So, it can still be accessed from outside the class,
# but the practice should be refrained.

# Notice also the object's built-in '__dict__' dictionary attribute
# It is used by Python to store the instance (not class!) attributes and their values as (key,value) pairs.
print("rectangle1.__dict__['_Rectangle__length'] =", rectangle1.__dict__['_Rectangle__length'])
print("rectangle1.__dict__['_Rectangle__width'] =", rectangle1.__dict__['_Rectangle__width'])

# When you define a Python class the execution engine creates a __dict__ attribute
# to store all of its methods and any class attributes you define as parts of it.
# Any instance attributes won't be included, as instance attributes are created only when objects are created.
print(Rectangle.__dict__)  # no attribute is included as Rectangle does not have any class attributes
# When appplied to an object, __dict__ attribute lists all instance
# (not class!) attributes and their values as (key,value) pairs.
print(rectangle1.__dict__)  # prints {'_Rectangle__length': 10, '_Rectangle__width': 5}

# As in case of protected attributes, accessing the class attribute "length" outside the class throws an error:
# AttributeError: 'Rectangle' object has no attribute 'length'
#print('rectangle1.length =', rectangle1.length)
# changing the class attribute "length" outside the class this way throws an error:
# AttributeError: 'Rectangle' object has no attribute 'length'
#rectangle1.length *= 20
# But changing the class attributes "length" and "width" outside the class this way does not throw an error or a warning:
rectangle1.length = 200
rectangle1.width = 100
# In fact the above two statements have included two additional instance attributes: length and width, to the object rectangle1.
# Therefore, now an attempt to access the class attributes "length" and "width" outside the class does not throw errors:
print('rectangle1.length =', rectangle1.length)
print('rectangle1.width =', rectangle1.width)
# Remember that in Python instance variables (like any variable) spring to existance just by assigning a value to them.
# To check, run the dir() function or __dict__ attribute for the object rectangle1:
print(dir(rectangle1))      # lists '_length', '_width', 'length' and 'width' instance attributes
print(rectangle1.__dict__)  # prints {'_Rectangle__length': 10, '_Rectangle__width': 5, 'length': 200, 'width': 100}

# accessing the class attribute "__length" outside the class throws an error:
# AttributeError: 'Rectangle' object has no attribute '__length'
# and issues a warning:
# Access to a protected member __length of a client class
#print('rectangle1.__length =', rectangle1.__length)

# changing the class attribute "__length" outside the class this way throws an error:
# AttributeError: 'Rectangle' object has no attribute '__length'
#rectangle1.__length *= 2
# but changing the class attribute "__length" outside the class this way does not throw an error;
# it issues a warning: Access to a protected member __length of a client class
rectangle1.__length = 300
# now an attempt to access the class attribute "__length" outside the class does not throw an error
# but issues a warning: Access to a protected member __length of a client class:
print('rectangle1.__length =', rectangle1.__length)
# As explained earlier, the above statement has included an additional instance attribute: __length, to the object rectangle1.
print(rectangle1.__dict__)  # prints {'_Rectangle__length': 10, '_Rectangle__width': 5, 'length': 200, 'width': 100, '__length': 300}

# however, there is still a way of accessing private attributes, despite being private -
# the two statements below work but produce warnings:
# Access to a protected member _Rectangle__length of a client class
# Access to a protected member _Rectangle__width of a client class
# Note: to display Warnings open the Assistant window (View > Assistant)

# Note that initial values of private class attributes __length and __width have not been changed:
print('rectangle1._Rectangle__length =', rectangle1._Rectangle__length)
print('rectangle1._Rectangle__width =', rectangle1._Rectangle__width)
# Thus, in the Rectangle class, the __length and __width attributes become _Rectangle__length and _Rectangle__width respectively.
# They can be accessed and changed from outside the class using the syntax: ObjName._ClassName__AttrName
# This feature of Python is called "name mangling". 
# Note: name mangling is all about safety and not security. 
# It will not keep you protected against intentional wrongdoing; just, accidental overriding. 
# In the example above, you can easily alter the value of a private attribute simply by doing this: 
rectangle1._Rectangle__length = 11
rectangle1._Rectangle__width = 6
# the two statements above produce warnings:
# Access to a protected member _Rectangle__length of a client class
# Access to a protected member _Rectangle__width of a client class

# the two statements below produce the same warnings, but reveal that
# the private attributes __length and __width have been changed outside the class, despite being private
print('rectangle1._Rectangle__length =', rectangle1._Rectangle__length)
print('rectangle1._Rectangle__length =', rectangle1._Rectangle__width)

# the following statement works but produces a warning:
# Access to a protected member __length of a client class
rectangle1.__length = 200
# the statements below produces the same warning
print('rectangle1.__length =', rectangle1.__length)
# the two statements below do not produce any error or warning, but are instead incuding two additional
# instance attributes: length and width to the object rectangle1, with values 300 and 100 respectively.
rectangle1.length = 300
rectangle1.width = 100
print('rectangle1.length =', rectangle1.length)
print(rectangle1.__dict__)  # prints {'_Rectangle__length': 11, '_Rectangle__width': 6, 'length': 300, 'width': 100, '__length': 200}

# the two statements below produce warnings:
# Access to a protected member _Rectangle__length of a client class
# Access to a protected member _Rectangle__width of a client class
# the private attributes __length and __width have been changed outside the class, despite being private
# but the private class attributes _Rectangle__length and _Rectangle__width remain unchanged:
print('rectangle1._Rectangle__length =', rectangle1._Rectangle__length)
print('rectangle1._Rectangle__width =', rectangle1._Rectangle__width)

# listing the methods of rectangle1 object, notice that now 'length' & 'width' are listed,
# along with '_Rectangle__length' & '_Rectangle__width' attributes, as well as __length.
# Assigning values to any new variables automatically includes them to the list of available
# attributes and methods for the object rectangle1.
print(dir(rectangle1))