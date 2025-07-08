# example of a class with protected methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length  # public attribute
        self.width = width    # public attribute
        
    # protected methods
    def _isValidLength(self, length):
        return length >= 0
    def _isValidWidth(self, width):
        return width >= 0
 
    # public method calling protected methods
    def area(self, length, width):
        if self._isValidLength(length) and self._isValidWidth(width):
            return length * width
        else:
            return None

# By convention, the underscore prefix for a method marks it as protected
# (and therefore cannot be accessed outside the class and its child classes).

rectangle1 = Rectangle(10, 5)

# The following statement throws AttributeError: 'Rectangle' object has no attribute 'isValidLength'
#print(rectangle1.isValidLength(100))

# The following statement works but throws a warning: Access to a protected member _isValidLength of a client class
print(rectangle1._isValidLength(100))
# Note: Warnings are visible only in the Assistant window.

# However, protected methods can be accessed by calling the protected methods via public methods
# (no errors or warnings are issued)
print(rectangle1.area(10, 5))
