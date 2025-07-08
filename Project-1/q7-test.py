"""
  #####                                               #######  
 #     # #    # ######  ####  ##### #  ####  #    #         # 
 #     # #    # #      #        #   # #    # ##   #        # 
 #     # #    # #####   ####    #   # #    # # #  #       #  
 #   # # #    # #           #   #   # #    # #  # #      #       
 #    #  #    # #      #    #   #   # #    # #   ##     #       
  #### #  ####  ######  ####    #   #  ####  #    #    #
                                                               
 #     #                   #######                             
 #     # #    # # #####       #    ######  ####  #####  ####   
 #     # ##   # #   #         #    #      #        #   #       
 #     # # #  # #   #         #    #####   ####    #    ####   
 #     # #  # # #   #         #    #           #   #        #  
 #     # #   ## #   #         #    #      #    #   #   #    #  
  #####  #    # #   #         #    ######  ####    #    ####   

"""
FILE = 'q7'       # Do NOT Include the .py
CLASS = 'Trainee'

import os
import sys
import unittest

# Do not show the Traceback error
__unittest = True

# Check if the user has put their code in the correct file name
print('----------------------------------------------------------------------')
if not os.path.isfile(FILE+'.py'):
    print('The file "'+FILE+'.py" does not exist')
    print('\nFAILED (errors=1)')
    sys.exit(2)

# Check that there are no unreadable characters within the file
f = open(FILE+'.py', 'r')
try:
    text = f.read().replace(' ', '')
except:
    print("Error reading file "+FILE+'.py'+"\nMake sure there are no styled characters, such as single/double quotes or dash symbols.\nPython does not recognise such characters.")
    f.close()
    sys.exit(3)

# Check if the class name is correct 
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if 'class'+CLASS not in text:
    print('The class "'+CLASS+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)

# If the class exists but does not import then there are syntax errors
try:
    from q7 import Trainee as test_class
except:
    print('The class "'+CLASS+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(5)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False
        
    # explanation used for testing an object and displaying the object's instance attributes to which a value has been assigned
    def explanation_1(self, e_id, f_n, l_n, d_j, s, w, output, result):
        message = CLASS+'('+str(e_id)+', '+f_n+', '+l_n+', '+d_j+', '+s+', '+str(w)+')'
        message = message+'\nFor input values:\n'+str(e_id)+', '+f_n+', '+l_n+', '+d_j+', '+s+', '+str(w)+'\nthe output is:\n'+str(output)+'\nYou returned '+str(result)
        return message

    # explanation used for testing a specified class attribute and displaying its value
    def explanation_2(self, cl, attr, output, result):
        message = 'class '+str(cl)+':'
        message = message+'\nFor attribute "'+attr+'" the output is '+str(output)+' - You returned '+str(result)
        return message
    
    # explanation used for testing a specified object's instance attribute and displaying its value
    def explanation_3(self, obj, attr, output, result):
        message = 'object '+obj + ':'
        message = message+'\nFor attribute "'+attr+'" the output is '+str(output)+' - You returned '+str(result)
        return message

    # explanation used for testing a specified object's instance method that returns a value
    def explanation_4(self, obj, method, arguments, output, result):
        message = 'object '+obj+'; method '+method+'():'
        message = message+'\nFor arguments: '+str(arguments)+'\nthe output is:\n'+str(output)+'\n- You returned:\n'+str(result)
        return message

    # explanation used for testing a specified object's instance method that sets a value of an attribute
    def explanation_5(self, obj, method, arguments, attr, output, result):
        message = 'object '+obj+'; method '+method+'():'
        message = message+'\nFor input value(s):\n'+str(arguments)+'\nthe value of attribute "'+str(attr)+'" is\n'+str(output)+'\n- You returned:\n'+str(result)
        return message

    def test_trainee_class(self):
        # test employing 1st trainee
        # --------------------------
        msg = "test employing 1st trainee:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        e_id = 25462
        f_n = 'Mark'
        l_n = 'Simpson'
        d_j = '15-03-2020'
        s = 'Data Engineering'
        w = 7
        output = {'_trainee_id': 25462, '_first_name': 'Mark', '_last_name': 'Simpson', '_email': 'mark.simpson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': None, 'stream': 'Data Engineering', 'weeks': 7, 'courses': {}}
        emp_25462 = test_class(e_id, f_n, l_n, d_j, s, w)
        message = self.explanation_1(e_id, f_n, l_n, d_j, s, w, output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test count_trainees class attribute
        msg = "test count_trainees class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 1
        result = test_class.count_trainees
        message = self.explanation_2(test_class, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing print_count() method
        msg = "testing print_count() method - after 1st trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()

        # test assign_course() method
        msg = "testing assign_course() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.assign_course('Java')
        emp_25462.assign_course('Python')
        emp_25462.assign_course('Advanced Python')
        emp_25462.assign_course('Hadoop & HDFS')
        emp_25462.assign_course('Hive + Architecture & Data')
        emp_25462.assign_course('Spark & PySpark')
        emp_25462.assign_course('APM')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25462', 'assign_course', "'Java', 'Python', 'Advanced Python', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark', 'APM'", 'courses', output, emp_25462.courses)
        self.assertEqual(output, emp_25462.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # trying to assign more courses than the number of weeks produces a warning
        msg = "trying to assign more courses than the number of weeks:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.assign_course('Project Week')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25462', 'assign_course', "'Project Week'", 'courses', output, emp_25462.courses)
        self.assertEqual(output, emp_25462.courses, msg=message)

        # test assign_mark_for_course() method
        msg = "testing assign_mark_for_course() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.assign_mark_for_course('Java', 82)
        emp_25462.assign_mark_for_course('Python', 100)
        emp_25462.assign_mark_for_course('Advanced Python', 91)
        emp_25462.assign_mark_for_course('Hadoop & HDFS', 92)
        emp_25462.assign_mark_for_course('Hive + Architecture & Data', 78)
        emp_25462.assign_mark_for_course('Spark & PySpark', 95)
        emp_25462.assign_mark_for_course('APM', 85)
        output = {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}
        message = self.explanation_5('emp_25462', 'assign_mark_for_course', "82, 100, 91, 92, 78, 95, 85", 'courses', output, emp_25462.courses)
        self.assertEqual(output, emp_25462.courses, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test avg_mark() method
        msg = "testing avg_mark() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 89.0
        result = round(emp_25462.avg_mark(), 2)
        message = self.explanation_4('emp_25462', 'avg_mark', list(emp_25462.courses.values()), output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test employing 2nd trainee
        # --------------------------
        msg = "test employing 2nd trainee:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        e_id = 25475
        f_n = 'Fatima'
        l_n = 'Farah'
        d_j = '16-03-2018'
        s = 'Data Engineering'
        w = 7
        output = {'_trainee_id': 25475, '_first_name': 'Fatima', '_last_name': 'Farah', '_email': 'fatima.farah@fdmgroup.com', 'date_joined': '16-03-2018', '_date_left': None, 'stream': 'Data Engineering', 'weeks': 7, 'courses': {}}
        emp_25475 = test_class(e_id, f_n, l_n, d_j, s, w)
        message = self.explanation_1(e_id, f_n, l_n, d_j, s, w, output, emp_25475.__dict__)
        self.assertEqual(output, emp_25475.__dict__, msg=message)
        print("\033[0;31;48m ok\n")
        
        
        # test count_trainees class attribute
        msg = "testing count_trainees class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 2
        result = test_class.count_trainees
        message = self.explanation_2(test_class, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing print_count() method
        msg = "testing print_count() method - after 2nd trainee joined:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()

        # test assign_course() method
        msg = "test assign_course() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25475.assign_course('Java')
        emp_25475.assign_course('Python')
        emp_25475.assign_course('Advanced Python')
        emp_25475.assign_course('Hadoop & HDFS')
        emp_25475.assign_course('Hive + Architecture & Data')
        emp_25475.assign_course('Spark & PySpark')
        emp_25475.assign_course('APM')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25475', 'assign_course', "'Java', 'Python', 'Advanced Python', 'Hadoop & HDFS', 'Hive + Architecture & Data', 'Spark & PySpark', 'APM'", 'courses', output, emp_25475.courses)
        self.assertEqual(output, emp_25475.courses, msg=message)
        print("\033[0;31;48m ok\n")
                
        # trying to assign more courses than the number of weeks produces a warning
        msg = "trying to assign more courses than the number of weeks:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25475.assign_course('Project Week')
        output = {'Java': 0, 'Python': 0, 'Advanced Python': 0, 'Hadoop & HDFS': 0, 'Hive + Architecture & Data': 0, 'Spark & PySpark': 0, 'APM': 0}
        message = self.explanation_5('emp_25475', 'assign_course', "'Project Week'", 'courses', output, emp_25475.courses)
        self.assertEqual(output, emp_25475.courses, msg=message)
                
        # test assign_mark_for_course() method
        msg = "testing assign_mark_for_course() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25475.assign_mark_for_course('Java', 78)
        emp_25475.assign_mark_for_course('Python', 90)
        emp_25475.assign_mark_for_course('Advanced Python', 91)
        emp_25475.assign_mark_for_course('Hadoop & HDFS', 81)
        emp_25475.assign_mark_for_course('Hive + Architecture & Data', 86)
        emp_25475.assign_mark_for_course('Spark & PySpark', 94)
        emp_25475.assign_mark_for_course('APM', 77)
        output = {'Java': 78, 'Python': 90, 'Advanced Python': 91, 'Hadoop & HDFS': 81, 'Hive + Architecture & Data': 86, 'Spark & PySpark': 94, 'APM': 77}
        message = self.explanation_5('emp_25475', 'assign_mark_for_course', list(emp_25475.courses.values()), 'courses', output, emp_25475.courses)
        self.assertEqual(output, emp_25475.courses, msg=message)
        print("\033[0;31;48m ok\n")
               
        # test avg_mark() method
        msg = "testing avg_mark() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 85.29
        result = round(emp_25475.avg_mark(), 2)
        message = self.explanation_4('emp_25475', 'avg_mark', list(emp_25475.courses.values()), output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # test terminate_employment() method
        msg = "testing terminate_employment() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.terminate_employment('12-07-2021')
        output = '12-07-2021'
        result = emp_25462.date_left
        message = self.explanation_5('emp_25462', 'terminate_employment', '12-07-2021', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing print_count() method
        msg = "testing print_count() method - after 1st trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()
        
        # testing trainee_id's getter
        msg = "testing trainee_id's getter"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 25462
        result = emp_25462.trainee_id
        message = self.explanation_3('emp_25462', 'trainee_id', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # testing that trainee_id is read only
        msg = "testing that trainee_id is read only - trying to change trainee_id by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25475.trainee_id = 32475       
        output = 25475
        result = emp_25475.trainee_id
        message = self.explanation_3('emp_25475', 'trainee_id', output, result)
        self.assertEqual(output, result, msg=message)
        
        # testing that first & last name can be shanged
        # through the setter only (updating the email accordingly)
        # 1. change the first_name only
        msg = "testing that first & last name can be changed\n1) changing the first_name only:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.first_name = 'Marcus'
        output = {'_trainee_id': 25462, '_first_name': 'Marcus', '_last_name': 'Simpson', '_email': 'marcus.simpson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1(25462, 'Marcus', 'Simpson', '15-03-2020', 'Data Engineering', 7, output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok")       
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")
        
        # 2. change the last_name only
        msg = "2) changing the last_name only:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.last_name = 'Sampson'
        output = {'_trainee_id': 25462, '_first_name': 'Marcus', '_last_name': 'Sampson', '_email': 'marcus.sampson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1(25462, 'Marcus', 'Sampson', '15-03-2020', 'Data Engineering', 7, output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok")       
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")
        
        # 3. change both first_name and last_name
        # 3a. changing the first_name before the last_name
        msg = "3) changing both first_name and last_name"
        msg = "3a) changing both but the first_name before the last_name:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.first_name = 'Marc'
        emp_25462.last_name = 'Samson'
        output = {'_trainee_id': 25462, '_first_name': 'Marc', '_last_name': 'Samson', '_email': 'marc.samson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1(25462, 'Marc', 'Samson', '15-03-2020', 'Data Engineering', 7, output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok")       
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")

        # 3b. changing the last_name before the first_name
        msg = "3b) changing both but the last_name before the first_name:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25462.last_name = 'Simson'
        emp_25462.first_name = 'Mark'
        output = {'_trainee_id': 25462, '_first_name': 'Mark', '_last_name': 'Simson', '_email': 'mark.simson@fdmgroup.com', 'date_joined': '15-03-2020', '_date_left': '12-07-2021', 'stream': 'Data Engineering', 'weeks': 7, 'courses': {'Java': 82, 'Python': 100, 'Advanced Python': 91, 'Hadoop & HDFS': 92, 'Hive + Architecture & Data': 78, 'Spark & PySpark': 95, 'APM': 85}}
        message = self.explanation_1(25462, 'Mark', 'Simson', '15-03-2020', 'Data Engineering', 7, output, emp_25462.__dict__)
        self.assertEqual(output, emp_25462.__dict__, msg=message)
        print("\033[0;31;48m ok")       
        #print("\033[1;32;40m" + emp_25462.first_name, emp_25462.last_name, emp_25462.email + "\033[0m")
        
        # check that email is read only
        msg = "trying to change email by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.email = 'dummy_email@dummydomain.com'
        output = 'mark.simson@fdmgroup.com'
        result = emp_25462.email
        message = self.explanation_3('emp_25462', 'email', output, result)
        self.assertEqual(output, result, msg=message)
                
        # testing that date_left's getter works
        msg = "testing that date_left's getter works"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = '12-07-2021'
        result = emp_25462.date_left
        message = self.explanation_3('emp_25462', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")
        
        # check that date_left is read only
        msg = "trying to change date_left by the object:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m", end='')
        # for a trainee that has left
        msg = "- for a trainee that has left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25462.date_left = '31-12-2030'
        output = '12-07-2021'
        result = emp_25462.date_left
        message = self.explanation_3('emp_25462', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        # for a trainee that has not left        
        msg = "- for a trainee that has not left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        emp_25475.date_left = '31-12-2030'
        output = None
        result = emp_25475.date_left
        message = self.explanation_3('emp_25475', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        
        # test terminate_employment() method
        msg = "testing terminate_employment() method"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        emp_25475.terminate_employment('31-01-2022')
        output = '31-01-2022'
        result = emp_25475.date_left
        message = self.explanation_5('emp_25475', 'terminate_employment', '31-01-2022', 'date_left', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")

        # test count_trainees class attribute
        msg = "testing count_trainees class attribute"
        print()
        print("\033[1;32;40m" + msg + "\033[0m" + "\033[0;31;48m ...", end='')
        output = 0
        result = test_class.count_trainees
        message = self.explanation_2(test_class, 'count_trainees', output, result)
        self.assertEqual(output, result, msg=message)
        print("\033[0;31;48m ok\n")

        # testing print_count() method
        msg = "testing print_count() method - after 2nd trainee left:"
        print()
        print("\033[1;32;40m" + msg + "\033[0m")
        test_class.print_count()
                

if __name__ == '__main__':
    unittest.main(verbosity=2)
