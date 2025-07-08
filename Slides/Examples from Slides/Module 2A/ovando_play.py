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