from abc import ABC, abstractmethod

# create a class Employee as parent of the classes Trainer
class Employee(ABC):

    # class attributes
    company = 'FDM'
    countemployees = 0

    # The class Employee should not be instantiable
    # constructor
    '''
    def __init__(self):
        raise TypeError("cannot create 'Employee' instances")
    '''
    
    def __init__(self, employeeid, firstname, lastname, datejoined):
        
        # instance parameters and attributes
        self.employee_id = employeeid
        self._first_name = firstname
        self._last_name = lastname
        self._email = (self._first_name.lower() + "." + self._last_name.lower() + "@fdmgroup.com")
        self.date_joined = datejoined
        self._date_left = None
        self.stream = stream
        self.weeks = weeks
        self.courses = {}
        self.__class__.count_employees += 1
        return
    
'''
    # not sure about
    # the number of FDM trainers (if called by Trainer class)
    trainer = Trainer(employeeid, firstname, lastname, datejoined, trainee_id, courses, trainings)
    tr = trainer.print_count(cls)

    # the number of FDM trainees (if called by Trainer class)
    trainee = Trainee(employeeid, firstname, lastname, datejoined, trainee_id, stream, weeks)
    te = trainee.print_count(cls)
'''

    ############################################################################################################################################################################
    # Everything that is in both q2.py and q7.py
    ############################################################################################################################################################################
    
    @classmethod
        def print_count(cls):
            print("The number of employees is ", cls.count_employees)

    # instance methods
    
    # company (read-only and set to FDM Group)
    @property
    def company(self):
        return company
    
    @company.setter
    def company(self, new_company):
        print("company cannot be modified")

    # Define the employee_id’s getter and setter as abstract methods to enforce 
    # their implementation in Trainer and Trainee classes
    @property
    def employee_id(self):
        return self.employee_id

    @employee_id.setter
    def employee_id(self, newemployee_id):
        print("employee_id cannot be modified")

    # abstract methods
    @abstractmethod
    def assign_course(self):
        pass

    @abstractmethod
    def assign_training(self):
        pass
                   
    @abstractmethod
    def terminate_employment(self):
        pass


    


    

############################################################################################################################################################################
# Everything only in q2.py 
############################################################################################################################################################################
     
 
# Trainer and Trainee are children of Employee.
class Trainer(Employee):
    def __init__(self, employeeid, firstname, lastname, datejoined, trainer_id, courses, trainings):

        # class attributes
        count_trainees = 0

        # constructor
        super().__init__(trainer_id, courses, trainings)
        self.trainer_id = trainer_id
        self.courses = []
        self.trainings = {}
        self.__class__.count_trainers += 1    
        return     
        
        # I don't know how to move this to employees and still have its functionality. 
        @classmethod
        def print_count(cls):
            print("The number of trainers is ", cls.count_trainers) # i don't understand this - Trainer.__name__

        # instance methods
        # assigning the cours is different for trainer and trainee
        def assign_course(self, course):
            self.courses.append(course)

        # assign training is different for trainer and traineer, the trainee only has course
        def assign_training(self, date, course,group):
            if course not in self.courses:
                print("The course ", course, " does not exsist in the list of courses for the trainer " + str(self.trainer_id) + " " + self.first_name + " " + self.last_name )
            else: 
                self.trainings[date] = course,group
                            
        def terminate_employment(self, date): 
            # if the person is leaving on this date, we are updating 
            # the system from None to that specific date
            self.date_left = date
            
            #then we remove the trainer from the count of trainers
            self.__class__.count_trainers -=1

    def train(self):
        print("This is subclass - training")


############################################################################################################################################################################
# Everything only in q7.py 
############################################################################################################################################################################

# The file q12.py will include Employee, Trainer and Trainee classes.
class Trainee(Employee):    
    
        
    def __init__(self, employeeid, firstname, lastname, datejoined, trainee_id, stream, weeks):

        # class attributes
        count_trainees = 0

        # constructor
        super().__init__(trainee_id, stream, weeks)
        self._trainee_id = trainee_id
        self.stream = stream
        self.weeks = weeks
        self.courses = {}
        self.__class__.count_trainees += 1
        return   
            
        @classmethod
        def print_count(cls):
            print("The number of trainees is ", cls.count_trainees)
            pass

        # instance methods
        # assigning the cours is different for trainer and trainee
        def assign_course(self, course):
            if (len(self.courses)) < (self.weeks):
                self.courses[course] = 0
            else: 
                print("no more courses can be added")

        # assign a mark for the course
        def assign_mark_for_course(self, mark, course):
            if mark in self.courses:
                self.courses[mark] = course
                
                
        def avg_mark(self):
            #getting valuse from dictionry
            #get all value from course and later put
            values = self.courses.values()
            values = list(values)
            total=0
            avarage = 0
            for mark in  values:
                total = total + mark
                avarage= total/len(values)
            return(avarage)

        # assign training is different for trainer and traineer, the trainer has course,group
        def assign_training(self, date, course,group):
            if course in self.courses:
                    self.trainings[date] = course
            else:
                print("The course", course, "does not exist in the list of courses for the trainer", self._trainee_id,self.first_name,self.last_name)
                
        @property
        def trainee_id(self):
            return self._trainee_id

        @trainee_id.setter
        def trainee_id(self, new_trainee_id):
            print("trainee_id cannot be modified")

        
        def assign_course(self, course):
            self.courses.append(course)

        def assign_training(self, date, course,group):
            if course not in self.courses:
                print("The course ", course, " does not exsist in the list of courses for the trainer " + str(self.trainer_id) + " " + self.first_name + " " + self.last_name )
            else: 
                self.trainings[date] = course,group
                    

        def terminate_employment(self, date):
            self.date_left = date
            self.__class__.count_trainers -=1

        @property
        def email(self):
            return self.email

        @email.setter
        def sort_code(self, newemail):
            print("email can be modified only through changing the first_name or last_name of an employee")

        @property
        def date_left(self):
            return self.date_left

        @date_left.setter
        def date_left(self, newdate_left):
            print("date_left cannot be modified directly by any employee; date_left can be set only through terminate_employment() method")
        
        @property
        def first_name(self):
            return self.first_name

        @first_name.setter
        def first_name(self, newfirst_name):
            print('Setting first name to:', newfirst_name)
            self.first_name = newfirst_name
            self.email = (self.first_name.lower() + '.' + self.last_name.lower() + '@fdmgroup.com')
                
        @property
        def last_name(self):
            return self.last_name
                
        @last_name.setter
        def last_name(self, newlast_name):
            print('Setting last name to:', newlast_name)
            self.last_name = newlast_name
            self.email = (self.first_name.lower() + '.' + self.last_name.lower() + '@fdmgroup.com')



    def learns(self):
        print("This is subclass - learning")  

print(Employee())