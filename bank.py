class Bankacc:
    def __init__(self,acccno,name,acctype,balance):
        self.accno=acccno
        self.name=name
        self.acctype=acctype
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
      if self.balance>=amount:
        self.balance-=amount
      else:
         print("insufficent balance")
    def show(self):
       print("ACCOUNT NO:",self.accno)
       print("NAME:",self.name)
       print("ACCOUNT TYPE:",self.acctype)
       print("BALANCE:",self.balance)
acc=Bankacc(1234,"Akshay","Current",20000)
acc.deposit(3000)
acc.withdraw(1000)
acc.show()
