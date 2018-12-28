
# Example of Object Oriented Programming
# By Zach Perlman
# Learned from Jose Portilla, Udemy Instructor

class Account():

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,money_in):
        self.balance = self.balance + money_in
        print(f"{money_in} has been added to this account.")

    def withdrawal(self,money_out):
        if self.balance >= money_out:
            self.balance = self.balance - money_out
            print("Withdrawal Accepted")
        else:
            print("Withdrawal declined due to insufficient funds.")
    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}"