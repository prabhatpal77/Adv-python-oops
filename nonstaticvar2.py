# non static variable with 3 objects.
class Test:
    """test non-static variable"""
    def insert(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
    def modify(self):
        self.a=self.a+100
        self.b=self.b-100
t1=Test()
print(t1)
t1.insert()
t1.display()
t1.modify()
t1.display()
t2=Test()
print(t2)
t2.insert()
t2.display()
