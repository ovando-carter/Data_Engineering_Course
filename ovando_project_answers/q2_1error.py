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
    '''
    
    def assign_training(self, date, course, group):
        # loops through each entry in the list _courses
        for trainer_course in courses:
            # checks whether the course exist in trainer’s courses list 
            if course == trainer_course:
                key = course
                # adds the training to the dictionary trainings in the form of date: 
                # (course, group) if the date does not already exist as a key. 
                if key not in trainings:
                    #check if the date is in the list already then adds
                    self.trainings[self.date: (course, group)] = 0 
                else: 
                    print("The course ", course, " does not exsist in the list of courses for the trainer " + self.trainer_id + " " + self.first_name.lower() + " " + self.last_name )
    
'''
    def assign_training(self, date_joined, course):
        if course not in self.courses:
            print("The course ", course, " does not exsist in the list of courses for the trainer " + self.trainer_id + " " + self.first_name.lower() + " " + self.last_name )
        else:
            #check if the date is in the list already then adds
            #self.trainings[self.date_joined: (x, group)] = 0  
            new_key = self.date_joined
            new_value = course
            self.trainings[new_key] = new_value




'''
        # checks whether the course exist in trainer’s courses list
        if course == self.courses:
                key = self.date_joined
                # adds the training to the dictionary trainings in the form of date: 
                # (course, group) if the date does not already exist as a key. 
                if key not in trainings:
                    #check if the date is in the list already then adds
                    #self.trainings[self.date_joined: (x, group)] = 0  
                    new_key = self.date_joined
                    new_value = course
                    self.trainings[new_key] = new_value
                else: 
                    print("The course ", course, " does not exsist in the list of courses for the trainer " + self.trainer_id + " " + self.first_name.lower() + " " + self.last_name )
 
    '''        
    '''
    group = ['6', '5', '7']

    def assign_training(self, date_joined, course, group):
        # loops through each entry in the list _courses
        for x in course:
            key = self.date_joined
            # checks whether the course exist in trainer’s courses list
            # adds the training to the dictionary trainings in the form of date: 
            # (course, group) if the date does not already exist as a key. 
            if (x == trainer_course) and (key not in trainings):
                #check if the date is in the list already then adds
                #self.trainings[self.date_joined: (x, group)] = 0  
                new_key = self.date_joined
                new_value = x 
                self.trainings[new_key] = new_value
            else: 
                print("The course ", course, " does not exsist in the list of courses for the trainer " + self.trainer_id + " " + self.first_name.lower() + " " + self.last_name )
'''
                   

    def terminate_employment(self, date_left):
        
        if self.date_left is None:
            print('This trainer has not terminated employment')
        else:
            # decrement the no_accounts by 1 and close the account (by deleting the account holder) 
            self.__class__.count_trainers -= 1
            print('The bank account ' + str(self.account_number) + ' has been closed.')
            del(self)


'''
emp_17639 = Trainer(99080, 'Ovando', 'Carter', '06-06-2022')
emp_17639.assign_course('Excel')
emp_17639.assign_course('Hadoop & HDFS')
emp_17639.assign_course('Hive + Architecture & Data')
emp_17639.assign_course('Spark & PySpark')

print(emp_17639.__dict__)
'''