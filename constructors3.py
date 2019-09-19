# Parameter with constructor.
class Test:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
        print(self.b)
t1=Test(1000, 2000)
t1.display()
t2=Test(3000, 4000)
t2.display()
