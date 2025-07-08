# slide 75 - Activity 2
'''
Create a copy of the Activity 1 script created earlier and
rename it to Activity 2.
Change the class BankAccount definition to make the
account_number, sort_code, name and balance instance
attributes read only, so that they cannot be changed
once set by the class constructor.
Any attempt to modify these attributes from an object needs
to invoke the attribute's setter, which should just print
out the message: "<attribute_name> cannot be modified". 
The getter for account_number, sort_code and name attributes
needs to return the current value of the attribute.
The getter for the balance instance attribute needs to print
the following message: "Use the get_balance() method to
obtain account holder's current balance."
Create the getter for transactions to return the list of
transactions made by an account holder, and two instance
methods: 
- make_transaction() that accepts the transaction amount
(any integer or float number); if not prints out the message
"The amount must be an integer or float value", otherwise
adds the transaction amount to the balance and appends the
amount to the transactions list.
- num_transactions() that returns the number of transactions
in the list of transactions.
Test all new methods from the main() function.

Tip: All three instance attributes need to bypass the setter
in the constructor. 
'''
class BankAccount():
    # constructor
    def __init__(self, acc_no, sort_code, name, amount):
        self._account_number = acc_no
        self._sort_code = sort_code
        self._name = name
        self._balance = amount
        self.transactions = []
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
    ah68234191.balance = 12000
    print('The balance for ah68234191 is:', ah68234191.balance)
    print('The balance for ah68234191 is:', ah68234191.get_balance())
    
    # testing the transaction instance attribute
    ah68234191.make_transaction(2000)
    print('\nThe transaction history for ah68234191 is:', ah68234191.get_transactions())
    print('The no. of transactions for ah68234191 is:', ah68234191.num_transactions())


main()
