# Constructors is a magic method is used to define and initialize non-static variable of a class at the time of creating object.
class Test:
    def __init__(self):
        print("in construcor of test")
    def display(self):
        print("welcome")
t1=Test()
t1.display()
t1.display()
t2=Test()
t2.display()
t2.display()
