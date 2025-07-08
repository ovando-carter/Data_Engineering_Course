class Trainee():
    # class attributes
    count_trainees = 0

    # constructor
    def __init__(self, trainee_id, first_name, last_name, date_joined, stream, weeks):
        self._trainee_id = trainee_id 
        self._first_name = first_name
        self._last_name = last_name
        self._email = (self._first_name.lower() + "." + self._last_name.lower() + "@fdmgroup.com")
        self.date_joined = date_joined
        self._date_left = None
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
        #getting values from dictionry
        #get all value from course and later put
        values = self.courses.values()
        values = list(values)
        total=0
        avarage = 0
        # calculate average
        for mark in  values:
            total = total + mark
            avarage= total/len(values)
        return(avarage)      

    @property
    def trainee_id(self):
        return self._trainee_id

    # trainee_id cannot be modified
    @trainee_id.setter
    def trainee_id(self, new_trainee_id):
        print("trainee_id cannot be modified")

    @property
    def email(self):
        return self._email

    # email cannot be modified
    @email.setter
    def sort_code(self, new_email):
        print("email cannot be modified")

    @property
    def date_left(self):
        return self._date_left

    # date_left cannot be modified
    @date_left.setter
    def date_left(self, new_date_left):
        print("date_left cannot be modified")
            
    # remove trainee count from the count_trainees and set the date they left
    def terminate_employment(self, date):
        self._date_left = date
        self.__class__.count_trainees -= 1
  

    @property
    def email(self):
        return self._email

    # email cannot be modified
    @email.setter
    def email(self, new_email):
        print("email cannot be modified")

    @property
    def first_name(self):
        return self._first_name

    # email can be modified here - first_name
    @first_name.setter
    def first_name(self, new_first_name):
        print('Setting first name to:', new_first_name)
        self._first_name = new_first_name
        self._email = (self._first_name.lower() + '.' + self._last_name.lower() + '@fdmgroup.com')
    
    @property
    def last_name(self):
        return self._last_name
    # email can be modified here - last_name
    @last_name.setter
    def last_name(self, new_last_name):
        print('Setting last name to:', new_last_name)
        self._last_name = new_last_name
        self._email = (self._first_name.lower() + '.' + self._last_name.lower() + '@fdmgroup.com')

