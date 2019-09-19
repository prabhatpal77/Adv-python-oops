# In this example we are covering all oops concept.
class Account:
    def __init__(self, balance):
        if balance<0:
            self.balance=0.0
            print("initeal balance was invalid")
        else:
            self.balance=balance
    def credit(self, camt):
        if camt<=0:
            print("amt shoud not be negative")
            return false
        else:
            self.balance=self.balance+camt
            return True
    def debit(self, damt):
        if damt>self.balance:
            print("debit ammount exceeded account balance")
            return False
        else:
            self.balance=self.balance-damt
            return True
    def getbalance(self):
        return self.balance
class SavingAccount(Account):
    def __init__(self, balance, roi):
        super().__init__(balance)
        self.roi=roi
    def calculateInterest(self):
        inter=(self.balance*1*self.roi)/100
        return inter
class CheckingAccount(Account):
    def __init__(self, balance, tf):
        super().__init__(balance)
        self.tf=tf
    def credit(self, camt):
        status=super().credit(camt)
        if status:
            self.balance=self.balance-self.tf
    def debit(self, damt):
        status=super().debit(damt)
        if status:
            self.balance=self.balance-self.tf
class CurrentAccount(Account):
    def __init__(self, balance, od):
        super().__init__(balance)
        self.od=od
    def debit(self, damt):
        if self.balance>damt:
            self.balance=self.balance-damt
        else:
            print("overdraft limit is exceeded")
ac1=Account(10000.00)
ac1.credit(5000.00)
ac1.debit(7000.00)
print(ac1.getbalance())
ac2=Account(-10000.00)
ac2.credit(5000.00)
ac2.debit(13000.00)
print(ac2.getbalance())
sal1=SavingAccount(100000.00, 12)
sal1.credit(70000.00)
sal1.debit(20000.00)
print(sal1.getbalance())
print(sal1.calculateInterest())
cal=CheckingAccount(100000.00, 25.00)
cal.credit(70000.00)
cal.debit(20000.00)
print(cal.getbalance())
cul=CurrentAccount(100000.00, 25000.00)
cul.credit(75000.00)
print(cul.getbalance())
cul.debit(190000.00)
print(cul.getbalance())
