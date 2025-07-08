class Trainer():
    # class attributes
    count_trainers = 0

    # constructor
    def __init__(self, trainer_id, first_name, last_name, date_joined):
        self.trainer_id = trainer_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_joined = date_joined
        self.email = (self.first_name.lower() + "." + self.last_name.lower() + "@fdmgroup.com")
        self.date_left = None
        self.courses = []
        self.trainings = {}
        self.__class__.count_trainers += 1
        return
        
    @classmethod
    def print_count(cls):
        print("The number of trainers is ", cls.count_trainers)
    
    # instance methods
    def assign_course(self, course):
        self.courses.append(course)

    # assign training 
    def assign_training(self, date, course,group):
        # check if course is in courses then add it the the trainings dictionary
        if course in self.courses:
                self.trainings[date] = course,group
        # if it is not then tell the user that it dose not exsist.
        else:
            print("The course ", course, " does not exsist in the list of courses for the trainer " + str(self.trainer_id) + " " + self.first_name + " " + self.last_name )
                

    def terminate_employment(self, date): 
        # if the person is leaving on this date, we are updating 
        # the system from None to that specific date
        self.date_left = date
        
        #then we remove the trainer from the count of trainers
        self.__class__.count_trainers -=1

    
