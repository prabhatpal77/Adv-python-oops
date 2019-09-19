class X:
    def __init__(self):
        print(" in constructor of x")
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
y1=Y()
y1.m1()
y1.m2()
