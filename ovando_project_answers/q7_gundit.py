
class Trainee:
    #class attribute
    count_trainees = 0
    #constructor
    def __init__(self,t_id,f_name,l_name,d_joined,s,w):#self, e_id, f_n, l_n,d_j,stream,weeks
        self._trainee_id = t_id
        self._first_name = f_name
        self._last_name = l_name
        self._email = (self._first_name.lower() + "." + self._last_name.lower() + "@fdmgroup.com")
        self.date_joined = d_joined
        self._date_left = None
        self.stream = s
        self.weeks = w
        self.courses = {}
        #self.__class__.count_trainees += 1
        return

    @classmethod
    def print_count(cls):
        print("The number of trainers is ", cls.count_trainees)
        pass
    
    


    #instance methods
    

    def assign_course(self, course):
        #check the length of couse and make sure it not exceed weeks
        if (len(self.courses)) < (self.weeks):
            self.courses[course] = 0
        else:
            print('No more courses can be added')
            
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



            
    #checks if course specified is in list of courses and prints the date:course
    def assign_training(self, date, course):
        if course in self.courses:
                self.trainings[date] = course
        else:
            print("The course", course, "does not exist in the list of courses for the trainer", self.trainer_id,self.first_name,self.last_name)
           
            
    #checks if date_left is date and removes 1 from count_trainers
    def terminate_employment(self, date):
        self.date_left = date
        
        if self.date_left is date:
            print("Trainer still working")
            self.__class__.count_trainees -=1
            


    def trainee_id(self):
        return self.___trainee_id

'''         
    # getter function
    @property
    def _trainee_id(self):
        print('Getting trainer ID:')
        return self.__name
    # setter function
    
    @_trainee_id.setter
    def _trainee_id(self, value):
        print('trainer id', value)
        self.__name = value
'''
            


'''
e_id = 25462
f_n = 'Mark'
l_n = 'Simpson'
d_j = '15-03-2020'
s = 'Data Engineering'
w = 7
emp_25462 = Trainee(e_id, f_n, l_n, d_j, s, w)

emp_25462.assign_course('Java')
emp_25462.assign_course('Python')
emp_25462.assign_course('Advanced Python')
emp_25462.assign_course('Hadoop & HDFS')
emp_25462.assign_course('Hive + Architecture & Data')
emp_25462.assign_course('Spark & PySpark')
emp_25462.assign_course('APM')
        
emp_25462.assign_mark_for_course('Java', 82)
emp_25462.assign_mark_for_course('Python', 100)
emp_25462.assign_mark_for_course('Advanced Python', 91)
emp_25462.assign_mark_for_course('Hadoop & HDFS', 92)
emp_25462.assign_mark_for_course('Hive + Architecture & Data', 78)
emp_25462.assign_mark_for_course('Spark & PySpark', 95)
emp_25462.assign_mark_for_course('APM', 85)
#print(emp_25462.__dict__)
#print(emp_25462.avg_mark())
print(emp_25462.trainee_id())
'''