# If we deefine the non-static variables within the methods those non-static variable will be added to the object when
# ever we call that method on that onject.
class Test:
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
t2=Test()
print(t2)
t2.display()
