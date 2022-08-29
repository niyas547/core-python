# class of a account
# def deposite() balamce+deposite
# def withdrew() b>amount  b=b-amount
# def enquiry()    balance
class account:
    def __init__(self):
        self.balance=100000
    def deposite(self):
        deposite_amount=int(input("enter the deposite amount="))
        self.balance=self.balance+deposite_amount
    def withdrew(self):
        withdrew_amount=int(input("enter the amount to withdrew="))
        if (withdrew_amount>self.balance):
            print("insufficinet balance")
        else:
            self.balance=self.balance-withdrew_amount
    def enquiry(self):
        print("your balance is",self.balance)
a1=account()
print(a1.balance)
a1.deposite()
a1.withdrew()
a1.enquiry()