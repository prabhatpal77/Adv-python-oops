# E.g. encapsulation in brief in this customer application..
class Cust:
    cbname="sbi"
    def __init__(self, cname, cadd, cacno, cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def deposit(self, damt):
        self.cbal=self.cbal+damt
    def withdraw(self, wamt):
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
        print(Cust.cbname)
c1=Cust("ravana","columbo",1001,100000.00)
print(c1)
c1.deposit(20000.00)
c1.withdraw(30000.00)
c1.display()
c2=Cust("ram","ayodhya",1002,1000.00)
print(c2)
c2.deposit(3000.00)
c2.withdraw(1000.00)
c2.display()
