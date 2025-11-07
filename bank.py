class Bankacc:
    def getdata(self, accno, name, acc_type, balance):
        self.accno = accno
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Total balance:", self.balance)
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Balance after withdrawal:", self.balance)
accno = int(input("Enter the account no: "))
name = input("Enter the name: ")
acc_type = input("Enter the type: ")
balance = float(input("Enter the initial balance: "))
acc = Bankacc()
acc.getdata(accno, name, acc_type, balance)
amount = float(input("Enter amount to deposit: "))
acc.deposit(amount)
amount = float(input("Enter amount to withdraw: "))
acc.withdraw(amount)
