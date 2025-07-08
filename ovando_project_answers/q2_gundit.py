class Trainer():
    # class attributes
    count_trainers = 0

    # constructor
    def __init__(self,t_id,f_name,l_name,d_joined):
        self.trainer_id = t_id
        self.first_name = f_name
        self.last_name = l_name
        self.date_joined = d_joined
        self.email = (self.first_name.lower() + "." + self.last_name.lower() + "@fdmgroup.com")
        self.date_left = None
        self.courses = []
        self.trainings = {}
        
        # when count trainer + 1 to exist trainer
        self.__class__.count_trainers += 1
        return
    
    @classmethod
    def print_count(cls):
        print("The number of trainers is ", cls.count_trainers)
    

    # instance methods
    def assign_course(self, course):
            self.courses.append(course)
    
    
    def assign_training(self, date, course):
        if course in self.courses:
                self.trainings[date] = course
        else:
            print("The course", course, "does not exist in the list of courses for the trainer", self.trainer_id,self.first_name,self.last_name)            


    def terminate_employment(self, date):
        self.date_left = date
        
        if self.date_left is date:
            print("Trainer still working")
            self.__class__.count_trainers -=1
            
    def close_account(self):
        if self._balance != 0:
            print('The bank account ' + str(self.account_number) + ' cannot be closed, as its balance is ' + str(self._balance) + ' GBP')
        else:
            # decrement the no_accounts by 1 and close the account (by deleting the account holder) 
            self.__class__.no_accounts -= 1
            print('The bank account ' + str(self.account_number) + ' has been closed.')
            del(self)         
       
'''
    def assign_training(self, date, course):
        # loops through each entry in the list _courses
        for trainer_course in _courses:
            # checks whether the course exist in trainer’s courses list 
            if course == trainer_course:
                key = date
                # adds the training to the dictionary trainings in the form of date: 
                # (course, group) if the date does not already exist as a key. 
                if key not in _trainings:
                    #check if the date is in the list already then adds
                    self._trainings[self.date: (course, group)] = 0
                    new_key = self.date_join
                    new_value=x
                    self.trainings[self.date_join] = assign_course
   '''             


            
    
'''

e_id = 17639
f_n = 'Elena'
l_n = 'Rostova'
d_j = '04-05-2016'
sample_dict={}
new_key = 'John'
new_value = 100
sample_dict[new_key] = new_value
print(sample_dict)    

emp_16384 = Trainer(e_id, f_n, l_n, d_j)
emp_17639 = Trainer(e_id, f_n, l_n, d_j)
emp_17639.assign_course('Excel')
emp_17639.assign_course('Hadoop & HDFS')
emp_17639.assign_course('Hive + Architecture & Data')
emp_17639.assign_course('Spark & PySpark')
emp_17639.assign_training('13/06/2022', 'Hadoop & HDFS')

print(emp_17639.__dict__)
'''
'''
e_id = 17639
f_n = 'Elena'
l_n = 'Rostova'
d_j = '04-05-2016'
    
    
trainee_Lucy = (Trainer(9080,'Ovando', 'Carter', '06/06/2022'))
trainee_Lucy.courses
#trainee_Lucy.assign_course('SQL')
#print(trainee_Lucy.courses)

#print(Trainer(9080, 'Ovando', 'Carter', '06/06/2022'))


class Trainer():
    # class attributes
    no_accounts = 0
    
    # constructor
    def __init__(self, trainer_id, first_name, last_name, date_joined):
        self._trainer_id = trainer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = first_name + "." + last_name + "@fdmgroup.com"
        self._date_joined = date_joined
        self._date_left = None
        self._courses = []
        self._trainings = {}
        self.__class__.no_accounts += 1
        print('email', self._email)
'''
'''
'''
