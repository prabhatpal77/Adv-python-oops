# We can access the both superclass and subclass properties by using subclass name or subclass reference var.
class X:
    a=1000
    def m1(self):
        print("in m1 of x")
class Y(X):
    b=2000
    def __init__(self):
        self.c=3000
    def m2(self):
        print("in m2 of y")
print(Y.a)
print(Y.b)
y1=Y()
y1.m1()
y1.m2()
