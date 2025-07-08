# example of a class with private methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length  # public attribute
        self.width = width    # public attribute
        
    # private methods
    def __isValidLength(self, length):
        return length >= 0
    def __isValidWidth(self, width):
        return width >= 0
 
    # public method calling private methods
    def area(self, length, width):
        if self.__isValidLength(length) and self.__isValidWidth(width):
            return length * width
        else:
            return None

# By convention, the double underscore prefix for a method marks it as private
# (and therefore cannot be accessed outside a class method).

rectangle1 = Rectangle(10, 5)

# accessing the class method "isValidLength" outside the class throws an error:
# throws AttributeError: 'Rectangle' object has no attribute 'isValidLength'
#print(rectangle1.isValidLength(100))

# accessing the class method "__isValidLength" outside the class throws an error:
# throws AttributeError: 'Rectangle' object has no attribute '__isValidLength'
#print(rectangle1.__isValidLength(100))

# However, private methods can be accessed by calling the private methods via public methods
# (no errors or warnings are issued)
print(rectangle1.area(10, 5))

# calling a private method through name mangling works
# but issues a warning:
# Access to a protected member _Rectangle__isValidLength of a client class
print(rectangle1._Rectangle__isValidLength(100))
# Note: Warnings are visible only in the Assistant window.