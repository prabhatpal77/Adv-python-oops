# Destructor is a magic method and the name of destructor must be __del__():
# Destructor of class will be executed auto metically at the time of deleting that class object from the memory location.
class X:
    def __init__(self):
        print("in constructor of x")
    def m1(self):
        print("in m1 of x")
    def m2(self):
        print("in m2 of x")
    def __del__(self):
        print("in destructor of x")
x1=X()
print(x1)
x1.m1()
x1.m2()
x1=X()
print(x1)
x1.m1()
x1.m2()
