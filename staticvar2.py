# static variable with 2 function2..
class Test:
    """Sample class to test static variable"""
    a=1000
    b=2000
    def display(self):
        print(Test.a)
        print(Test.b)
    def modify(self):
        Test.a=Test.a+100
        Test.b=Test.b-100
t1=Test()
t1.display()
t1.modify()
t1.display()
t2=Test()
t2.display()
t2.modify()
t2.display()
