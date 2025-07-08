# slide 90 - Activity 5b
'''
Create a copy of the Activity 4b script created earlier and
rename it to Activity 5b.
Add a static method interest() to the BankAccount class, that
accepts the starting balance, interest rate and time period,
and returns the predicted interest calculated as:
starting balance * interest rate * time period.
Then add an instance method calc_interest() that accepts the
number of years and uses the static method interest() to
return the predicted interest earned by an account holder
over the specified number of years.
Test the two new methods from the main() function by
calculating the predicted interest of the account holder
with the highest balance over 1, 3 and 5 years.
'''
class BankAccount():
    # class attributes
    no_accounts = 0
    __annual_interest_rate = 0.001
    
    # constructor
    def __init__(self, acc_no, sort_code, name, amount):
        self._account_number = acc_no
        self._sort_code = sort_code
        self._name = name
        self._balance = amount
        self.transactions = []
        self.__class__.no_accounts += 1
        print('New bank account opened for', self._name)

    @property
    def annual_interest_rate(self):
        return self.__class__._BankAccount__annual_interest_rate
        

    @annual_interest_rate.setter
    def annual_interest_rate(self, new_value):
        print("The annual interest rate can be modified only via the set_annual_interest_rate() method.")
        
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, new_acc_number):
        print("account_number cannot be modified")

    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, new_sort_code):
        print("sort_code cannot be modified")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        print("name cannot be modified")
        
    @property
    def balance(self):
        print("Use the get_balance() method to obtain account holder's current balance.")

    @balance.setter
    def balance(self, new_balance):
        print("balance cannot be modified directly. Use make_transaction() method.")

    @classmethod
    def print_no_accounts(cls):
        print("The number of openned accounts is:", cls.no_accounts)
        
    @classmethod
    def set_annual_interest_rate(cls, new_annual_interest_rate):
        cls._BankAccount__annual_interest_rate = new_annual_interest_rate
        print('New annual interest rate set to', new_annual_interest_rate)

    # instance methods
    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self.transactions

    def make_transaction(self, amount):
        if type(amount) not in (int, float):
            print('The amount must be an integer or float value')
        else:
            self._balance += amount 
            self.transactions.append(amount)           

    def num_transactions(self):
        return len(self.transactions)

    def close_account(self):
        if self._balance != 0:
            print('The bank account ' + str(self.account_number) + ' cannot be closed, as its balance is ' + str(self._balance) + ' GBP')
        else:
            # decrement the no_accounts by 1 and close the account (by deleting the account holder) 
            self.__class__.no_accounts -= 1
            print('The bank account ' + str(self.account_number) + ' has been closed.')
            del(self)

    def calc_interest(self, num_years):
        start_amount = self.get_balance()
        ann_int_rate = self.__class__._BankAccount__annual_interest_rate
        return self.interest(start_amount, ann_int_rate, num_years)

    @staticmethod
    def interest(starting_balance, interest_rate, time_period):
        return starting_balance * interest_rate * time_period
        

def max_balance_v1(acc_holders):
    max_balance = 0
    for acc_holder in acc_holders:
        if acc_holder.get_balance() > max_balance:
            max_balance = acc_holder.get_balance()
            max_balance_holder = acc_holder.name
    return max_balance, max_balance_holder

def max_balance_v2(*args):
    max_balance = 0
    for arg in args:
        if arg.get_balance() > max_balance:
            max_balance = arg.get_balance()
            max_balance_holder = arg.name
    return max_balance, max_balance_holder
    
def main():
    ah68234191 = BankAccount(68234191, '50 28 32', 'Dina Jackson', 1000)
    print('The balance is:', ah68234191.get_balance())

    ah68234192 = BankAccount(68234192, '50 28 32', 'Martin Fox', 550)
    print('The balance is:', ah68234192.get_balance())

    ah68234193 = BankAccount(68234193, '50 28 32', 'Paul Dobson', 2400)
    print('The balance is:', ah68234193.get_balance())
    
    ah68234194 = BankAccount(68234194, '50 28 32', 'Ida Turner', 3500)
    print('The balance is:', ah68234194.get_balance())

    # find the highest balance and account holder with the highest balance
    # version 1: passing list of balances to the max_balance_v1() function
    list_of_acc_holders = [ah68234191, ah68234192, ah68234193, ah68234194]
    highest_balance, acc_holder_name = max_balance_v1(list_of_acc_holders)
    # version 2: passing an unspecified number of balances to the max_balance_v2() function
    highest_balance2, acc_holder_name2 = max_balance_v2(ah68234191, ah68234192, ah68234193, ah68234194)

    # display the output:
    print('The account holder ' + acc_holder_name + ' has the highest balance: £' + str(highest_balance) + '.')
    print('The account holder ' + acc_holder_name2 + ' has the highest balance: £' + str(highest_balance2) + '.')
    
    # testing the account_number instance attribute
    print('\nTrying to change account_number:')
    ah68234191.account_number = 12345678
    print('The account_number for ah68234191 is:', ah68234191.account_number)
    
    # testing the sort_code instance attribute
    print('\nTrying to change sort_code:')
    ah68234191.sort_code = '12 34 56'
    print('The sort_code for ah68234191 is:', ah68234191.sort_code)

    # testing the name instance attribute
    print('\nTrying to change name:')
    ah68234191.name = 'Dummy Name'
    print('The name for ah68234191 is:', ah68234191.name)

    # testing the balance instance attribute
    print('\nTrying to change balance:')
    ah68234191.balance = '12 34 56'
    print('The balance for ah68234191 is:', ah68234191.balance)
    print('The balance for ah68234191 is:', ah68234191.get_balance())
    
    # testing the transaction instance attribute
    ah68234191.make_transaction(2000)
    print('\nThe transaction history for ah68234191 is:', ah68234191.get_transactions())
    print('The no. of transactions for ah68234191 is:', ah68234191.num_transactions())

    # testing the accounts class attribute and
    # the close_account() instance attribute
    BankAccount.print_no_accounts()
    # withdraw the entire balance from ah68234191's account
    ah68234191.make_transaction(-ah68234191.get_balance())
    print('\nThe balance for ah68234191 is:', ah68234191.get_balance())
    # delete the ah68234191 account holder
    ah68234191.close_account()
    # trying to close an account with zero balance
    BankAccount.print_no_accounts()
    print('BankAccount.no_accounts =', BankAccount.no_accounts)
    # trying to close an account with a positive balance
    ah68234192.close_account()
    # trying to close an account with a negative balance
    ah68234192.make_transaction(-600)
    ah68234192.close_account()
   
    # testing the annual_interest_rate class attribute
    print("\nah68234194's annual interest rate:", ah68234194.annual_interest_rate)
    print("Trying to modify the annual interest rate from an object:")
    ah68234194.annual_interest_rate = 0.005
    print("ah68234194's annual interest rate:", ah68234194.annual_interest_rate)
    #print("Trying to modify the annual interest rate from the class:")
    #BankAccount.annual_interest_rate = 0.003 # creates a new class attribute annual_interest_rate (set to 0.003); _annual_interest_rate remains unchanged
    #print("ah68234194's annual interest rate:", ah68234194.annual_interest_rate) # now that _annual_interest_rate exists, its value is printed, but it is not the real interest rate
    #print("BankAccount's annual interest rate:", BankAccount._annual_interest_rate)
    print("Trying to modify the annual interest rate using the set_annual_interest_rate() method:")
    BankAccount.set_annual_interest_rate(0.005)
    print("BankAccount's annual interest rate:", BankAccount._BankAccount__annual_interest_rate)
    
    # test the instance method calc_interest() and the
    # static method interest()
    print('\nPredicted interest earned over 1 year on account ah68234194 is £' + str(ah68234194.calc_interest(1)))
    print('Predicted interest earned over 3 years on account ah68234194 is £' + str(ah68234194.calc_interest(3)))
    print('Predicted interest earned over 5 years on account ah68234194 is £' + str(ah68234194.calc_interest(5)))
    
main()


'''
Add an attribute called login_attempts to the BankAccount class. 
Write a method called increment_login_attempts() that
increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that
resets the value of login_attempts to 0.

Make an instance of the BankAccount class and call
increment_login_attempts() several times. 
Print the value of login_attempts then call
reset_login_attempts(). Print login_attempts again to make
sure it was reset to 0.

'''