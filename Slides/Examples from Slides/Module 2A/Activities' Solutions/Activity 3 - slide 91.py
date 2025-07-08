# slide 91 - Activity 3
'''
Create a copy of the Activity 2 script created earlier and
rename it to Activity 3.
Add an attribute no_accounts to the BankAccount class, to
store the number of accounts. Increment this counter by 1
every time a new account is opened, and decrement it by 1
every time an account is closed.
Include a method close_account() that closes the account of
the account holder who invokes it. If the balance on the
account holder's account is 0, the close _account() method
decrements the no_accounts attribute, prints out the message:
"The bank account <account_number> has been closed" and
closes the account by deleting the account holder, otherwise
it prints the message: "The bank account <account_number>
cannot be closed, as its balance is <balance> GBP".
Finally, include the method print_no_accounts() to print the
number of opened accounts.
Test the no_accounts attribute, the close_account() and the
print_no_accounts() methods from the main() function.

Tip: the no_accounts attribute does not relate to any particular instance; it relates to the BankAccount class

'''
class BankAccount():
    # class attributes
    no_accounts = 0
    
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


def max_balance_v1(acc_holders):
    max_balance = 0
    #max_balance_holder = ''
    for acc_holder in acc_holders:
        if acc_holder.get_balance() > max_balance:
            max_balance = acc_holder.get_balance()
            max_balance_holder = acc_holder.name
    return max_balance, max_balance_holder

def max_balance_v2(*args):
    max_balance = 0
    #max_balance_holder = ''
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