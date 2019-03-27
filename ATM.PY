class atm:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self):
        Withdraw = float(input("Enter Withdraw amount: "))
        if Withdraw > 0:
            forewardbalance = (self.balance - Withdraw)
            print("Foreward Balance  :", forewardbalance)
            self.balance = forewardbalance
        elif Withdraw > balance:
            print("No funs in account")
        else:
            print("None withdraw made")

    def desposit(self):
        print("Balance... ",self.balance)
        deposit = float(input("Enter deposit amount : "))
        if deposit > 0:
            forewardbalance = (self.balance + deposit)
            print("Forewardbalance  : ",forewardbalance)
            self.balance = forewardbalance
        else:
            print("None deposit made")
    

o1=atm("Krampus",10000)
print(o1.balance)
o1.withdraw()
print(o1.balance)
o1.desposit()
print(o1.balance)
