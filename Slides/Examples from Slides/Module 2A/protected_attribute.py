# example of a class with protected attributes
class Rectangle:
    def __init__(self, length, width):
        self._length = length  # protected attribute
        self._width = width    # protected attribute

# By convention, the underscore prefix for an instance variable marks it as protected
# (and therefore cannot be accessed outside the class and its child classes).

rectangle1 = Rectangle(10, 5)

print('rectangle1._length =', rectangle1._length)  # returns 10
print('rectangle1._width =', rectangle1._width)   # returns 5
# dir(Rectangle) list no attribute as Rectangle does not have any class attribute
# (when applied to a class, dir lists all available class attributes and methods for that class).
print(dir(Rectangle))
# dir(rectangle1) lists both _length and _width instance attributes, as the object rectangle1
# was created with initialising both of its instance attributes _length and _width).
# Remember that instance attributes are created at the point when a value is assigned to them.
# The class Student uses the __init__() constructor, which initialises both instance attributes.
print(dir(rectangle1))      # lists '_length' and '_width' instance attributes
# accessing the class attribute "length" outside the class throws an error:
# AttributeError: 'Rectangle' object has no attribute 'length'
#print('rectangle1.length =', rectangle1.length)

# changing the class attribute "length" outside the class this way throws an error:
# AttributeError: 'Rectangle' object has no attribute 'length'
#rectangle1.length *= 2
# because rectangle1.length *= 2 <=> rectangle1.length = rectangle1.length * 2, but since rectangle1.length does
# not exist, its appearance on the right hand side of the equation throws an error.
# But changing the class attributes "length" and "width" outside the class this way does not throw errors or warnings:
rectangle1.length = 200
rectangle1.width = 100
# In fact the above two statements have included two additional instance attributes: length and width, to the object rectangle1.
# Therefore, now an attempt to access the class attributes "length" and "width" outside the class does not throw errors:
print('rectangle1.length =', rectangle1.length)
print('rectangle1.width =', rectangle1.width)
# Remember that in Python instance variables (like any variable) spring to existance just by assigning a value to them.
# To check, run the dir() function or __dict__ attribute for the object rectangle1:
print(dir(rectangle1))      # lists '_length', '_width', 'length' and 'width' instance attributes
print(rectangle1.__dict__)  # prints {'_length': 10, '_width': 5, 'length': 200, 'width': 100}

# the protected instance attributes _length and _width stil maintained their original values: 10 and 5 respectively
print('rectangle1._length =', rectangle1._length)
print('rectangle1._width =', rectangle1._width)

# accessing the class attributes "_length" and "_width" outside the class does not throw any error
# but throws warnings:
# Access to a protected member _length of a client class
# Access to a protected member _width of a client class
# class attributes _length and _width remain unchanged:
# Note: to display Warnings open the Assistant window (View > Assistant)

# changing the class attribute "_length" outside the class this way does not throw an error or a warning:
rectangle1._length *= 2  # now _length = 20
print('rectangle1._length =', rectangle1._length)
# changing the class attributes "_length" and "_width" outside the class this way does not throw errors
# but throws warnings:
# Access to a protected member _length of a client class
# Access to a protected member _width of a client class

# Despite being marked as protected (through inclusion of the underscore prefix), it is still  possible
# to change and access variables _length and _width; this is just a convention rather than a mechanism
# that effectively restricts access to any instance variable
rectangle1._length = 200
rectangle1._width = 100
# accessing the class attributes "_length" and "_width" outside the class still does not throw errors
# but throws warnings:
# Access to a protected member _length of a client class
# Access to a protected member _width of a client class

# class attributes _length and _width have been changed:
print('rectangle1._length =', rectangle1._length)
print('rectangle1._width =', rectangle1._width)

