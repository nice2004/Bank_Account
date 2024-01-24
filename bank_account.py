
##
# this class represents a simple BankAccount
# Guang Song
#
class BankAccount:
    ##
    # this is the constructor
    # @param initial_balance - the initial balance to start the account 
    def __init__(self, initial_balance = 0):
        self._balance = initial_balance
    
    ##
    # @return the balance
    def get_balance(self):
        return self._balance
   
    ##
    # this method withdraw a given amount of money from the account
    # @param amount - the amount to be withdrawn, a float 
    def withdraw(self, amount):
        # if self._balance < amount:
        #     raise ValueError("Insufficient fund, amount left: %.2f" % self._balance)
        self._balance -= amount
    
    ##
    # deposit a given amount of money into the account
    # @param amount - money to be deposited, a float.    
    def deposit(self, amount):
        self._balance += amount
    
 
    ##
    # this method transfers a given amount of money from the current account to account other
    # @param amount - amount to be tranferred, a float.
    # @param other - the other BankAccount object    
    def transfer(self, amount, other):
        # if isinstance(other, BankAccount):
        self.withdraw(amount)
        other.deposit(amount)
    
    ##
    # this method returns a string representation of the object
    # @return a str.    
    def __repr__(self):
        return "BankAccount[balance=%.2f]" % self._balance
    
