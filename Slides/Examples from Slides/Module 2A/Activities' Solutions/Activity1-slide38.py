# slide 38 - Activity 2
'''
Create a class BankAccount that includes the following
instance methods:
- constructor, accepting the following instance parameters:
acc_no, sort_code, name, amount
to initialise the instance attributes: acc_no, sort_code,
name, balance (to amount) and transactions (to empty list),
and to print the message:
"New bank account opened for <name>."
- get_balance(), that returns the current balance for the
account holder
Write the client code within the main() function below the 
class definition to open an account for 4 account holders,
and display the balance for each of them.
Outside the class and the main() write a function max_balance(),
that takes any number of balances (*args) or a list of balances
and returns the highest one.
Use max_balance in main() to output the name of the account
holder with the highest balance as follows:
"The account holder <name> has the highest balance: £<balance>."
'''
class BankAccount():
    # constructor
    def __init__(self, acc_no, sort_code, name, amount):
        self.account_number = acc_no
        self.sort_code = sort_code
        self.name = name
        self.balance = amount
        self.transactions = []
        print('New bank account opened for', self.name)
        
    # instance methods
    def get_balance(self):
        return self.balance
  
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
main()
